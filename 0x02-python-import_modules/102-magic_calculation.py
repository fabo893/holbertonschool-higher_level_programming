#!/urs/bin/python3
def magic_calculation(a, b):
    from magic_calculation_102 import add, sub
    if a < b:
        cal = add(a, b)
        for x in range(4, 6):
            cal = add(cal, x)
        return cal
    else:
        return sub(a, b)
