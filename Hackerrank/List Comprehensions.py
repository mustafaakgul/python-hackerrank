def condition(x):
    return True


if __name__ == '__main__':

    x = int(input())
    print(x)
    y = int(input())
    print(y)
    z = int(input())
    print(z)
    n = int(input())
    print(n)

    # matrix = [[i, j, k] for i in range(0, 6) for j in range(0, 6) for k in range(0, 6) if i + j + k != n]
    # matrix = [i for i in range(3)]
    # print(matrix)
    # matrix_list_comprehension = [[i for i in range(3)] for j in range(3)]
    # print(matrix_list_comprehension)

    # matrix = [i for i in range(1, 5) if i % 2 == 0]
    # matrix_list_comprehension = [[i for i in range(3) if i % 2 == 0] for j in range(3)]

    """
    output = []
    abc = []
    for X in range(x + 1):
        for Y in range(y + 1):
            for Z in range(z + 1):
                if X + Y + Z != n:
                    abc = [X, Y, Z]
                    output.append(abc)
    print(output)
    """

    print(list([i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if i + j + k != n))