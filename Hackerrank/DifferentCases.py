def DifferentCases(strParam):
  import re
  a1 = strParam
  #print(a1)
  a2 = a1.split()
  #print(a2)
  a3 = re.findall(r"[\w']+|[.,!?;]", a1)
  #print(a3)
  newnew = ""
  for i in a3:
    edited = ""
    edited = i.lower()
    edited = edited.capitalize()
    newnew = newnew + edited
  #print(newnew)
  return newnew

# keep this function call here
print(DifferentCases(input()))