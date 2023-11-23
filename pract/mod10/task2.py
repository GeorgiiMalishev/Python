import re


def is_valid_color(color):
    """
    Метод проверяет коррекстность web цвета
    >>> is_valid_color("#21f48D")
    True
    >>> is_valid_color("#888")
    True
    >>> is_valid_color("rgb(255, 255,255)")
    True
    >>> is_valid_color("rgb(10%, 20%, 0%)")
    True
    >>> is_valid_color("hsl(200,100%,50%)")
    True
    >>> is_valid_color("hsl(0, 0%, 0%)")
    True

    >>> is_valid_color("#2345")
    False
    >>> is_valid_color("ffffff")
    False
    >>> is_valid_color("rgb(257, 50, 10)")
    False
    >>> is_valid_color("hsl(20, 10, 0.5)")
    False
    >>> is_valid_color("hsl(34%, 20%, 50%)")
    False
    """
    rgb_integer = "^rgb\((\d{1,2}|1\d\d|2[0-4]\d|25[0-5]),\s*(\d{1,2}|1\d\d|2[0-4]\d|25[0-5]),\s*(\d{1,2}|1\d\d|2[0-4]\d|25[0-5])\)$"
    rgb_percentage = "^rgb\((\d{1,2}%|100%),\s*(\d{1,2}%|100%),\s*(\d{1,2}%|100%)\)$"
    hex_color = "^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$"
    hsl = "^hsl\((\d{1,2}|[0]\d\d|2[0-4]\d|25[0-5]),\s*(\d{1,2}%|100%),\s*(\d{1,2}%|100%)\)$"

    if re.match(rgb_integer, color) or re.match(rgb_percentage, color) or re.match(hex_color, color) or re.match(hsl, color):
        return True
    return False
