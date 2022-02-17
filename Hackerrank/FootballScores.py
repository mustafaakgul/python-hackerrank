import os
import sys


def counts(teamA, teamB):
    print(teamA)
    return (2,4)
if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    teamA_count = int(input().strip())

    teamA = []

    for _ in range(teamA_count):
        teamA_item = int(input().strip())
        teamA.append(teamA_item)

    teamB_count = int(input().strip())

    teamB = []

    for _ in range(teamB_count):
        teamB_item = int(input().strip())
        teamB.append(teamB_item)

    result = counts(teamA, teamB)

    # fptr.write('\n'.join(map(str, result)))
    # fptr.write('\n')
    #
    # fptr.close()