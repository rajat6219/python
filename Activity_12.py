def input_number():
    input_string = input('Enter 3 numbers separated by space ')
    list = input_string.split()
    return list[0],list[1],list[2]

def compare(a, b, c):
    if (a >= b) and (a >= c):
        return a
    elif(b >= c):
        return b 
    else:
        return c
        
def display(a, b, c, greatest):
    print(f'{greatest} is the greatest number among {a},{b} and {c}')


def main():
    a,b,c = input_number()
    greatest = compare(a,b,c)
    display(a,b,c,greatest)
main()

