str = input("Enter a string to reverse : ")
rev = ""

def strRev():
    for i in range(1,len(str)+1):
        # a = str[len(str)-i]
        global rev
        rev += str[len(str)-i]
    return rev

print(f"The reversed string is {strRev()}")