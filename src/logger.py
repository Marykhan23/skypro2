import logging
import os


cwd = os.getcwd()

print(cwd)
# Основная конфигурация logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s %(funcName)s - %(levelname)s - %(message)s',
                    filename=f"{cwd}\\..\\logs\\application.log",  # Запись логов в файл
                    filemode='w')  # Перезапись файла при каждом запуске

# Создаем логеры для различных компонентов программы
utils_logger = logging.getLogger('utils')
masks_logger = logging.getLogger('masks')
