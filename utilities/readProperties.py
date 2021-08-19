import configparser

config = configparser.RawConfigParser()
config.read("/home/manish/Documents/Programming/Python/phpTravel_Project_2021/Configurations/config.ini")

class ReadConfig:
    @staticmethod
    def getApplication_URL():
        url = config.get('common data', 'baseurl')
        return url

    @staticmethod
    def getUserName():
        user_name = config.get('common data', 'userName')
        return user_name

    @staticmethod
    def getPassword():
        password = config.get('common data', 'password')
        return password

