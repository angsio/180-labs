## parrot_trouble()
def parrot_trouble(talking, hour):
    if talking:
        if ((hour < 7) or (hour > 20)):
          return True
    return False

## sum_double()
def sum_double(x, y):
    if x != y:
        return (x + y)
    else:
        return ((x + y) * 2)

## sleep-in()
def sleep_in(weekday, vacation):
    if weekday and not vacation:
        return False
    elif weekday and vacation:
        return True
    return True

## set_square()
def set_square(x):
    global ret_square
    ret_square = (x ** 2)

