#!/usr/bin/python3

def subhex(x):
    color = hex(x)[2:].upper()
    if len(color) == 1:
        color = "0"+color
    return color


def hexcolor(r, g, b):
    return "#{}{}{}".format(
            subhex(r),
            subhex(g),
            subhex(b))

def check_color(hex_code, hex_string):
    print(hex_code, "==", hex_string)
    assert hex_code == hex_string

check_color(hexcolor(255, 99, 71), "#FF6347")
check_color(hexcolor(184, 134, 11), "#B8860B")
check_color(hexcolor(189, 183, 107), "#BDB76B")
check_color(hexcolor(0, 0, 205), "#0000CD")
