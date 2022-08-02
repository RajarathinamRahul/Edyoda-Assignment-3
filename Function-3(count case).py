str = input("Enter a string : ")

def strCount():
    upr = 0
    lwr = 0
    for i in str:
        val = ord(i)
        if val >= 65 and val <= 90:
            upr += 1
        elif val >= 97 and val <= 122:
            lwr += 1
    print(f"Number of Upper case character : {upr}")
    print(f"Number of Lower case character : {lwr}")

strCount()


