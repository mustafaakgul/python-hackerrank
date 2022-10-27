from collections import Counter

if __name__ == '__main__':
    # Practice on Counter object
    # list = [2, 3, 4, 5, 6, 8, 7, 6, 5, 18]
    # counter_list = Counter(list)
    # print(type(counter_list), counter_list)
    # print(counter_list.items())
    # # # Printing Dictionary Keys and Values
    # print(counter_list.keys())
    # print(counter_list.values())

    #Problem Solving
    # space_seperated_list = input().split()
    # print(space_seperated_list, type(space_seperated_list))
    number_of_shoes = int(input())
    # print(number_of_shoes)
    space_seperated_list = input().split()
    shoes = Counter(space_seperated_list)
    number_of_customers = int(input())
    #print(number_of_customers)

    total_earned = 0
    for i in range(number_of_customers):
        size, price = map(int, input().split())
        if shoes[size]:
            total_earned += price
            shoes[size] -= 1

    print(total_earned)