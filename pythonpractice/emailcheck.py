import re
regex=r'\b[A-Za-z0-9._%+-]+[@|$][A-Za-z0-9.-]+\.[A-Za-z]{2,7}\b'
def check_email(email):
    if(re.fullmatch(regex,email)):
        print("valid email")
        return email
    else:
        print("Invalid Email")

check_email(email=input("Enter your email: "))