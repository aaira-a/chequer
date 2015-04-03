
def get_digits(numstr):
    return numstr.split('.')[0]


def get_decimals(numstr):
    try:
        return numstr.split('.')[1]
    except:
        ValueError
