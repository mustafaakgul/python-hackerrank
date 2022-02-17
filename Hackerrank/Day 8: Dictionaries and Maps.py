# Enter your code here. Read input from STDIN. Print output to STDOUT

number_of_inputs = int(input())
dict_of_inputs = {}

for i in range(number_of_inputs):
    key, value = input().split()
    dict_of_inputs[key] = value

print(dict_of_inputs)

while True:
    try:
        key = input()
        if key in dict_of_inputs:
            print(key+"="+dict_of_inputs[key])
        else:
            print("Not found")
    except EOFError:
        break