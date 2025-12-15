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

---

# Инструмент автоматического именования (Auto Namer) для Unreal Engine 5

Этот скрипт на Python обеспечивает соблюдение соглашений об именовании для выбранных ассетов в Content Browser (Браузере контента) Unreal Engine.

## Функции

- **Авто-переименование**: Автоматически добавляет префиксы к ассетам на основе их класса (например, `Texture2D` -> `T_`).
- **Обнаружение коллизий**: Предотвращает переименование, если ассет с целевым именем уже существует.
- **Идемпотентность**: Пропускает ассеты, которые уже имеют правильный префикс.
- **Логирование**: Предоставляет понятную обратную связь в Output Log (Журнале вывода).

## Поддерживаемые префиксы

| Класс (Class) | Префикс |
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

## Установка и Использование

1.  **Откройте Unreal Engine 5**.
2.  **Откройте Output Log**: Перейдите в `Window` (Окно) -> `Output Log` (Журнал вывода).
3.  **Выберите ассеты**: Выделите ассеты, которые вы хотите переименовать, в Content Browser.
4.  **Запустите скрипт**:
    - Переключите режим ввода в Output Log с `Cmd` на `Python`.
    - Скопируйте и вставьте содержимое `AutoNamer.py` в строку ввода и нажмите Enter.
    - ИЛИ, если файл находится в вашем пути python (python path), вы можете импортировать и запустить его:
      ```python
      import AutoNamer
      AutoNamer.rename_assets()
      ```
      *(Примечание: Вам может потребоваться перезагрузить модуль, если вы внесли изменения: `import importlib; importlib.reload(AutoNamer)`)*

## Требования

- Unreal Engine 5 с включенным плагином Python Scripting Plugin.
