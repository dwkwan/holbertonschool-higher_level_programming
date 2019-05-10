#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) == str:
        roman_ref = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500,
                     'M': 1000}
        sum = 0
        flag = 0
        for i in range(len(roman_string)):
            if flag:
                flag = 0
                continue
            for key in roman_ref:
                if roman_string[i] == key and i != len(roman_string) - 1:
                    if roman_string[i] == 'I' and roman_string[i + 1] == 'V':
                        sum += 4
                        flag = 1
                    elif roman_string[i] == 'I' and roman_string[i + 1] == 'X':
                        sum += 9
                        flag = 1
                    elif roman_string[i] == 'X' and roman_string[i + 1] == 'L':
                        sum += 40
                        flag = 1
                    elif roman_string[i] == 'X' and roman_string[i + 1] == 'C':
                        sum += 90
                        flag = 1
                    elif roman_string[i] == 'C' and roman_string[i + 1] == 'D':
                        sum += 400
                        flag = 1
                    elif roman_string[i] == 'C' and roman_string[i + 1] == 'M':
                        sum += 900
                        flag = 1
                    else:
                        sum += roman_ref[key]
                elif roman_string[i] == key:
                    sum += roman_ref[key]
        return sum
    return 0
