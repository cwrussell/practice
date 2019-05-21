#! /anaconda3/bin/python3

# added on test branch
# some conversion dictionaries
decimal_hex_dict = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
hex_decimal_dict = {h: d for d, h in decimal_hex_dict.items()}
binary_octal_dict = {'000': 0, '001': 1, '010': 2, '011': 3, '100': 4, '101': 5, '110': 6, '111': 7}
octal_binary_dict = {o: b for b, o in binary_octal_dict.items()}

class Number():
    """
    Number objects are numbers in decimal, binary, hexadecimal or octal
    """
    bases = {2: 'binary', 8: 'octal', 10: 'decimal', 16: 'hexadecimal'}

    def __init__(self, number, base):
        """
        Number objects are numbers in decimal, binary, hexadecimal or octal
        :param number_string: the number represented in a string, int, or float
        :param base: the base (2, 8, 10, or 16) as an int
        """
        self.initial_base = int(base)
        if self.initial_base not in bases:
            raise Exception('The base must be one of the following: 2, 8, 10, 12')

        self.initial_number = str(number)
        if self.initial_base == 10:
            self.decimal = self.initial_number
            self.set_binary()
            self.set_octal()
            self.set_hexadecimal()
        else:
            self.decimal = set_decimal(self.initial_number, self.initial_base)
            if self.initial_base == 2:
                self.binary = self.initial_number
                self.set_octal()
                self.set_hexadecimal()
            elif self.initial_base == 8:
                self.octal = self.initial_number
                self.set_binary()
                self.set_hexadecimal()
            elif self.initial_base == 16:
                self.hexadecimal = self.initial_number
                self.set_binary()
                self.set_octal()


    def set_decimal(self, num, bs):
        """
        Convert a number from binary, octal, or hexadecimal into decimal
        :param num: the number, given as a string
        :param bs: the base of the number, given as an int: 2, 8, 16
        :return:
        """
        dec = 0
        if bs == 2:
            for i, n in enumerate(reversed(num)):
                dec += (n * (2**i))
        elif bs == 8:
            pass
        elif bs == 16:
            pass


def binary_to_decimal(b: str) -> int:
    """
    Convert a binary number to decimal
    :param b: binary number (str)
    :return: the decimal conversion (int)
    """
    b = str(b)
    d = 0
    for i, n in enumerate(reversed(b)):
        d += (int(n) * (2**i))
    return d


def hex_to_decimal(h: str) -> int:
    """
    Convert a hexadecimal number to decimal
    :param h: hexadecimal (str); no '#' or '0x'
    :return: the decimal conversion (int)
    """
    hex_list = list(h)
    dec_list = [hex_decimal_dict.get(hl.upper(), hl) for hl in hex_list]
    d = 0
    for i, n in enumerate(reversed(dec_list)):
        d += (int(n) * (16**i))
    return d


def octal_to_decimal(o: str) -> int:
    """
    Convert an octal number to decimal
    :param o: the octal number (int)
    :return: the decimal conversion (int)
    """
    o = str(o)
    d = 0
    for i, n in enumerate(reversed(o)):
        d += (int(n) * (8**i))
    return d


def binary_to_hex(b: str) -> str:
    """
    Convert a binary number to hexadecimal
    :param b: the binary number (str)
    :return: the hexadecimal conversion (str)
    """
    b = str(b)
    if len(b) % 4 != 0:
        b = '0' * (4 - (len(b) % 4)) + b
    bl = [b[i:i+4] for i in range(0, len(b), 4)]
    dl = [binary_to_decimal(x) for x in bl]
    hl = [str(decimal_hex_dict.get(x, x)) for x in dl]
    return ''.join(hl)


def binary_to_octal(b: str) -> str:
    """
    Convert a binary number to octal
    :param b: the binary number (str)
    :return: the octal conversion (str)
    """
    b = str(b)
    if len(b) % 3 != 0:
        b = '0' * (3 - (len(b) % 3)) + b
    bl = [b[i:i+3] for i in range(0, len(b), 3)]
    o = ''
    for bit3 in bl:
        o += str(binary_octal_dict[bit3])
    return o


def decimal_to_binary(d: int) -> str:
    """
    Convert a decimal number to binary
    :param d: a decimal (int)
    :return: the binary conversion (str)
    """
    i = 0
    j = 1
    while j < d:
        i += 1
        j = 2 ** i
    return i, j

def decimal_to_octal():
    pass

def decimal_to_hex():
    pass

def octal_to_hex():
    pass

def octal_to_binary():
    pass

def hex_to_binary():
    pass

def hex_to_octal():
    pass
