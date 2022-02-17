if __name__ == '__main__':
    x, k = map(int, input().split(" "))
    string = input().strip()

    if eval(string) == k:
        print(True)
    else:
        print(False)