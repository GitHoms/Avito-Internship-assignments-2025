## Автоматизированные тесты для доски объявлений

Этот проект содержит автоматизированные тесты для проверки функциональности доски объявлений. Тесты написаны на Python с использованием библиотеки Selenium и WebDriver.


## Предварительные требования

Для запуска тестов необходимо установить следующие компоненты:

### 1. **Python v3**
   - Убедиться, что Python установлен на компьютере. Проверить это можно командой:
     ```bash
     python --version
     ```
   - Если Python не установлен, скачайте его с [официального сайта](https://www.python.org/downloads/).

### 2. **Библиотеки Python**
   - Установить необходимые библиотеки, выполнив команду:
     ```bash
     pip install selenium webdriver-manager
     ```

### 3. **Браузер Chrome**
   - Убедиться, что на компьютере установлен браузер Google Chrome.
    Тесты используют ChromeDriver, который автоматически устанавливается с помощью `webdriver-manager`.


## Установка и запуск тестов

### 1. **Клонируйте репозиторий**
   - Склонировать репозиторий с тестами на свой компьютер:
     ```bash
     git clone <ваш-репозиторий>
     cd <папка-с-проектом>
     ```

### 2. **Запуск тестов**
   - Для запуска всех тестов выполнить команду:
     ```bash
     python -m unittest
     ```
   - Тесты автоматически откроют браузер Chrome, выполнят сценарии и закроют браузер после завершения.

## Описание тестов

Проект содержит следующие тесты:

1. **Создание объявления**:
   - Проверяет возможность создания нового объявления с указанными данными (название, цена, описание, ссылка на изображение).

2. **Редактирование объявления**:
   - Проверяет возможность редактирования существующего объявления (изменение названия, цены, описания и ссылки на изображение).

3. **Поиск объявления**:
   - Проверяет функциональность поиска объявления по названию.


## Структура проекта

- `test_avito.py` — файл с автоматизированными тестами.
- `README.md` — инструкция по установке и запуску тестов.
- `TESTCASES.md` — файл с тест-кейсами.
