from utilities.customLogger import LogGen


class A:
    @staticmethod
    def a():
        return "I am A"


class B:
    a = A.a()
    print(a)

    def b(self):
        if "am" in self.a:
            print("yewww")
        else:
            print("whuuu")

# class Imple_log():
#     log = LogGen.loggen()
#
#     def logCheckMethod(self):
#         print("log instance is created....")
#         self.log.info("this is first log entry")
#         print("***********happy ending from class method")
