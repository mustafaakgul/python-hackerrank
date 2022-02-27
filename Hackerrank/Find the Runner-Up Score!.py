if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())  # Seperated by space
    arr = list(arr)
    s = set()  # cuz of dublicates not allowed
    for i in arr:
        s.add(i)
    s = sorted(s)
    print(s[-2])