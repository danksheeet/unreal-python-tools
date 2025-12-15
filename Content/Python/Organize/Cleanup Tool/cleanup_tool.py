import unreal
import os

def fix_redirectors(path="/Game"):
    """
    Scans the project (or selected path) for redirectors and fixes them up.
    """
    asset_registry = unreal.AssetRegistryHelpers.get_asset_registry()
    asset_tools = unreal.AssetToolsHelpers.get_asset_tools()

    # Create a filter to find ObjectRedirectors
    asset_filter = unreal.ARFilter(
        class_names=["ObjectRedirector"],
        package_paths=[path],
        recursive_paths=True
    )

    # Get all redirectors
    redirector_assets = asset_registry.get_assets(asset_filter)
    
    if not redirector_assets:
        unreal.log("Cleanup Tool: No redirectors found in " + path)
        return

    unreal.log(f"Cleanup Tool: Found {len(redirector_assets)} redirectors. Fixing up...")

    # Load assets mainly because fix_up_referencers expects objects, not asset data
    redirector_objects = []
    for asset_data in redirector_assets:
        # Use get_asset() to load the object
        redir = asset_data.get_asset()
        if redir:
            redirector_objects.append(redir)

    if redirector_objects:
        # Fix up referencers
        try:
            asset_tools.fix_up_referencers(redirector_objects)
            unreal.log("Cleanup Tool: Fix Up Redirectors Complete.")
        except AttributeError:
            unreal.log_error("Cleanup Tool: 'fix_up_referencers' not found on AssetTools.")
            unreal.log_warning("Available methods on AssetTools:")
            for member in dir(asset_tools):
                if not member.startswith("_"):
                    unreal.log_warning(f"  {member}")
        except Exception as e:
            unreal.log_error(f"Cleanup Tool: Error fixing redirectors: {e}")
    else:
        unreal.log_warning("Cleanup Tool: Failed to load redirector objects.")

def delete_empty_folders(path="/Game"):
    """
    Scans the project for empty directories and deletes them.
    """
    editor_asset_lib = unreal.EditorAssetLibrary()
    asset_registry = unreal.AssetRegistryHelpers.get_asset_registry()
    
    unreal.log(f"Cleanup Tool: Scanning for empty folders in {path}...")
    
    all_folders = []
    
    def collect_folders(current_path):
        # Use AssetRegistry to get sub-paths
        sub_paths = asset_registry.get_sub_paths(current_path, recurse=False)
        for sub_path in sub_paths:
            all_folders.append(sub_path)
            collect_folders(sub_path)
            
    try:
        collect_folders(path)
    except Exception as e:
        unreal.log_error(f"Cleanup Tool: Error listing directories: {e}")
        return

    # Sort folders by length in descending order to process deepest folder first
    all_folders.sort(key=len, reverse=True)
    
    deleted_count = 0
    
    with unreal.ScopedSlowTask(len(all_folders), "Cleaning up empty folders...") as slow_task:
        slow_task.make_dialog(True)
        
        for folder in all_folders:
            if slow_task.should_cancel():
                break
                
            slow_task.enter_progress_frame(1, f"Checking {folder}")
            
            # Check if directory has assets 
            has_assets = editor_asset_lib.does_directory_have_assets(folder, recursive=False)
            
            # Check if directory has sub-directories
            # Since we are processing bottom-up, if a sub-directory was empty, it should have been deleted already.
            # Use AssetRegistry again to be sure
            sub_paths = asset_registry.get_sub_paths(folder, recurse=False)
            has_sub_dirs = len(sub_paths) > 0
            
            if not has_assets and not has_sub_dirs:
                if editor_asset_lib.delete_directory(folder):
                    unreal.log(f"Deleted empty folder: {folder}")
                    deleted_count += 1
                else:
                    unreal.log_warning(f"Failed to delete empty folder: {folder}")

    unreal.log(f"Cleanup Tool: Deleted {deleted_count} empty folders.")

def execute_cleanup_all():
    """
    Runs both Fix Redirectors and Delete Empty Folders on /Game
    """
    fix_redirectors("/Game")
    delete_empty_folders("/Game")

if __name__ == "__main__":
    execute_cleanup_all()
