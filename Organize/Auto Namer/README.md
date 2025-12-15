# Auto Namer Tool for Unreal Engine 5

This Python script enforces naming conventions on selected assets in the Unreal Engine Content Browser.

## Features

- **Auto-Renaming**: Automatically adds prefixes to assets based on their class (e.g., `Texture2D` -> `T_`).
- **Collision Detection**: Prevents renaming if an asset with the target name already exists.
- **Idempotency**: Skips assets that already have the correct prefix.
- **Logging**: Provides clear feedback in the Output Log.

## Supported Prefixes

| Class | Prefix |
| :--- | :--- |
| Texture2D | `T_` |
| Material | `M_` |
| MaterialInstanceConstant | `MI_` |
| StaticMesh | `SM_` |
| SkeletalMesh | `SK_` |
| Blueprint | `BP_` |
| ParticleSystem | `P_` |
| SoundWave | `S_` |
| Level | `L_` |

## Installation & Usage

1.  **Open Unreal Engine 5**.
2.  **Open the Output Log**: Go to `Window` -> `Output Log`.
3.  **Select Assets**: Select the assets you want to rename in the Content Browser.
4.  **Run the Script**:
    - Change the input mode in the Output Log from `Cmd` to `Python`.
    - Paste the contents of `AutoNamer.py` into the input line and press Enter.
    - OR, if the file is in your python path, you can import and run it:
      ```python
      import AutoNamer
      AutoNamer.rename_assets()
      ```
      *(Note: You may need to reload the module if you make changes: `import importlib; importlib.reload(AutoNamer)`)*

## Requirements

- Unreal Engine 5 with Python Scripting Plugin enabled.
