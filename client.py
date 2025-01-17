import json
from telethon import TelegramClient
import logging
import locale

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

DEFAULT_CONFIG = {
    "device_model": "Rerowros",
    "system_version": "14.8.1",
    "app_version": "8.4",
    "lang_code": "en",
    "system_lang_code": "en-US",
    "api_id": None,
    "api_hash": None,
}

TRANSLATIONS = {
    'en': {
        'enter_api_id': "Please enter api_id: ",
        'enter_api_hash': "Please enter api_hash: ",
        'config_created': "Created new config file at {}",
        'config_error': "Error creating config file at {}: {}",
        'missing_fields': "Config file is missing required fields.",
        'config_not_found': "Config file not found at {}. Creating new config.",
        'json_decode_error': "Error decoding JSON from {}. Creating new config.",
        'enter_field': "Please enter {}: "
    },
    'ru': {
        'enter_api_id': "Пожалуйста, введите api_id: ",
        'enter_api_hash': "Пожалуйста, введите api_hash: ",
        'config_created': "Создан новый файл конфигурации: {}",
        'config_error': "Ошибка создания файла конфигурации {}: {}",
        'missing_fields': "В файле конфигурации отсутствуют обязательные поля.",
        'config_not_found': "Файл конфигурации не найден: {}. Создаём новый.",
        'json_decode_error': "Ошибка декодирования JSON из {}: Создаём новый.",
        'enter_field': "Пожалуйста, введите {}: "
    }
}

def create_client(config_path='config.json', session_name='session_name'):
    config = load_config(config_path)
    validate_config(config)
    
    client = TelegramClient(
        session_name,
        config['api_id'],
        config['api_hash'],
        device_model=config['device_model'],
        system_version=config['system_version'],
        app_version=config['app_version'],
        lang_code=config['lang_code'],
        system_lang_code=config['system_lang_code']
    )
    return client

def create_default_config(config_path):
    config = DEFAULT_CONFIG.copy()
    
    # Запрос необходимых значений
    config['api_id'] = input("Please enter api_id: ")
    config['api_hash'] = input("Please enter api_hash: ")
    
    try:
        with open(config_path, 'w', encoding='utf-8') as config_file:
            json.dump(config, config_file, indent=4)
        logger.info(f"Created new config file at {config_path}")
        return config
    except IOError as e:
        logger.error(f"Error creating config file at {config_path}: {e}")
        return DEFAULT_CONFIG.copy()

def get_system_language():
    try:
        # Получение текущей локали
        locale.setlocale(locale.LC_ALL, '')
        system_locale = locale.setlocale(locale.LC_ALL, '').lower() 
        return 'ru' if 'russian_russia' in system_locale else 'en'
    except:
        return 'en'

def get_text(key, *args):
    lang = get_system_language()
    text = TRANSLATIONS.get(lang, TRANSLATIONS['en']).get(key, TRANSLATIONS['en'][key])
    return text.format(*args) if args else text

def create_default_config(config_path):
    config = DEFAULT_CONFIG.copy()
    
    config['api_id'] = input(get_text('enter_api_id'))
    config['api_hash'] = input(get_text('enter_api_hash'))
    
    try:
        with open(config_path, 'w', encoding='utf-8') as config_file:
            json.dump(config, config_file, indent=4)
        logger.info(get_text('config_created', config_path))
        return config
    except IOError as e:
        logger.error(get_text('config_error', config_path, str(e)))
        return DEFAULT_CONFIG.copy()

def load_config(config_path):
    try:
        with open(config_path, 'r', encoding='utf-8') as config_file:
            config = json.load(config_file)
            if config.get('api_id') is None or config.get('api_hash') is None:
                logger.warning(get_text('missing_fields'))
                return create_default_config(config_path)
            return config
    except FileNotFoundError:
        logger.warning(get_text('config_not_found', config_path))
        return create_default_config(config_path)
    except json.JSONDecodeError as e:
        logger.error(get_text('json_decode_error', config_path))
        return create_default_config(config_path)

def validate_config(config):
    for key in DEFAULT_CONFIG:
        if config.get(key) is None:
            config[key] = input(get_text('enter_field', key))
    return config