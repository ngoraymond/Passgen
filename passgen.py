from random import randint
def passgen(num):
    ans = ""
    possDigits = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890!@#$%^&*"
    t=0
    while t<num:
        ans+=possDigits[randint(0,len(possDigits)-1)]
        t+=1
    return ans

if __name__ == "__main__":
    print(passgen(int(input("Input what length you want the password to be: "), base=10)))