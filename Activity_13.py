def input_number():
    start = int(input("Enter the start number: "))
    stop = int(input("Enter the stop number: "))
    return start,stop
  
def iteration(start,stop):
    for num in range(start, stop + 1):
        if num % 2 != 0:
            print(num, end=",")
    
def main(): 
    start,stop = input_number()
    iteration(start,stop)    
    
main()        
