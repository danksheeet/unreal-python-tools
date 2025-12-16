import unreal
import os
import sys

# Constants
MENU_NAME = "LevelEditor.LevelEditorToolBar.UserScriptsMenu"
TOOLBAR_NAME = "LevelEditor.LevelEditorToolBar"
COMBO_BUTTON_NAME = "UserScriptsCombo"

def run_script(script_path):
    """
    Global function to execute a script.
    Called by the menu entry command string.
    """
    if not os.path.exists(script_path):
        unreal.log_error(f"Script Launcher: Script not found at {script_path}")
        return

    unreal.log(f"Script Launcher: Executing {script_path}")
    try:
        # read and exec
        with open(script_path, "r", encoding="utf-8") as f:
            code = f.read()
            # Execute in a new namespace or globals? 
            # Globals allows it to access 'unreal' if imported there, but cleaner to use a dict.
            # However, for simple scripts, they often expect __name__ == "__main__" check to fail or work.
            # Let's use a custom global dict but copy current globals to it?
            # Simplest for UE python usage: exec in a new dict but give it 'unreal'.
            
            # Actually, standard behavior for 'Execute Python Script' in UE is often just running it.
            # We will use a passed globals dict that includes 'unreal'.
            script_globals = {
                "__file__": script_path,
                "__name__": "__main__",
                "unreal": unreal
            }
            exec(code, script_globals)
    except Exception as e:
        unreal.log_error(f"Script Launcher: Error executing {script_path}: {e}")
        # Also show dialog for visibility
        unreal.EditorDialog.show_message(
            title="Script execution error",
            message=str(e),
            message_type=unreal.AppMsgType.OK
        )

class ScriptLauncherSetup:
    def __init__(self):
        self.menus = unreal.ToolMenus.get()
        # Assume this file is in Content/Python
        self.python_root = os.path.dirname(__file__)
        self.create_menu()

    def get_scripts(self):
        """
        Recursively find .py files in Content/Python, excluding init_unreal.py and this file.
        """
        scripts = []
        # We want to scan the folder where this file resides
        scan_root = self.python_root
        
        for root, dirs, files in os.walk(scan_root):
            for file in files:
                if file.endswith(".py"):
                    # Exclude the infrastructure scripts
                    if file in ["init_unreal.py", "script_launcher.py"]:
                        continue
                        
                    full_path = os.path.join(root, file)
                    rel_path = os.path.relpath(full_path, scan_root)
                    # Label: subdir > file
                    label = rel_path.replace(os.path.sep, " > ")
                    scripts.append((label, full_path))
        return sorted(scripts, key=lambda x: x[0])

    def create_menu(self):
        unreal.log("Script Launcher: Creating menu...")
        
        # DEBUG: Check if toolbar exists
        found_toolbar = self.menus.find_menu(TOOLBAR_NAME)
        unreal.log(f"Script Launcher: Explicit find_menu('{TOOLBAR_NAME}') returned: {found_toolbar}")

        # 1. Try Main Menu (Top bar) - This is usually safer/easier to see
        # Add a "Scripts" menu to the Main Menu bar
        main_menu = self.menus.extend_menu("LevelEditor.MainMenu")
        # Add to the end or specific section? 'Window' is a good place.
        # But MainMenu is a bar, sections are implicitly the top level items.
        # Let's add a new top-level menu "Scripts"
        # Accessing the "Help" section usually puts it at the end
        scripts_main_menu = main_menu.add_sub_menu(
            owner=self.menus.get_name(),
            section_name="Help", 
            name="ScriptsMainMenu",
            label="Scripts",
            tool_tip="Exec Scripts"
        )
        
        # Populate Main Menu Scripts
        self.populate_menu(scripts_main_menu)

        # 2. Try Toolbar again
        toolbar = self.menus.extend_menu(TOOLBAR_NAME)
        unreal.log(f"Script Launcher: Extended toolbar {toolbar}")

        # Add sub menu "UserScriptsCombo" to "Content" section
        scripts_toolbar_menu = toolbar.add_sub_menu(
            owner=self.menus.get_name(),
            section_name="Content",
            name="UserScriptsCombo",
            label="Scripts",
            tool_tip="Execute Python Scripts"
        )
        self.populate_menu(scripts_toolbar_menu)

        self.menus.refresh_all_widgets()

    def populate_menu(self, menu_obj):
        # Refresh Button
        entry = unreal.ToolMenuEntry(
            name="RefreshScripts",
            type=unreal.MultiBlockType.MENU_ENTRY,
            insert_position=unreal.ToolMenuInsert("", unreal.ToolMenuInsertType.FIRST)
        )
        entry.set_label("Refresh Scripts")
        entry.set_string_command(
            unreal.ToolMenuStringCommandType.PYTHON, 
            "", 
            "import script_launcher; import importlib; importlib.reload(script_launcher); script_launcher.setup()"
        )
        menu_obj.add_menu_entry("Scripts", entry)

        # Scripts
        scripts = self.get_scripts()
        for label, path in scripts:
            self.add_script_entry(menu_obj, label, path)

    def add_script_entry(self, menu, label, path):
        entry_name = f"Script_{label}"
        entry = unreal.ToolMenuEntry(
            name=entry_name,
            type=unreal.MultiBlockType.MENU_ENTRY,
            insert_position=unreal.ToolMenuInsert("", unreal.ToolMenuInsertType.DEFAULT)
        )
        entry.set_label(label)
        
        # Safe path
        clean_path = path.replace('\\', '/')
        command = f'import script_launcher; script_launcher.run_script(r"{clean_path}")'
        
        entry.set_string_command(
            unreal.ToolMenuStringCommandType.PYTHON,
            "",
            command
        )
        
        menu.add_menu_entry("Scripts", entry)

    def cleanup(self):
        # We need to clean up the entry we added to the toolbar
        # identifying it by name "UserScriptsCombo"
        # And the menu we created? add_sub_menu creates a menu internally.
        # Usually unregistering owner helps.
        self.menus.unregister_owner_by_name(self.menus.get_name())
        pass

# Global instance
_launcher_instance = None

# Delayed setup to ensure LevelEditor is loaded
_tick_handle = None
_retry_count = 0
MAX_RETRIES = 600  # Approx 10-20 seconds at 30-60fps

def setup():
    # Use extend_menu to register our extension regardless of whether the menu exists yet
    _launcher_instance = ScriptLauncherSetup()
    unreal.log("Script Launcher: Extension registered.")

if __name__ == "__main__":
    setup()


