from lib.logger import mylogger as logger


def delete_option_a(arr, n, customer):
    logger.debug("[OptionA - Delete] : {}, {}, {}".format(len(arr), n, customer))
    i = 0
    while i < n and arr[i] != customer:
        logger.debug("i < n and {} != {}, i += 1".format(arr[i], customer))
        i += 1
    if i == n:
        logger.debug("{} == {}, {} not found".format(i, n, customer))
        return -1, n
    else:
        logger.debug("{} != {}".format(i, n))
        while i < n - 1:
            logger.debug("Shifting array items")
            logger.debug("arr[{}] = arr[{}]".format(i, i+1))
            arr[i] = arr[i+1]
            i += 1
        logger.debug("Reached i = n -1, n -= 1 because one item has been deleted.")
        n -= 1
        return 0, n


def delete_option_b(arr, n, customer):
    logger.debug("[OptionB - Delete] : {}, {}, {}".format(len(arr), n, customer))
    i = 0
    logger.debug("Setting variable r = n - 1")
    r = n - 1
    while i < r:
        logger.debug("set position as half of the array length. m = int((i + r) / 2)")
        m = int((i+r) / 2)
        try:
            if arr[m] == customer:
                logger.debug("We got hit, best case scenario happened. arr[{}] == {}".format(m, customer))
                while m < n - 1:
                    logger.debug("Position is smaller than data length, shifting array items.")
                    arr[m] = arr[m+1]
                    logger.debug("arr[{}] = arr[{}]".format(m, m + 1))
                    m += 1
                logger.debug("Reached m = n - 1, n -= 1 because one item has been deleted.")
                n -= 1
                return 0, n
            elif arr[m] > customer:
                logger.debug("{} is larger than {} using string comparison".format(arr[m], customer))
                logger.debug("Moving forward... r = m - 1")
                r = m - 1
            else:
                logger.debug("{} is smaller than {} using string comparison".format(arr[m], customer))
                logger.debug("Moving backward... r = m + 1")
                i = m + 1
        except TypeError:
            logger.error("TypeError occur...")
            continue
    return -1, n


