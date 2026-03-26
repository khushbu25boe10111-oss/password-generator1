import random
import string

print("🔐 Password Generator")

length = int(input("Enter password length: "))

use_digits = input("Include numbers? (y/n): ").lower() == 'y'
use_symbols = input("Include symbols? (y/n): ").lower() == 'y'

characters = string.ascii_letters

if use_digits:
    characters += string.digits

if use_symbols:
    characters += string.punctuation

password = ''.join(random.choice(characters) for _ in range(length))

print("\n✅ Generated Password:", password)