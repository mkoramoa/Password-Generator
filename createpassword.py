import secrets
import string

base = string.ascii_letters + string.digits

class Password_Generator:
    def __init__(self,size=10):
        self.size = size
               
    def generate_key(self,size):
        while True:
            password = ''.join(secrets.choice(base) for i in range(size))
            if (sum(c.islower() for c in password) >=2
                    and sum(c.isupper() for c in password) >=2
                    and sum(c.isdigit() for c in password) >= 3):
                break
        return password
        
    def return_key(self,size=10):
        password = self.generate_key(size)
        return password
    