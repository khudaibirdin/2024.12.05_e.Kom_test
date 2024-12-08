import json
import os


BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  # Корень проекта
CONFIG_PATH = os.path.join(BASE_DIR, 'configs', 'config.json')

with open(CONFIG_PATH, mode='r', encoding='utf-8') as config_file:
    config = json.load(config_file)
    