def pase(parse):
    try:
        print('Your is integer : ', end = '')
        return int(parse)
    except ValueError:
        print('is float : ', end = '')
        return float(parse)
    # if len(parse) == '.':
    #    print('Your is float :', parse)
    # else:
    #    print('Your is integer :', parse)
parse = input('Type an integer ot float : ')
pase(parse)
