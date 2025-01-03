#!/usr/bin/env python
import regex as re

def is_valid_phone_num(phone_number):
    if phone_number.isdigit() and len(phone_number)==10:
        print(f"{phone_number} is valid")
        return phone_number
    else:
        print(f"{phone_number} is not valid")
        

def is_valid_email(email):
    """
    Validates an email address based on a standard pattern.
    Returns True if valid, False otherwise.
    """
    # Regular expression for validating an email
    email_pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+.[a-zA-Z]{2,}$"
    
    return bool(re.match(email_pattern, email))
