'''Your job is to write a function which increments a string, to create a new string.

If the string already ends with a number, the number should be incremented by 1.
If the string does not end with a number. the number 1 should be appended to the new string.
Examples:

foo -> foo1

foobar23 -> foobar24

foo0042 -> foo0043

foo9 -> foo10

foo099 -> foo100

'''
def increment_string(strng):

    # Case 1: last character is not a digit
    if not strng or not strng[-1].isdigit():
        return strng + "1"

    num_location = len(strng)

    # Move backward while digits exist
    while num_location > 0 and strng[num_location - 1].isdigit():
        num_location -= 1

    text_part = strng[:num_location]
    number_part = strng[num_location:]

    increased_number = str(int(number_part) + 1)
    increased_number = increased_number.zfill(len(number_part))

    return text_part + increased_number
