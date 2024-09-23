import re

def check_password(password):

    pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@!#$%^&*(),.?":{}|<>])[a-zA-Z\d@!#$%^&*(),.?":{}|<>]{8,}$'
    if re.match(pattern, password):
        return True
    else:
        return False
        
with open('passwords.txt', 'r') as file:
    passwords = file.readlines()
    
for password in passwords:
    password = password.strip()  
    if check_password(password):
        print(password)
