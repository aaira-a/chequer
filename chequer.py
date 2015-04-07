
WORDS = {'1': 'satu', '2': 'dua', '3': 'tiga', '4': 'empat', '5': 'lima',
         '6': 'enam', '7': 'tujuh', '8': 'lapan', '9': 'sembilan',
         }


def get_digits(numstr):
    return numstr.split('.')[0]


def get_decimals(numstr):
    try:
        return numstr.split('.')[1]
    except:
        ValueError


def parse_single_digit(numstr):
    return WORDS[numstr]


def parse_two_digits(numstr):
    if numstr == '00':
        return None

    elif numstr == '10':
        return 'sepuluh'

    elif numstr == '11':
        return 'sebelas'

    elif numstr[0] == '1':
        return WORDS[numstr[1]] + ' belas'

    elif numstr[1] == '0':
        return WORDS[numstr[0]] + ' puluh'

    elif numstr[0] == '0':
        return parse_single_digit(numstr[1])

    else:
        return parse_single_digit(numstr[0]) + ' puluh ' + parse_single_digit(numstr[1])


def parse_three_digits(numstr):
    if numstr == '000':
        return None

    elif numstr[0] == '0':
        return parse_two_digits(numstr[1:3:])

    else:
        builder = []
        builder.append(parse_single_digit(numstr[0]) + ' ratus ')
        builder.append(parse_two_digits(numstr[1:3:]))
        return ''.join(x for x in builder if x is not None).strip()


def parse_four_digits(numstr):
    builder = []
    builder.append(parse_single_digit(numstr[0]) + ' ribu ')
    builder.append(parse_three_digits(numstr[1:4:]))
    return ''.join(x for x in builder if x is not None).strip()
