import unreal

def main():
    """
    Bulk Property Editor Tool
    
    This script iterates through selected assets in the Content Browser, filters them by a specific class,
    modifies a specified property, and saves the changes.
    """
    
    # ==================================================================================================
    # USER CONFIGURATION
    # ==================================================================================================
    # 1. Target Class: The type of asset you want to modify (e.g., unreal.Texture2D, unreal.StaticMesh)
    TARGET_CLASS = unreal.Texture2D
    
    # 2. Property Name: The exact name of the property to change (string).
    #    Tip: Hover over a property in the Details panel to see its internal name (e.g., 'sRGB', 'LODGroup').
    PROPERTY_NAME = "sRGB"
    
    # 3. Property Value: The new value to set. Ensure the type matches the property (e.g., True/False, or an Enum).
    #    Example for boolean: False
    #    Example for Enum: unreal.TextureGroup.TEXTUREGROUP_WORLD
    PROPERTY_VALUE = False
    # ==================================================================================================

    # Get the list of currently selected assets in the Content Browser
    selected_assets = unreal.EditorUtilityLibrary.get_selected_assets()
    
    if not selected_assets:
        unreal.log_warning("No assets selected. Please select assets in the Content Browser.")
        return

    modified_count = 0
    failed_count = 0
    
    unreal.log("--------------------------------------------------")
    unreal.log(f"Starting Bulk Property Edit: Setting '{PROPERTY_NAME}' to '{PROPERTY_VALUE}' for class '{TARGET_CLASS.__name__}'")
    unreal.log("--------------------------------------------------")

    with unreal.ScopedSlowTask(len(selected_assets), "Processing Assets...") as slow_task:
        slow_task.make_dialog(True) # Show the progress bar dialog
        
        for asset in selected_assets:
            # Check if the user cancelled the operation via the progress dialog
            if slow_task.should_cancel():
                unreal.log_warning("Operation cancelled by user.")
                break
                
            slow_task.enter_progress_frame(1, f"Processing: {asset.get_name()}")

            # Filter by class
            if isinstance(asset, TARGET_CLASS):
                try:
                    # Attempt to set the property
                    # set_editor_property is safer than direct assignment as it handles some editor-specific logic
                    asset.set_editor_property(PROPERTY_NAME, PROPERTY_VALUE)
                    
                    # Save the asset to disk
                    unreal.EditorAssetLibrary.save_loaded_asset(asset)
                    
                    unreal.log(f"[SUCCESS] Modified and Saved: {asset.get_path_name()}")
                    modified_count += 1
                    
                except Exception as e:
                    unreal.log_error(f"[ERROR] Failed to modify '{asset.get_name()}': {str(e)}")
                    failed_count += 1
            else:
                # Optional: Log skipped assets if you want verbose output, otherwise keep it clean
                # unreal.log(f"[SKIP] '{asset.get_name()}' is not a {TARGET_CLASS.__name__}")
                pass

    # Summary
    unreal.log("--------------------------------------------------")
    unreal.log("Bulk Property Edit Complete")
    unreal.log(f"Total Modified: {modified_count}")
    unreal.log(f"Total Failed:   {failed_count}")
    unreal.log("--------------------------------------------------")

if __name__ == "__main__":
    main()
