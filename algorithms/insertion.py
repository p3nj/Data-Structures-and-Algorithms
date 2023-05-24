from lib.logger import mylogger as logger


def insert_option_a(arr, n, new_customer):
    logger.debug("[OptionA - Insertion]: {}, {}, {}".format(len(arr), n, new_customer))
    if n < len(arr):
        logger.debug("Insert arr[{}] as {}".format(n, new_customer))
        arr[n] = new_customer
        logger.debug("Update n({}) to n + 1({})".format(n, n+1))
        n += 1
    else:
        logger.debug("The Array Is Already Full.")

    return arr, n


def insert_option_b(arr, n, new_customer):
    logger.debug("[OptionB - Insertion]: {}, {}, {}".format(len(arr), n, new_customer))
    if n < len(arr):
        i = 0
        while arr[i] is not None and arr[i] < new_customer:
            logger.debug("arr[{}] is not None and arr[{}] < {}".format(i, i, new_customer))
            i += 1
        logger.debug("j = n - 1")
        j = n - 1
        while j >= i:
            logger.debug("arr[j+1] = arr[j]")
            arr[j+1] = arr[j]
            j -= 1
        logger.debug("arr[i] = {}".format(new_customer))
        arr[i] = new_customer
        logger.debug("n + 1")
        n += 1
    else:
        logger.debug("The Array Is Already Full.")

    return arr, n


