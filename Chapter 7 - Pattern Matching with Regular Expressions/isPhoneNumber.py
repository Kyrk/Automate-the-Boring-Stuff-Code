#!usr/bin/env python3
# Example program that checks if passed string matches a phone number pattern
# i.e. xxx-xxx-xxxx
def isPhoneNumber(text):
    # 12 character string
    if len(text) != 12:
        return False
    # Checking that certain elements of string are either decimals or dashes
    for i in range(0,3):
        if not text[i].isdecimal():
            return False
    if text[3] != '-':
        return False
    for i in range(4,7):
        if not text[i].isdecimal():
            return False
    if text[7] != '-':
        return False
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False
    return True

#print('Is 415-555-4242 a phone number?')
#print(isPhoneNumber('415-555-4242'))
#print('Is Moshi moshi a phone number?')
#print(isPhoneNumber('Moshi moshi'))

message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'
# Loop through indexes of message
for i in range(len(message)):
    chunk = message[i:i+12] # Assign characters from position i to i + 12
    # Print chunk if it matches phone number pattern
    if isPhoneNumber(chunk):
        print('Phone number found: ' + chunk)
print('Done')
