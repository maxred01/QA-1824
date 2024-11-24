#!/bin/bash

# Получаем текущую директорию скрипта
SCRIPT_DIR=$(dirname "$0")

# Определяем путь к тестовому файлу относительно директории со скриптом
TEST_FILE="$SCRIPT_DIR/../tests"

# Определяем путь к директории с отчетами относительно директории со скриптом
REPORT_DIR="$SCRIPT_DIR/../reports"

# Запускаем pytest с использованием относительного пути к файлу test_my_project.py и директории с отчетами
pytest -v -s "$TEST_FILE" --alluredir="$REPORT_DIR"

#pytest -v -s /home/ubuntu/PycharmProjects/QA-1023/Maksim_Tsybulka/class_work_9_f/tests