# Organizer Tool for Unreal Engine

This tool allows you to automatically organize selected assets in the Content Browser into `Textures`, `Materials`, and `Meshes` folders.

## Installation

1.  **Enable Python Plugin**: In Unreal Engine, go to `Edit` -> `Plugins`, search for "Python Editor Script Plugin", and enable it. Restart the engine if required.
2.  **Locate Script Folder**: Locate your project's Python script folder. Usually, this is `YourProject/Content/Python`. If it doesn't exist, create it.
    *   Alternatively, you can add any folder to the Python path in `Project Settings` -> `Plugins` -> `Python`.
3.  **Copy Script**: Copy `organizer_tool.py` into that folder.

## Usage

### Method 1: Tool Menu
1.  Restart the editor or reload the Python script.
2.  The tool should appear in the main menu under `Tools` -> `Organizer Tool`.
3.  Select assets in the Content Browser.
4.  Click `Organizer Tool` in the menu.

### Method 2: Context Menu (Experimental)
1.  Right-click on selected assets in the Content Browser.
2.  Look for `Organizer Tool` in the context menu (usually under `Common Asset Actions` or at the bottom).
3.  Click it to organize.

### Method 3: Python Console
1.  Open the Output Log (`Window` -> `Output Log`).
2.  Change the input mode to `Python` (bottom left of the log window).
3.  Type `import organizer_tool; organizer_tool.organize_selected_assets()` and press Enter.

## Customization

You can modify `organizer_tool.py` to add more categories or change folder names. Look for the `organize_selected_assets` function.
