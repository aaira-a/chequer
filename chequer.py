
WORDS = {'1': 'satu', '2': 'dua', '3': 'tiga', '4': 'empat', '5': 'lima',
         '6': 'enam', '7': 'tujuh', '8': 'lapan', '9': 'sembilan', '0': None,
         }


def get_digits(numstr):
    try:
        temp = numstr.split('.')[0]
        if temp == '':
            return None

        else:
            return temp

    except:
        return None


def get_decimals(numstr):
    try:
        temp = numstr.split('.')[1]

        if len(temp) == 2:
            return temp

        elif len(temp) == 1:
            return temp + '0'

        elif len(temp) > 2:
            return temp[0:2:]

    except:
        return None


def get_padded_digits_to_max_parser_limit(numstr):
    if len(numstr) < 7:
        return numstr.zfill(7)

    elif len(numstr) > 7:
        return numstr[0:7:]

    else:
        return numstr


def parse_single_digit(numstr):
    return WORDS[numstr]


def parse_two_digits(numstr):
    if is_all_zero(numstr):
        return None

    elif numstr == '10':
        return 'sepuluh'

    elif numstr == '11':
        return 'sebelas'

    elif numstr[0] == '1':
        return WORDS[numstr[1]] + ' belas'

    elif numstr[1] == '0':
        return WORDS[numstr[0]] + ' puluh'

    elif is_first_digit_zero(numstr):
        return parse_single_digit(numstr[1])

    else:
        return parse_single_digit(numstr[0]) + ' puluh ' + parse_single_digit(numstr[1])


def parse_three_digits(numstr):
    if is_all_zero(numstr):
        return None

    elif is_first_digit_zero(numstr):
        return parse_two_digits(numstr[1:3:])

    else:
        builder = []
        builder.append(parse_single_digit(numstr[0]) + ' ratus ')
        builder.append(parse_two_digits(numstr[1:3:]))
        return ''.join(x for x in builder if x is not None).strip()


def parse_four_digits(numstr):
    if is_all_zero(numstr):
        return None

    elif is_first_digit_zero(numstr):
        return parse_three_digits(numstr[1:4:])

    else:
        builder = []
        builder.append(parse_single_digit(numstr[0]) + ' ribu ')
        builder.append(parse_three_digits(numstr[1:4:]))
        return ''.join(x for x in builder if x is not None).strip()


def parse_five_digits(numstr):
    if is_all_zero(numstr):
        return None

    elif is_first_digit_zero(numstr):
        return parse_four_digits(numstr[1:5:])

    else:
        builder = []
        builder.append(parse_two_digits(numstr[0:2]) + ' ribu ')
        builder.append(parse_three_digits(numstr[2:5:]))
        return ''.join(x for x in builder if x is not None).strip()


def parse_six_digits(numstr):
    if is_all_zero(numstr):
        return None

    elif is_first_digit_zero(numstr):
        return parse_five_digits(numstr[1:6:])

    else:
        builder = []
        builder.append(parse_three_digits(numstr[0:3:]) + ' ribu ')
        builder.append(parse_three_digits(numstr[3:6:]))
        return ''.join(x for x in builder if x is not None).strip()


def parse_seven_digits(numstr):
    if is_all_zero(numstr):
        return None

    elif is_first_digit_zero(numstr):
        return parse_six_digits(numstr[1:7:])

    else:
        builder = []
        builder.append(parse_single_digit(numstr[0]) + ' juta ')
        builder.append(parse_six_digits(numstr[1:7:]))
        return ''.join(x for x in builder if x is not None).strip()


def is_all_zero(numstr):
    truth = []
    for digit in numstr:
        truth.append(bool(digit == '0'))
    return all(truth)


def is_first_digit_zero(numstr):
    return bool(numstr[0] == '0')


def is_valid_positive_number(numstr):
    try:
        number = float(numstr)
        if number > 0:
            return True

        else:
            return False

    except:
        return False
