import inspect
import logging


class Loggingen:
    @staticmethod
    def loggens():
        logging.basicConfig(filename="../Logs/testLog.log",
                            format='%(asctime)s: %(levelname)s: %(name)s: %(message)s',
                            level=logging.INFO)
        # loggerName1 = inspect.currentframe()
        loggerName = inspect.stack()[1][3]
        log = logging.getLogger(loggerName)
        return log


    # def test_log():
    #     print("exe test_log******************")
    #     log = Loggingen.loggens()
    #     log.info("test - calling log from different class method")


class Imple_log:
    log = Loggingen.loggens()
    print("log instance is created")
    log.info("this is first log entry")
    print("***********happy ending")
#     # Loggingen.test_log()



