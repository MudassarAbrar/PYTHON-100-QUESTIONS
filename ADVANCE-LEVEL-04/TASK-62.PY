'''
Question 62
Write a program to read an ASCII string and to convert it to a unicode string encoded by utf-8.

Hints:

Use unicode() function to convert.
'''

def read_ascii(ascii_string:str):
    unicode_string = ascii_string.encode('utf-8').decode('utf-8')
    return unicode_string

# Example usage
ascii_str = "Hello, World!"
unicode_str = read_ascii(ascii_str)

print(f"ASCII String: {ascii_str}")
print(f"Unicode String: {unicode_str}")
