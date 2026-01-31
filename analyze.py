vals = {}

def analyze(code):
    if len(code) == 4:
        fun, als1, als2, als3 = code
    elif len(code) == 3:
        fun, als1, als2 = code
        als3 = None  # на всяк випадок
    elif len(code) == 2:
        fun, als1 = code
        als2 = als3 = None

    match fun:
        case 'var':
            vals[als1] = als2

        case 'print':
            if als1 == 'var':
                print(vals[als2])

        case 'add':
            if als1 in vals and als2 in vals and als3 is not None:
                vals[als3] = int(vals[als1]) + int(vals[als2])

        case 'sub':
            if als1 in vals and als2 in vals and als3 is not None:
                vals[als3] = int(vals[als1]) - int(vals[als2])

        case 'mul':
            if als1 in vals and als2 in vals and als3 is not None:
                vals[als3] = int(vals[als1]) * int(vals[als2])

        case 'div':
            if als1 in vals and als2 in vals and als3 is not None:
                vals[als3] = int(vals[als1]) / int(vals[als2])  # використовується справжнє ділення
