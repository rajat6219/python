input_string = input("Enter 3 numbers separated by space ")
list = input_string.split()

print('{0} is the greatest number among {1},{2} and {3}'.format(max(list),list[0],list[1],list[2]))    
