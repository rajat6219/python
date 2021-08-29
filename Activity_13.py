print('To find all the odd numbers between a start number till the stop number,')
def input_number():
    start = int(input("Enter the start number: "))
    stop = int(input("Enter the stop number: "))
    return start,stop
  
def iteration(start,stop):
    list = []
    for num in range(start, stop + 1):
        if (num%2 != 0):
            list.append(num)
    return list        

def display(odd_numbers):
    print(f'Required odd numbers are: {odd_numbers}')
    
def main(): 
    start,stop = input_number()
    odd_numbers = iteration(start,stop)
    display(odd_numbers)
    
main()        
