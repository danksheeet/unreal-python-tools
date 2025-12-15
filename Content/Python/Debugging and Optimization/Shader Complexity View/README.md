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

---

# Анализатор стоимости материалов (Material Cost Analyzer)

Скрипт на Python для Unreal Engine 5, который анализирует "стоимость" (влияние на производительность) выбранных материалов на основе их настроек.

## Функции

- **Работает с выделением**: Обрабатывает ассеты, выбранные в данный момент в Content Browser.
- **Умная фильтрация**: Автоматически выбирает только ассеты типов `Material` и `MaterialInstance`.
- **Поддержка инстансов**: Корректно обрабатывает Material Instances, проверяя переопределения (overrides) и свойства родительского материала.
- **Система оценки**: Присваивает "Оценку стоимости производительности" (Performance Cost Score), чтобы помочь выявить тяжелые материалы.

## Эвристика оценки

Начальная оценка равна **0**. Баллы добавляются или вычитаются на основе следующих правил:

### Качество полупрозрачности (Translucency Quality)
- **+25** : Режим освещения `Surface` или `SurfacePerPixelLighting`.
- **+5**  : Режим освещения `VolumetricNonDirectional`.
- **+20** : Режим смешивания `Translucent` (Базовая стоимость перерисовки/Overdraw).

### Модели затенения (Shading Models)
- **+20** : `Hair` (Волосы).
- **+15** : `ClearCoat` (Лак).
- **+10** : `Subsurface` или `SubsurfaceProfile` (Подповерхностное рассеивание).
- **-5**  : `Unlit` (Без освещения).

### Тяжелые флаги (Expensive Flags)
- **+10** : `Two Sided` (Двусторонний) - рендерит геометрию дважды.
- **+5**  : `Dithered LOD Transition` (Дизеринг при смене LOD).
- **+5**  : `Cast Ray Traced Shadows` (Отбрасывание теней с трассировкой лучей).
- **+10** : `Masked` Blend Mode (Маскированный режим смешивания).
- **+5**  : `Wireframe` (Каркасный режим).

## Использование

1. **Откройте Unreal Engine 5**.
2. Откройте **Output Log** (Window -> Output Log).
3. Выберите **Материалы (Materials)** или **Инстансы материалов (Material Instances)**, которые вы хотите проанализировать, в **Content Browser**.
4. Запустите скрипт:
    - **Вариант А (Консоль Python)**: Скопируйте содержимое `MaterialCostAnalyzer.py` и вставьте его в командную строку Python Console в Unreal.
    - **Вариант Б (Запуск файла)**: Если файл скрипта находится в вашем проекте, вы можете запустить его через `File -> Execute Python Script...` или используя команду `py "path/to/MaterialCostAnalyzer.py"`.
5. Посмотрите **Отчет о сложности (Complexity Report)** в Output Log.

## Пример вывода

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
