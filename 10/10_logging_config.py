import logging

# Настройка логгера
logging.basicConfig(filename='my_app.log', 
                    filemode='a',
                    encoding='utf-8', 
                    level=logging.DEBUG)

logging.debug('Это сообщение отладки (debug)')
logging.info('Это информационное сообщение (info)')
logging.warning('Это предупреждение (warning)')
logging.error('Это сообщение об ошибке (error)')
logging.critical('Это сообщение о критической ошибке (critical)')