#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    y = dir(hidden_4)
    for x in y:
        if x[:2] != "__":
        print("{}".format(x))
