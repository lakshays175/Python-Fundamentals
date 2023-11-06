email = "lakshay.sharma@gmail.com"

#List of functions for string

"""
name.title()
name.upper()
name.lower()
len(name)
"""

#email= email.split("@")[0].split(".")
#print(email)

def get_name_from_email(email_address):
    name = email_address.split("@")[0].split(".")
    return name

print(get_name_from_email(email))