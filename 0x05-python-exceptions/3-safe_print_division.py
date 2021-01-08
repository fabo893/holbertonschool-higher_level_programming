#!/usr/bin/python3
def safe_print_division(a, b):
    div = 0
    try:
        div = a / b
    except:
        div = None
    finally:
        print("Inside resul: {}".format(div))
    return div
