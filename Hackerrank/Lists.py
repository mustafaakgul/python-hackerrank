if __name__ == '__main__':
    N = int(input())
    list = []

    for i in range(N):
        #print(i+1, end=' ')
        command = input()
        command = command.split()
        #print(command[0])
        if command[0] == 'insert':
            # index, value = map(int, input().split())
            # l.insert(index, value)
            list.insert(int(command[1]), int(command[2]))
        elif command[0] == 'print':
            print(list)
        elif command[0] == 'remove':
            list.remove(int(command[1]))
        elif command[0] == 'append':
            list.append(int(command[1]))
        elif command[0] == 'sort':
            list.sort()
        elif command[0] == 'pop':
            list.pop()
        elif command[0] == 'reverse':
            list.reverse()


    # list = [2, 3, 4]
    # list.insert(2, 12)
    # print(list)