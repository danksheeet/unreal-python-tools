import unreal

# Configuration: Mapping Unreal Engine classes to their prefixes
PREFIX_MAPPING = {
    unreal.Texture2D: "T_",
    unreal.Material: "M_",
    unreal.MaterialInstanceConstant: "MI_",
    unreal.StaticMesh: "SM_",
    unreal.SkeletalMesh: "SK_",
    unreal.Blueprint: "BP_",
    unreal.ParticleSystem: "P_",
    unreal.SoundWave: "S_",
    unreal.World: "L_", 
    unreal.TextureCube: "TC_",
    unreal.TextureRenderTarget2D: "RT_",
}

def rename_assets():
    """
    Renames selected assets based on the PREFIX_MAPPING.
    """
    unreal.log("AutoNamer: Script started.")
    # Get selected assets
    selected_assets = unreal.EditorUtilityLibrary.get_selected_assets()
    
    unreal.log(f"AutoNamer: Found {len(selected_assets)} assets selected.")

    if not selected_assets:
        unreal.log_warning("AutoNamer: No assets selected.")
        unreal.EditorDialog.show_message("AutoNamer", "Please select assets in the Content Browser to rename.", unreal.AppMsgType.OK)
        return

    renamed_count = 0
    for asset in selected_assets:
        # Check if the asset's class is in our mapping
        prefix = None
        for mapped_class, mapped_prefix in PREFIX_MAPPING.items():
            if isinstance(asset, mapped_class):
                 prefix = mapped_prefix
                 break
        
        if not prefix:
            unreal.log_warning(f"AutoNamer: Skipping '{asset.get_name()}' - Class '{asset.get_class().get_name()}' not in mapping.")
            continue

        old_name = asset.get_name()
        
        # Check if already starts with prefix
        if old_name.startswith(prefix):
            unreal.log(f"AutoNamer: Skipped '{old_name}' (already has prefix).")
            continue

        # Generate new name
        new_name = f"{prefix}{old_name}"
        asset_path = asset.get_path_name()
        package_path = asset.get_package().get_name()
        
        # The rename_loaded_asset expects the new package path, not just the name.
        # Wait, rename_loaded_asset(source_asset, destination_package_path)
        # destination_package_path should be the full path including the new name.
        
        # Construct new package path
        # package_path is like "/Game/Folder/Asset"
        # we want "/Game/Folder/NewName"
        
        folder_path = "/".join(package_path.split("/")[:-1])
        new_package_path = f"{folder_path}/{new_name}"

        # Check for collision
        if unreal.EditorAssetLibrary.does_asset_exist(new_package_path):
            existing_asset_data = unreal.EditorAssetLibrary.find_asset_data(new_package_path)
            existing_class = existing_asset_data.asset_class_path.asset_name
            
            msg = f"AutoNamer: Target '{new_name}' already exists. Type: {existing_class}."
            if str(existing_class) == "ObjectRedirector":
                msg += " (It is a hidden Redirector! Right-click folder and 'Fix Up Redirectors' to clean it.)"
            
            unreal.log_warning(msg)
            continue

        # Rename
        success = unreal.EditorAssetLibrary.rename_loaded_asset(asset, new_package_path)
        
        if success:
            unreal.log(f"AutoNamer: Renamed '{old_name}' to '{new_name}'")
        else:
            unreal.log_error(f"AutoNamer: Failed to rename '{old_name}' to '{new_name}'")

if __name__ == "__main__":
    rename_assets()
