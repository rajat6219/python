def input_number():
	num1 = int(input('Enter the first number: '))
	num2 = int(input('Enter the second number: '))
	return num1, num2

def add(a, b):
	return a+b

def display(a, b, c):
	print(f'{a} + {b} = {c}')


def main():
	num1, num2 = input_number()
	answer = add(num1, num2)
	display(num1, num2, answer)
main()
