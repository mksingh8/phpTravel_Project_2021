import inspect
import logging


class LogGen:
    @staticmethod
    def loggen():
        logging.basicConfig(filename="../Logs/phpTravel_automation_test.log",
                            format='%(asctime)s: %(levelname)s: %(name)s: %(message)s'
                            # , datefmt='%m/%d/%Y %I:%M:%S %p'
                            , level=logging.INFO)

        logger_Name = inspect.stack()[1][3]
        logger = logging.getLogger(logger_Name)
        return logger


        # formatter = logging.Formatter('%(asctime)s: %(levelname)s: %(name)s: %(message)s')
        # fileHandler = logging.FileHandler("/home/manish/Documents/Programming/Python/phpTravel_Project_2021/Logs"
        #                     "/phpTravel_automation.log", mode='a')
        # fileHandler.setFormatter(formatter)

        # logger.addHandler(fileHandler)
        # logger.setLevel(logging.INFO)
