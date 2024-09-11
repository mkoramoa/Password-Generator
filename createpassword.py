import secrets
import string
import pyperclip
import threading
import time

class PasswordGenerator:
    def __init__(self, size=13, use_upper=True, use_lower=True, use_digits=True, use_special=True):
        self.size = size
        self.use_upper = use_upper
        self.use_lower = use_lower
        self.use_digits = use_digits
        self.use_special = use_special
        self.base = self._create_base_characters()
        self.history = []

        if not (self.use_upper or self.use_lower or self.use_digits or self.use_special):
            raise ValueError("At least one character type must be selected.")

    def _create_base_characters(self):
        base = ''
        if self.use_upper:
            base += string.ascii_uppercase
        if self.use_lower:
            base += string.ascii_lowercase
        if self.use_digits:
            base += string.digits
        if self.use_special:
            base += string.punctuation
        return base

    def generate_key(self):
        while True:
            password = ''.join(secrets.choice(self.base) for _ in range(self.size))
            if self._is_valid_password(password):
                self.history.append(password)  # Store generated password in history
                return password

    def _is_valid_password(self, password):
        if len(password) < 12:
            return False
        if (sum(c.islower() for c in password) < (2 if self.use_lower else 0) or
                sum(c.isupper() for c in password) < (2 if self.use_upper else 0) or
                sum(c.isdigit() for c in password) < (3 if self.use_digits else 0) or
                sum(c in string.punctuation for c in password) < (2 if self.use_special else 0)):
            return False
        return True

    def copy_to_clipboard(self, password):
        """ Copy the generated password to the clipboard and clear it after a fixed delay of 30 seconds. """
        pyperclip.copy(password)
        print("Password copied to clipboard!")
        # Start a timer to clear the clipboard after 30 seconds
        threading.Thread(target=self.clear_clipboard, args=(30,)).start()

    def clear_clipboard(self, delay):
        """ Clear the clipboard after a specified delay. """
        time.sleep(delay)
        pyperclip.copy("")  # Clear the clipboard
        print("Clipboard cleared after {} seconds.".format(delay))

    def return_key(self):
        password = self.generate_key()
        self.copy_to_clipboard(password)
        return password
    



# Example usage
if __name__ == "__main__":
    try:
        size = int(input("Enter the desired password length (minimum 13): "))
        # Check for valid password length input
        while(size<13):
            size = int(input("Password length was less than the minimum(13). Enter the desired password length (minimum 13): "))
        use_upper = input("Include uppercase letters? (y/n): ").lower() == 'y'
        use_lower = input("Include lowercase letters? (y/n): ").lower() == 'y'
        use_digits = input("Include digits? (y/n): ").lower() == 'y'
        use_special = input("Include special characters? (y/n): ").lower() == 'y'

        password_gen = PasswordGenerator(size=size, use_upper=use_upper, use_lower=use_lower, use_digits=use_digits, use_special=use_special)
        generated_password = password_gen.return_key()
        

    except ValueError as ve:
        print(f"Error: {ve}")
