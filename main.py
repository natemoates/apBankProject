import math

P = float(input('Please enter account balance: '))
rate = float(input('Please enter interest rate: '))
compound = input('How often is this balance compounded? (enter cont. for continuous compounding): ')
if compound.isdigit():
    compound = int(compound)
time = float(input('How long will this balance be compounded?: '))


def truncate(number):
    factor = 10.0 ** 2
    return math.trunc(number * factor) / factor


def calc_interest(r, c, t):
    if c == "cont." or type(c) == int:
        if c != "cont." and r < 1:
            return truncate(P*((1+(r/c))**(c*t)))
        elif c == "cont." and r < 1:
            return truncate(P*(math.e ** (r * t)))
    else:
        return "you broke it"


print(calc_interest(rate, compound, time))
