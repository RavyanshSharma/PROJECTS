# project 4 password generator

import random
class password():
    def random(self):
        random_pass="1234567890!@#$%^&*()abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        try:
            length=int(input("enter the length of the password from 5-9:"))
            if length<5 or length>9:
                print("enter a valid numbe b/w 5-9")
            else:
                print(f"length set to {length}")
            password=''.join(random.choice(random_pass) for _ in range(length)) 
            print(f"PASSWORD GENERATED:{password}")
        except ValueError:
            print("enter a valid number")
p=password()
p.random()