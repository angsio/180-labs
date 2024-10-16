## Problem 1 (Warm-up)
# Complete.

## Problem 2
# Complete.

## Problem 3
# Discussed with TA before, array UNDO works for all undo functions till infinity. Therefore, no need to do it? Confirmed.

## Problem 4
def initialize():
    global too_much_coffee
    global current_time
    global last_coffee_time
    global last_coffee_time2
    global knols
+---++
    too_much_coffee = False
    current_time = 0
    knols = 0

    last_coffee_time = -100
    last_coffee_time2 = -100

def drink_coffee():
    global too_much_coffee
    global last_coffee_time
    global last_coffee_time2
    global current_time

    if (last_coffee_time != -100) and (last_coffee_time2 != -100):
        if (current_time - last_coffee_time) <= 120:
            if (current_time - last_coffee_time2) <= 120:
                too_much_coffee = True

    last_coffee_time2 = last_coffee_time
    last_coffee_time = current_time

def study(minutes):
    global knols
    global current_time
    global too_much_coffee
    global last_coffee_time

    current_time = current_time + minutes

    if too_much_coffee:
        knols = knols + 0
    else:
        if current_time - last_coffee_time <= 10:
            knols = knols + (minutes * 10)
        else:
            knols = knols + (minutes * 5)

if __name__ == "__main__":
    initialize()    # start the simulation
    study(60)       # knols = 300
    study(20)       # knols = 400
    drink_coffee()  # knols = 400
    study(10)       # knols = 500
    drink_coffee()  # knols = 500
    study(10)       # knols = 600
    drink_coffee()  # knols = 600, 3rd coffee in 20 minutes
    study(10)       # knols = 600

    print (knols)

## Problem 5
# Working on it.

### OLD THINGS
## Problem 4
# def leibniz_formula(iterations):
#     total = 0
#
#     for item in range(iterations):
#         total = total + (((-1) ** item) / (2 * item + 1))
#     return total * 4  # Multiply by 4 to get pi()
#
# if __name__ == "__main__":
#     print(leibniz_formula(1000))

## Problem 5
# def gcd(n, m):
#     max_gcd = 1
#
#     for item in range(1, min(n, m) + 1):
#         if n % item == 0 and m % item == 0:
#             max_gcd = item
#             print (max_gcd)
#     return max_gcd
#
# if __name__ == "__main__":
#     print ("GCD of 12 and 15: ")
#     print (gcd(12, 15))
#
#     print ("GCD of 100 and 25:")
#     print (gcd(100, 25))

## Problem 6
# We have to use recursive function here such that we keep using gcd() again and again until a final end case is reahced.
#
# def euclid_main(n1, m1):
#     global n
#     global m
#     n = n1
#     m = m1
#
#     temp_value1 = -1
#     while gcd_eulicds(n, m):
#         pass
#
# def gcd_euclids(n1, m1):
#     global n
#     global m
#     n = n1
#     m = m1
#
#     if temp_value != 0:
#         if n1 >= m1:
#             temp_value1 = n % m
#             m = temp_value1
#         else:
#             temp_value1 = n % m
#             m = temp_value1
#         return True
#     else:
#         return False
#
# euclid_main(12, 15)