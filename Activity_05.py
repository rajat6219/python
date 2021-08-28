input_string = input('Enter 5 elements of a list separated by comma ')
user_list = input_string.split(',')
print('list: ', user_list)
for i in range(len(user_list)):
    user_list[i] = int(user_list[i])
print("Sum = ", sum(user_list))
