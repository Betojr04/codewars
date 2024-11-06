"""
Even or Odd
"""


def even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"


"""
Convert a Number to a String
"""


def number_to_string(num):
    # Return a string of the number here!
    return str(num)


""""
Vowel Count
"""


def get_count(sentence):
    a = sentence.count("a")
    e = sentence.count("e")
    i = sentence.count("i")
    o = sentence.count("o")
    u = sentence.count("u")
    total = a + e + i + o + u
    return total
