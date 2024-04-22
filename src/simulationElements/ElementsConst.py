
class ElementsConst:
    # SHOP OPTIONS
    SHOP_OPTIONS = ["Store's daily takings", "Shop type", "Number of regular checkouts", "Number of self-service checkouts"
                    "Number of worker", "Time of product placment in shop"]
    DEF_SHOP_VALUE = 100000 # the store's daily takings in zł
    DEF_SHOP_TYPE = "small"
    DEF_REGULAR_CHECKOUTS_NUMBER = 1
    DEF_SELF_SERVICE_CHECKOUTS_NUMBER = 1
    DEF_WORKER_NUMBER = 2 
    DEF_TIME_OF_PRODUCT_PLACMENT = 10 # time of product placment in min 

    # CLIENT OPTIONS
    CLINET_OPTIONS = ["Average cost of card", "Time of shoping", "Time of abandoning shoping", "Rush hours"]
    DEF_SHOPING_TIME = 30 # time of shoping in mins
    DEF_AVG_CART_COST = 120 # cost of the shoping cart in zł
    DEF_SHOPING_TIME_ABOUNDE = 10 # time after which the clinet will leave the shop
