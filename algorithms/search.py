from lib.logger import mylogger as logger


def search_option_a(arr, customer):
    logger.debug("[OptionA - Search] - {}, {}".format(len(arr), customer))
    for i in range(len(arr)):
        logger.debug("Looping through whole database {} / {}".format(i, len(arr)))
        if arr[i] == customer:
            logger.debug("We have a hit! arr[{}] == {}".format(i, customer))
            return i
    logger.debug("404 Not found")
    return -1


def search_option_b(arr, n, customer):
    logger.debug("[OptionB - Search] - {}, {}, {}".format(len(arr), n, customer))
    i = 0
    logger.debug("Define r = n - 1")
    r = n - 1
    while i <= r:
        logger.debug("set position as half of the array length. m = int((i + r) / 2)")
        m = int((i+r) / 2)
        if arr[m] == customer:
            logger.debug("A wild best-case appeared. arr[{}] == {}".format(m, customer))
            return m
        elif arr[m] > customer:
            logger.debug("arr[{}] is larger than {} using string comparison. r = m - 1".format(m, customer))
            r = m - 1
        else:
            logger.debug("arr[{}] is smaller than {} using string comparison. r = m + 1".format(m, customer))
            i = m + 1
    logger.debug("404 Not found")
    return -1
