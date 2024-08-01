import random
import string
def generate_password(length, include_uppercase=True, include_digits=True, include_punctuation=True):
    characters=string.ascii_lowercase
    if include_uppercase:
        characters+=string.ascii_uppercase
    if include_digits:
        characters+=string.digits
    if include_punctuation:
        characters+=string.punctuation
    password=''.join(random.choice(characters)for _ in range(length))
    return password
def main():
    length=int(input("Enter the desired length for the password:"))
    include_uppercase=input("Include uppercase letters? (y/n):").strip().lower()=='y'
    include_digits=input("Include digits? (y/n):").strip().lower()=='y'
    include_punctuation=input("Include punctuation? (y/n):").strip().lower()=='y'
    password=generate_password(length, include_uppercase, include_digits, include_punctuation)
    print("Generated Password:",password)
if __name__=="__main__":
    main()