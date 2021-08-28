input_string = input('Enter 5 elements of a list separated by space ')
user_list = input_string.split()

sliced_list = user_list[0:3]
print('sliced list: ', sliced_list)

rep_list_1 = user_list
rep_list_1[0] = 0
rep_list_1[-1] = 0
print("replaced list-1", rep_list_1)

rep_list_2 = sliced_list
rep_list_2[0] = 0
rep_list_2[2] = 0
print("replaced list-2", rep_list_2)
