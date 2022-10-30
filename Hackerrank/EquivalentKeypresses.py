def EquivalentKeypresses(strArr):
    # code goes here
    arr1 = strArr[0].split(",")
    new1 = ""
    for i in arr1:
        # print(i)
        if i != '-B':
            new1 = new1 + i
        elif i == '-B':
            new1 = new1[0:-1]
    # print(new1)

    arr2 = strArr[1].split(",")
    new2 = ""
    for i in arr2:
        # print(i)
        if i != '-B':
            new2 = new2 + i
        elif i == '-B':
            new2 = new2[0:-1]
    # print(new2)

    if new1 == new2:
        return True
    else:
        return False

    # return strArr


# keep this function call here
print(EquivalentKeypresses(input()))