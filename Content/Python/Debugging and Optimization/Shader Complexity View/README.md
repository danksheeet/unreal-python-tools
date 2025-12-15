# Material Cost Analyzer

A Python script for Unreal Engine 5 to analyze the performance cost of selected materials based on their settings.

## Features

- **Selection Based**: Works on currently selected assets in the Content Browser.
- **Smart Filtering**: Automatically processes only `Material` and `MaterialInstance` assets.
- **Instance Support**: Correctly handles Material Instances by checking overrides and parent properties.
- **Scoring System**: Assigns a "Performance Cost Score" to help identify expensive materials.

## Scoring Heuristics

The score starts at **0**. Points are added or subtracted based on the following rules:

### Translucency Quality
- **+25** : `Surface` or `SurfacePerPixelLighting` Lighting Mode.
- **+5**  : `VolumetricNonDirectional` Lighting Mode.
- **+20** : `Translucent` Blend Mode (Base Overdraw Cost).

### Shading Models
- **+20** : `Hair`.
- **+15** : `ClearCoat`.
- **+10** : `Subsurface` or `SubsurfaceProfile`.
- **-5**  : `Unlit`.

### Expensive Flags
- **+10** : `Two Sided` (Renders geometry twice).
- **+5**  : `Dithered LOD Transition`.
- **+5**  : `Cast Ray Traced Shadows`.
- **+10** : `Masked` Blend Mode.
- **+5**  : `Wireframe`.

## Usage

1. **Open Unreal Engine 5**.
2. Open the **Output Log** (Window -> Output Log).
3. Select the **Materials** or **Material Instances** you want to analyze in the **Content Browser**.
4. Run the script:
    - **Option A (Python Console)**: Copy the contents of `MaterialCostAnalyzer.py` and paste it into the Python Console command line in Unreal.
    - **Option B (File Execution)**: If you have the script file in your project, you can run it via `File -> Execute Python Script...` or using the command `py "path/to/MaterialCostAnalyzer.py"`.
5. View the **Complexity Report** in the Output Log.

## Example Output

```text
==========================================
       MATERIAL COMPLEXITY REPORT         
==========================================
[30] M_GlassWindow | (Reasons: Translucent, TwoSided)
[10] M_Foliage | (Reasons: Masked)
[0] M_BasicWall | (Reasons: None)
[-5] M_UI_Element | (Reasons: Unlit)
==========================================
Analyzed 4 materials.
```
