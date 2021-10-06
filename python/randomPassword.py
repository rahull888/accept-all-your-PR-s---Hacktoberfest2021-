import random
import string
def randomStringDigitsAlpha(stringLength=8):
    "Generate a random string of letters,digits and alpha numeric characters"
    lettersDigitsAlpha = string.ascii_lowercase+string.digits
    if stringLength%2==0:
        x = "".join(random.choice(string.ascii_uppercase))+"".join(random.choice(string.digits))
        x = list(x+"".join(random.choice(lettersDigitsAlpha)+random.choice(["!","@","#",'$',"%","^","&","*","~"]) for _ in range((stringLength//2)-1)))
        random.shuffle(x)
        return "".join(i for i in x)
    else:
        x = "".join(random.choice(lettersDigitsAlpha)+random.choice(["!","@","#",'$',"%","^","&","*","~"]) for i in range(stringLength//2))
        x = list(x + "".join(random.choice(string.ascii_uppercase) for _ in range(1)))
        random.shuffle(x)
        return "".join(i for i in x)
def randomStrings(stringLength = 8):
    "Generate a random string of letters"
    capSmallLetters = string.ascii_lowercase+string.ascii_uppercase
    return "".join(random.choice(capSmallLetters) for _ in range(stringLength))

def randomStringDigits(stringLength = 8):
    "Generate a random string of letters and numbers"
    if stringLength%2==0:
        capSmalllettersEven = string.ascii_uppercase+string.ascii_lowercase
        return "".join(random.choice(capSmalllettersEven)+random.choice(string.digits) for _ in range(stringLength // 2))
    else:
        capSmalllettersOdd = string.ascii_lowercase
        x =  "".join(
            random.choice(capSmalllettersOdd) + random.choice(string.digits) for _ in range(stringLength // 2))
        x = list(x+"".join(random.choice(string.ascii_uppercase)))
        random.shuffle(x)
        return "".join(i for i in x)
if __name__ == '__main__':
    print("<====Welcome To Random Password Generator====>")
    x = int(input("Enter which type of password do you want:\n1)Password with only capital and"
                  "small letters\n2)Medium strength Password\n3)Strong Password(Recommended)\n:"))

    if x==1:
        y = int(input("Enter the length of the password you want:"))
        print("HERE IS YOUR PASSWORD",randomStrings(y))
    elif x==2:
        y = int(input("Enter the length of the password you want:"))
        print("HERE IS YOUR PASSWORD",randomStringDigits(y))
    elif x==3:
        y = int(input("Enter the length of the password you want:"))
        print("HERE IS YOUR PASSWORD",randomStringDigitsAlpha(y))
    else:
        print("Enter a valid Option")
    print("<====THANKS====>")