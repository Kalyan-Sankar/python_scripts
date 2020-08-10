#!/usr/bin/python python
# author='Kalyan Sankar'

import sys
import logging
import logging.handlers

# ----- example for basic logging -----
logfilename=sys.argv[0][:-2]+'log'
print(logfilename)
logging.basicConfig(filename=logfilename, format="%(message)s|%(asctime)s|%(levelname)s", level=logging.INFO)

def main():
    logging.info("This is test info message")
    logging.warning("This is a test warning message")

if __name__ == '__main__':
    main()

# ----- example for logging using log handlers -----
logger = logging.getLogger(f'{logfilename}')                        # create logger
logger.setLevel(logging.INFO)                                       # set log level
logger_stream_handler = logging.StreamHandler()                     # create console handler
logger_stream_handler.setLevel(logging.INFO)                        # set log level to console handler
logger_file_handler = logging.FileHandler(f'{logfilename}')         # create file handler
# to create file handler with log rotate
#logger_file_handler = logging.handlers.RotatingFileHandler(f'{logfilename}', maxBytes=1024*1024*3, backupCount=5)
logger_file_handler.setLevel(logging.INFO)                          # set log level to file handler
formatter = logging.Formatter("%(asctime)s|%(levelname)s|%(filename)s:%(lineno)d|%(message)s") # create formatter
logger_stream_handler.setFormatter(formatter)                       # set formatter to stream handler
logger_file_handler.setFormatter(formatter)                         # set formatter to file handler
logger.addHandler(logger_stream_handler)                            # add stream handler to logger
logger.addHandler(logger_file_handler)                              # add file handler to logger

class main:
    def __init__(self, logger):
        self.logger = logger

    def log_func(self):
        logger.info("This is a test info message")
        logger.warning("This is a warning message")

if __name__ == "__main__":
    start=main(logger)
    start.log_func()
