import machine
import time
import shift_register

debug_mode = True

# select segments on display to shot number
# test= dpgfedcba
num_0 = 0b00111111
num_1 = 0b00000110
num_2 = 0b01011011
num_3 = 0b01001111
num_4 = 0b01100110
num_5 = 0b01101101
num_6 = 0b01111101
num_7 = 0b00000111
num_8 = 0b01111111
num_9 = 0b01101111
num_a = 0b01110111
num_b = 0b01111100
num_c = 0b00111001
num_d = 0b01011110
num_e = 0b01111001
num_f = 0b01110001

number = [num_0, num_1, num_2, num_3, num_4, num_5, num_6, num_7, num_8, num_9, num_a, num_b, num_c, num_d, num_e, num_f]

num_dp = 0b10000000

# select actual display from all (10)
disp_0 = 0b00000001
disp_1 = 0b00000010
disp_2 = 0b00000100
disp_3 = 0b00001000
disp_4 = 0b00010000
disp_5 = 0b00100000
disp_6 = 0b01000000
disp_7 = 0b10000000
disp_Z = 0b00000000

elements = [disp_0, disp_1, disp_2, disp_3, disp_4, disp_5, disp_6, disp_7, disp_Z]


sr = shift_register.shift_reg(19, 18, 17, 16)


def prepare_date(date):
    """
    From string create list and count lenght prepare list
    :param date: string
    :return: lista and lenght(lista)
    """
    lista = list(date)
    lenght = len(lista)
    if debug_mode:
        print("Enter data:", date)
        print("Lenght enter date:", lenght)
    return lista, lenght


def prepare_date_to_display(date):
    """
    Prepare data to display. Convert to list using function delete_zero and count lenght new list
    :param date: int or float
    :return: list and lenght list
    """
    global ret, lenght, dot_position
    try:
        x = str(date)
        ret, dot_position = delete_zero(x)
        lenght = len(ret)
    except:
        print("Error. Convert int or float to string is failed!!")
    return ret, lenght, dot_position


def convert(date):
    """
    Convert char to inn value
    :param date: char
    :return: int value
    """
    global ret
    try:
        ptr = ord(date)
        ret = ptr - 48
    except:
        print("Error. Can't convert char to int!!!")
    return ret



def delete_None(date, pos_dot):
    """
    Function delete None value from lista
    :param date: lista, position dot
    :return: list
    """
    new_date = []
    for x in range(len(date)):
        if date[x] is None:
            pass
        else:
            if len(new_date) < 10 and pos_dot is not None:
                new_date.append(date[x])
            elif len(new_date) < 11:
                new_date.append(date[x])
            else:
                if debug_mode:
                    print("List is FULL")
                break
    return new_date


def list_to_string(string):
    str1 = ""
    for ele in string:
        if ele is None:
            pass
        else:
            str1 += ele
    return str1


def search_dot(data):
    """
    Function search dot in string (or list) and return position dot in all enter data.
    :param data: data to search dot
    :return: If find dots ret position dot else return None. Returns list is len 10 without dots or 11 with dots.
    """
    lista, lenght = prepare_date(data)
    increment = 0
    dot_pos = None
    for x in range(lenght):
        if lista[x] == ".":
            if debug_mode:
                print("Dot is position:", x)
            increment += 1
            dot_pos = x
        else:
            if dot_pos == 0:
                if debug_mode:
                    print(x)
            elif dot_pos != 0:
                if debug_mode:
                    print(x - 1)
    return dot_pos

def delete_zero(data):
    """
    Function delete first zero from int and delete zero from float.
    :param data: date
    :return: date_ret without first 0 or None and dot position
    """
    lista, lenght = prepare_date(data)
    first_zero = 0
    is_not_zero = 0
    data_to_ret = []
    ret_data = None
    dot_pos = search_dot(data)
    for x in range(lenght):
        if lista[x] == "0" and is_not_zero == 0:
            first_zero = x
        else:
            ret_data = lista[x]
            is_not_zero = 1
        data_to_ret.append(ret_data)
    if dot_pos is not None:
        data_to_ret.insert(0, "0")
    if debug_mode:
        print("Position zero:", first_zero)
        print("Data to display:", list_to_string(data_to_ret))
# return date without None position in list
    date_ret = delete_None(data_to_ret, dot_pos)
    return date_ret, dot_pos


class display:
    def __init__(self):
        print("Display initialization")

    def demo(self):
        print("DEMO is active")
        for i in range(10):
            sr.write(number[i], 0)
            if i < 8:
                sr.write(elements[i], 0)
                sr.write(elements[8], 1)
            else:
                sr.write(elements[8], 0)
                sr.write(elements[i - 8], 1)

    def display_date(self, date):
        lista, lenght, dot_pos = prepare_date_to_display(date)
        to_display = None
        for i in range(lenght):
            value = convert(lista[i])
            if value is dot_pos:
                sr.write((number[i] | num_dp), 0)
            else:
                sr.write(number[i], 0)
            if i < 8:
                sr.write(elements[i], 0)
                sr.write(elements[8], 1)
            else:
                sr.write(elements[8], 0)
                sr.write(elements[i - 8], 1)










