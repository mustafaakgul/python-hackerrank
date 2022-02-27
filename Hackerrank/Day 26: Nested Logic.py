first_date_string = input()
first_date = list(map(int, first_date_string.split()))
second_date_string = input()
second_date = list(map(int, second_date_string.split()))
fine = 0
if second_date[2] < first_date[2]:
    fine = 10000
elif second_date[2] == first_date[2]:
    if second_date[1] < first_date[1]:
        fine = 500*(first_date[1]-second_date[1])
    elif second_date[0] < first_date[0]:
        fine = 15*(first_date[0]-second_date[0])

print(fine)