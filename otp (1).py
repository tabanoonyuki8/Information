
import random

def generate_otp():
    # Generate an 8-digit OTP
    otp = random.randint(10000000, 99999999)  # Random number between 10 million and 99 million
    return otp

# Example usage
otp = generate_otp()
print(f"Your 8-digit OTP is: {otp}")
