import logging
import datetime

#create an instance of logger
logger=logging.getLogger('simple_loggre')

current_time=datetime.datetime.now().strftime("%I-%M%p-%B-%d-%Y")
log_path='./logs/'+current_time

#create log handler
handler=logging.FileHandler(log_path+'.log')
handler.setLevel(logging.DEBUG)

#create formatter and set it in handler
formatter=logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

logger.setLevel(level=logging.DEBUG)
logger.addHandler(handler)