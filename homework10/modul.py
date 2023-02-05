x=0
y=0

def init(a,b):
    global x,y
    x=a
    y=b

def summ():
    return x+y

def diff():
    return x-y

def multi():
    return x*y

def div():
    return x/y

def div_cel():
    return x//y

def div_ost():
    return x%y

def calculate(a,b,sign):
    res=0
    init(a,b)
    if sign == "+":
        res = summ()
    elif sign == "-":
        res = diff()
    elif sign == "*":
        res = multi()
    elif sign == "/":
        res = div()
    elif sign == "//":
        res = div_cel()
    elif sign == "%":
        res = div_ost()
    return res

def is_number(s):
    try:
        float(s) 
    except ValueError:
        return False

    return True

def is_complex(s):
    try:
        complex(s) 
    except ValueError:
        return False

    return True