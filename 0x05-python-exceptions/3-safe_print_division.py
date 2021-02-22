#!/usr/bin/python3
def safe_print_division(a, b):
    div = 0
    try:
        div = int(a) / int(b)
    except:
        div = None
    finally:
        print("Inside result: {}".format(div))
    return div
