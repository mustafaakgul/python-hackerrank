"""
# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == '__main__':
    s = "2\nHacker\nRank"
    array = s.splitlines()

    for j in range(0, len(array)):
        new_string = array[j]
        if not len(new_string) == 1:
            even_index = []
            odd_index = []
            even_s = ""
            odd_s = ""

            for i in range(0, len(new_string)):
                if i % 2 == 0:
                    even_index.append(new_string[i])
                    even_s = even_s + new_string[i]
                else:
                    odd_index.append(new_string[i])
                    odd_s = odd_s + new_string[i]

            print(even_s, "", odd_s)
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == '__main__':
    lenght = int(input())

    for j in range(0, lenght):
        s = input()
        new_string = s
        if not len(s) == 1:
            even_index = []
            odd_index = []
            even_s = ""
            odd_s = ""

            for i in range(0, len(s)):
                if i % 2 == 0:
                    even_index.append(s[i])
                    even_s = even_s + s[i]
                else:
                    odd_index.append(s[i])
                    odd_s = odd_s + s[i]

            print(even_s, odd_s)