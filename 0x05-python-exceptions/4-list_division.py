#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):
    list_div = []
    x = 0
    for num in range(list_length):
        try:
            list_div.append(my_list_1[x] / my_list_2[x])
        except TypeError:
            print("wrong type")
            list_div.append(0)
        except ZeroDivisionError:
            print("division by 0")
            list_div.append(0)
        except IndexError:
            print("out of range")
            list_div.append(0)
        finally:
            x = x + 1
    return list_div
