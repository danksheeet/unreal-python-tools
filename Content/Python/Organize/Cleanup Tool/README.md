# Project Cleanup Tool

A utility script for Unreal Engine 5 to maintain project hygiene by fixing up redirectors and removing empty folders.

## Features

- **Fix Redirectors**: Scans the project (defaulting to `/Game`) for `ObjectRedirector` assets (leftovers from moving/renaming assets) and fixes up all references to point to the new location, then removes the redirectors.
- **Delete Empty Folders**: Recursively scans user content for directories that contain no assets and no subfolders, ensuring a clean folder structure.

## Usage

1.  **Open Unreal Engine 5**.
2.  **Open Output Log**: `Window` -> `Output Log`.
3.  **Run the script**:
    ```python
    import cleanup_tool
    cleanup_tool.execute_cleanup_all()
    ```
    This will run both operations on the `/Game` content folder.

### Individual Functions

You can also run functions individually or on specific paths:

```python
import cleanup_tool

# Fix redirectors only in a specific folder
cleanup_tool.fix_redirectors("/Game/Characters")

# Delete empty folders only
cleanup_tool.delete_empty_folders("/Game")
```

## Requirements

- Unreal Engine 5 with Python Scripting Plugin enabled.

---

# Инструмент очистки проекта (Project Cleanup Tool)

Утилита для Unreal Engine 5 для поддержания гигиены проекта: исправление редиректоров и удаление пустых папок.

## Функции

- **Исправление редиректоров (Fix Redirectors)**: Сканирует проект (по умолчанию `/Game`) на наличие ассетов `ObjectRedirector` (остатки после перемещения/переименования файлов), исправляет все ссылки, чтобы они указывали на новое местоположение, а затем удаляет редиректоры.
- **Удаление пустых папок (Delete Empty Folders)**: Рекурсивно сканирует контент пользователя на наличие папок, не содержащих ни ассетов, ни подпапок, и удаляет их.

## Использование

1.  **Откройте Unreal Engine 5**.
2.  **Откройте Output Log**: `Window` (Окно) -> `Output Log` (Журнал вывода).
3.  **Запустите скрипт**:
    ```python
    import cleanup_tool
    cleanup_tool.execute_cleanup_all()
    ```
    Это запустит обе операции для папки `/Game`.

### Отдельные функции

Вы также можете запускать функции по отдельности или для конкретных путей:

```python
import cleanup_tool

# Исправить редиректоры только в определенной папке
cleanup_tool.fix_redirectors("/Game/Characters")

# Только удалить пустые папки
cleanup_tool.delete_empty_folders("/Game")
```

## Требования

- Unreal Engine 5 с включенным плагином Python Scripting Plugin.
