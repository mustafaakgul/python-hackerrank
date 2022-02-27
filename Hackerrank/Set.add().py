# s = set('HackerRank')
# s.add('H')
# print(s)
# s.add('HackerRank')
# print(s)

if __name__ == '__main__':
    n = int(input().strip())
    s = set()
    for i in range(n):
        element_of_set = input().strip()
        s.add(element_of_set)
    print(len(s))