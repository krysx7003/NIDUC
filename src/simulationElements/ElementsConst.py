
class ElementsConst:
    # SHOP OPTIONS
    SHOP_OPTIONS = ["Shop's daily takings",
                    "Shop type",
                    "Number of regular checkouts",
                    "Number of self-service checkouts",
                    "Number of worker",
                    "Time of product placment in shop",
                    "Rush hour",
                    "All settings"]

    DEF_SHOP_VALUE = 100000 # the store's daily takings in zł
    DEF_SHOP_TYPE = "small"
    DEF_REGULAR_CHECKOUTS_NUMBER = 1
    DEF_SELF_SERVICE_CHECKOUTS_NUMBER = 1
    DEF_WORKER_NUMBER = 2 
    DEF_TIME_OF_PRODUCT_PLACMENT = 10 # time of product placment in min 
    DEF_RUSH_HOURS = 16 # hour from 0-24 when the rush hour occures

    #Number relevent to option
    VALUE = 1
    TYPE = 2
    REG_CHECKOUTS = 3
    SS_CHECKOUTS = 4
    WORKER = 5 
    TIME_OF_PRODUCT_PLACMENT = 6
    RUSH_HOUR = 7
    ALL_SHOP = 8

    # CLIENT OPTIONS
    CLINET_OPTIONS = ["Time of shoping",
                      "Average value of shoping cartime of shoping", 
                      "Time of abandoning shoping", 
                      "Number of clients",
                      "All settings"]

    DEF_SHOPING_TIME = 30 # time of shoping in mins
    DEF_AVG_CART_COST = 120 # cost of the shoping cart in zł
    DEF_SHOPING_TIME_ABOUNDE = 10 # time after which the clinet will leave the shop
    DEF_NUMBER_OF_CLIENTS = 5 # deafault number of clients in an hour

    # Numbers relevent to option
    SHOPING_TIME = 1
    CART_VALUE= 2
    ABOUNDE_TIME = 3
    CLIENT_NUM = 4
    ALL_CLIENT = 5

    # employee
    DEF_AVG_EMPLOYEE_SALARY = 3262
    DEF_SERVED_CLIENTS_PER_MINUTE = 3
    # SERVED CLIENTS PER MIN
    DEF_SERVED_CLIENTS_REGULARCHECKOUT = 3
    DEF_SERVED_CLIENTS_SELFCHECKOUT = 4
