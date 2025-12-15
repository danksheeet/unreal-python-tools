import unreal
import os

def organize_selected_assets():
    """
    Organizes selected assets in the Content Browser into 'Textures', 'Materials', and 'Meshes' folders.
    """
    # Get the libraries we need
    editor_util = unreal.EditorUtilityLibrary()
    editor_asset_lib = unreal.EditorAssetLibrary()

    # Get selected assets
    selected_assets = editor_util.get_selected_assets()

    if not selected_assets:
        unreal.log_warning("Organizer Tool: No assets selected.")
        return

    unreal.log(f"Organizer Tool: Processing {len(selected_assets)} assets...")

    for asset in selected_assets:
        # Get the class of the asset to determine type
        # We use isinstance checks or class name checks. 
        # Note: In UE Python, strict type checking is often safer with isinstance if classes are available,
        # but string checking is robust against some inheritance quirks if we just want broad categories.
        
        target_folder_name = None
        
        if isinstance(asset, unreal.Texture):
            target_folder_name = "Textures"
        elif isinstance(asset, (unreal.Material, unreal.MaterialInstance)):
            target_folder_name = "Materials"
        elif isinstance(asset, unreal.StaticMesh):
            target_folder_name = "Meshes"
        
        # If it's not one of the types we care about, skip it
        if not target_folder_name:
            continue

        # Get the full package name (e.g., /Game/MyFolder/MyAsset)
        package_name = asset.get_package().get_name()
        asset_name = asset.get_name()
        
        # Calculate parent path
        # UE paths use forward slashes.
        parent_path = package_name.rsplit('/', 1)[0]
        
        # Construct new path
        # e.g., /Game/MyFolder/Textures/MyAsset
        new_folder_path = f"{parent_path}/{target_folder_name}"
        new_asset_path = f"{new_folder_path}/{asset_name}"

        # Skip if already in the correct place
        if package_name == new_asset_path:
            continue

        # Move the asset
        # rename_asset will create directories if they don't exist
        try:
            success = editor_asset_lib.rename_asset(package_name, new_asset_path)
            if success:
                unreal.log(f"Moved {asset_name} to {target_folder_name}")
            else:
                unreal.log_error(f"Failed to move {asset_name} to {new_asset_path}")
        except Exception as e:
            unreal.log_error(f"Exception moving {asset_name}: {e}")

    unreal.log("Organizer Tool: Organization complete.")

def create_menu_entry():
    """
    Adds a menu entry to the Content Browser context menu or a tool menu.
    For simplicity and reliability, we'll add it to the 'LevelEditor.MainMenu.Tools' for now,
    or we can try to hook into the Content Browser context menu if possible.
    
    Actually, a common pattern for simple scripts is just running them. 
    But to make it a 'Tool', we can register a menu entry.
    """
    menus = unreal.ToolMenus.get()
    
    # Find the 'Tools' menu in the Main Menu bar
    main_menu = menus.find_menu("LevelEditor.MainMenu.Tools")
    if not main_menu:
        return

    # Create a script entry
    entry = unreal.ToolMenuEntry(
        name="OrganizerTool",
        type=unreal.MultiBoxType.MENU_ENTRY,
        insert_position=unreal.ToolMenuInsert("", unreal.ToolMenuInsertType.DEFAULT)
    )
    
    # Set label and tooltip
    entry.set_label("Organizer Tool")
    entry.set_tool_tip("Organize selected assets into Textures, Materials, and Meshes folders.")
    
    # Set the command to run this function
    # Note: For this to work, this script must be importable or available in the python environment.
    # We will use a dynamic command string assuming this file is 'organizer_tool.py'
    entry.set_string_command(
        type=unreal.ToolMenuStringCommandType.PYTHON,
        custom_type="organizer_tool",
        string="import organizer_tool; organizer_tool.organize_selected_assets()"
    )
    
    # Add the entry
    main_menu.add_menu_entry("Tools", entry)
    
    # Also try to add to Content Browser Context Menu
    # Note: This menu might be named differently in different UE versions or contexts.
    # Common names: "ContentBrowser.AssetContextMenu", "ContentBrowser.FolderContextMenu"
    cb_menu = menus.find_menu("ContentBrowser.AssetContextMenu")
    if cb_menu:
        # We need to find a section to add to, or add a new section.
        # "CommonAssetActions" is a safe bet usually, or just add to the end.
        # For safety, we'll just add it to the end or a custom section.
        cb_menu.add_menu_entry("CommonAssetActions", entry)
        unreal.log("Organizer Tool: Menu entry added to Content Browser context menu.")

    # Refresh the UI
    menus.refresh_all_widgets()
    unreal.log("Organizer Tool: Menu entry added to Tools menu.")

if __name__ == "__main__":
    # If run directly, just organize
    organize_selected_assets()
    
    # Also try to register the menu (optional, good for startup scripts)
    # create_menu_entry() 
