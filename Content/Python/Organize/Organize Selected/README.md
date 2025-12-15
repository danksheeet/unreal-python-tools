# Organizer Tool for Unreal Engine

This tool allows you to automatically organize selected assets in the Content Browser into categorized folders.

## Supported Asset Types

- **Textures** -> `Textures`
- **Materials & Instances** -> `Materials`
- **Static & Skeletal Meshes** -> `Meshes`
- **Blueprints** -> `Blueprints`
- **Level Sequences** -> `Sequences`
- **Sound Waves & Cues** -> `Audio`
- **Particle Systems & Niagara** -> `Particles`
- **Levels (Maps)** -> `Maps`
- **Widget Blueprints** -> `UI`

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

---

# Инструмент Организатор (Organizer Tool) для Unreal Engine

Этот инструмент позволяет автоматически сортировать выбранные ассеты в Content Browser по соответствующим папкам.

## Поддерживаемые типы ассетов

- **Текстуры (Textures)** -> `Textures`
- **Материалы и Инстансы (Materials & Instances)** -> `Materials`
- **Статические и Скелетные меши (Static & Skeletal Meshes)** -> `Meshes`
- **Блюпринты (Blueprints)** -> `Blueprints`
- **Секвенции (Level Sequences)** -> `Sequences`
- **Звуки (Sound Waves & Cues)** -> `Audio`
- **Частицы (Particles & Niagara)** -> `Particles`
- **Уровни (Levels/Maps)** -> `Maps`
- **Виджеты (Widget Blueprints)** -> `UI`

## Установка

1.  **Включите плагин Python**: В Unreal Engine перейдите в `Edit` (Правка) -> `Plugins` (Плагины), найдите "Python Editor Script Plugin" и включите его. Перезапустите движок, если потребуется.
2.  **Найдите папку скриптов**: Найдите папку для Python скриптов вашего проекта. Обычно это `YourProject/Content/Python`. Если она не существует, создайте её.
    *   Альтернативно, вы можете добавить любую папку в путь Python в `Project Settings` (Настройки проекта) -> `Plugins` (Плагины) -> `Python`.
3.  **Скопируйте скрипт**: Скопируйте `organizer_tool.py` в эту папку.

## Использование

### Способ 1: Меню инструментов (Tool Menu)
1.  Перезапустите редактор или перезагрузите Python скрипт.
2.  Инструмент должен появиться в главном меню в разделе `Tools` (Инструменты) -> `Organizer Tool`.
3.  Выберите ассеты в Content Browser.
4.  Нажмите `Organizer Tool` в меню.

### Способ 2: Контекстное меню (Экспериментально)
1.  Нажмите правой кнопкой мыши на выбранных ассетах в Content Browser.
2.  Найдите `Organizer Tool` в контекстном меню (обычно в разделе `Common Asset Actions` или внизу).
3.  Нажмите на него, чтобы организовать файлы.

### Способ 3: Консоль Python
1.  Откройте Output Log (`Window` -> `Output Log`).
2.  Переключите режим ввода на `Python` (внизу слева окна лога).
3.  Введите `import organizer_tool; organizer_tool.organize_selected_assets()` и нажмите Enter.

## Настройка

Вы можете изменить `organizer_tool.py`, чтобы добавить больше категорий или изменить имена папок. Ищите функцию `organize_selected_assets`.
