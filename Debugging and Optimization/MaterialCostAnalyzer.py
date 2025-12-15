import unreal

def analyze_materials():
    """
    Analyzes selected materials and generates a complexity report based on specific heuristics.
    """
    # 1. Get Selection
    # Retrieve selected assets from the Content Browser
    selected_assets = unreal.EditorUtilityLibrary.get_selected_assets()
    
    # Filter for Materials and Material Instances
    materials_to_analyze = []
    for asset in selected_assets:
        # Check if the asset is a Material or MaterialInstance
        if isinstance(asset, (unreal.Material, unreal.MaterialInstance)):
            materials_to_analyze.append(asset)
            
    if not materials_to_analyze:
        unreal.log_warning("Material Cost Analyzer: No Materials or Material Instances selected.")
        return

    results = []

    # 2. Analyze & Score
    for mat in materials_to_analyze:
        score = 0
        reasons = []

        # Retrieve properties using MaterialInterface methods where possible
        # These methods typically resolve overrides in Material Instances
        # Blend Mode: Available on MaterialInterface
        blend_mode = mat.get_blend_mode()
        
        # Shading Model: Only available on Material, not MaterialInstance directly (usually)
        # We need to access the base material for instances
        shading_model = None
        try:
            if isinstance(mat, unreal.Material):
                 shading_model = mat.get_editor_property("shading_model")
            elif isinstance(mat, unreal.MaterialInstance):
                 # get_base_material() returns the UMaterial at the root of the chain
                 base_mat_for_model = mat.get_base_material()
                 if isinstance(base_mat_for_model, unreal.Material):
                     shading_model = base_mat_for_model.get_editor_property("shading_model")
        except Exception:
            # Fallback or ignore if property not found (e.g. specialized material types)
            pass

        # Two Sided
        two_sided = False
        try:
            # Try to get the property directly (works for Material)
            two_sided = mat.get_editor_property("two_sided")
        except Exception:
            # If failed (likely MaterialInstance), check if it's overridden or get from base
            if isinstance(mat, unreal.MaterialInstance):
                # Check BasePropertyOverrides if available
                try:
                    overrides = mat.get_editor_property("base_property_overrides")
                    if overrides.get_editor_property("override_two_sided"):
                        two_sided = overrides.get_editor_property("two_sided")
                    else:
                        # Fallback to base material
                        base_mat_for_two_sided = mat.get_base_material()
                        if isinstance(base_mat_for_two_sided, unreal.Material):
                            two_sided = base_mat_for_two_sided.get_editor_property("two_sided")
                except Exception:
                    pass

        # Wireframe is a property of the base Material
        is_wireframe = False
        try:
            if isinstance(mat, unreal.Material):
                is_wireframe = mat.get_editor_property("wireframe")
            elif isinstance(mat, unreal.MaterialInstance):
                base_mat_for_wireframe = mat.get_base_material()
                if isinstance(base_mat_for_wireframe, unreal.Material):
                    is_wireframe = base_mat_for_wireframe.get_editor_property("wireframe")
        except Exception:
            pass
        
        # --- Heuristics ---
        
        # Blend Mode: Translucent is expensive due to overdraw
        if blend_mode == unreal.BlendMode.BLEND_TRANSLUCENT:
            score += 20
            reasons.append("Translucent")
        # Blend Mode: Masked is more expensive than Opaque but cheaper than Translucent
        elif blend_mode == unreal.BlendMode.BLEND_MASKED:
            score += 10
            reasons.append("Masked")
            
        # Two Sided: Renders geometry twice
        if two_sided:
            score += 10
            reasons.append("TwoSided")
            
        # Shading Model: Unlit is the cheapest
        if shading_model == unreal.MaterialShadingModel.MSM_UNLIT:
            score -= 5
            reasons.append("Unlit")
            
        # Wireframe: Debug rendering, adds cost
        if is_wireframe:
            score += 5
            reasons.append("Wireframe")
            
        results.append({
            "asset": mat,
            "name": mat.get_name(),
            "score": score,
            "reasons": reasons
        })

    # 3. Sorting
    # Sort by Score Descending (Most expensive first)
    sorted_results = sorted(results, key=lambda x: x["score"], reverse=True)

    # 4. Output
    unreal.log("==========================================")
    unreal.log("       Material Cost Analyzer Report      ")
    unreal.log("==========================================")
    
    for res in sorted_results:
        reasons_str = ", ".join(res["reasons"])
        if not reasons_str:
            reasons_str = "Base Cost"
            
        # Format: [Score] AssetName | (Reasons)
        log_msg = "[{}] {} | ({})".format(res["score"], res["name"], reasons_str)
        unreal.log(log_msg)
        
    unreal.log("==========================================")
    unreal.log("Analysis Complete. Processed {} materials.".format(len(sorted_results)))

if __name__ == "__main__":
    analyze_materials()
