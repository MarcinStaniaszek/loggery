import logging

# Inicjalizacja loggera
logger = logging.getLogger(__name__)


# Ustalenie poziomu od którego logi mają być zapisywane
logger.setLevel(level=logging.DEBUG)

# Tworzenie handlera
file_handler:file_handler=logging.FileHandler('file_logger.log')
file_handler.setLevel(level=logging.DEBUG)
logger.addHandler(file_handler)

# Tworzenie formattera
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
# formatter = logging.Formatter(
#     '{asctime} - {name} - {levelname} - {message}', style='{'
# )
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

# Logowanie informacji
logger.debug('I am a debug level log')
logger.info('I am info level log')
logger.warning('I am warning level log')
logger.error('I am error level log')
logger.critical('I am critical level log')
