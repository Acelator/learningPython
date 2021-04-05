import time


# Measures the time what takes a func to run
def timing(f):
    def wrap(*args, **kwargs):
        time1 = time.time()
        ret = f(*args, **kwargs)
        time2 = time.time()
        print('{:s} function took {:.3f} ms'.format(f.__name__, (time2 - time1) * 1000.0))

        return ret

    return wrap


# Given a string, it returns if it's equals to False or True
def true_or_false(string: str):
    string = string.upper()
    if string == 'FALSE':
        return False
    elif string == 'NO':
        return False
    else:
        return True
