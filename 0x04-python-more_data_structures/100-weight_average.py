#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list:
        total = 0
        divisor = 0
        for x in my_list:
            total += x[0] * x[1]
            divisor += x[1]
        return total/divisor
    return 0
