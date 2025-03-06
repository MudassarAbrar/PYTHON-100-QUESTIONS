'''
Question 59
Assuming that we have some email addresses in the "username@companyname.com" format, please write program to print the company name of a given email address. Both user names and company names are composed of letters only.

Example: If the following email address is given as input to the program:

john@google.com

Then, the output of the program should be:

google

In case of input data being supplied to the question, it should be assumed to be a console input.

Hints:

Use \w to match letters.
'''

import re 

def company_name(email:str):
    match = re.search(r"@([\w\-]+)\.",email)
    #match is used when we want to match something in the start of the string
    #search is used when we want to search something from the in between of the string
    #r"@[\w\-]+"
    #the @ means start searching after the @ sign
    #[] means search everything methoned in it 
    #\w means search upper,lower,digits and \- means search hypens too
    #[]+ plus sign means search more then one 
    #\. means stop before it
    #the parantheses () on [\w\-]+ 
    
    if match:
        print(match.group(1))
        
    else:
        print("No match found")
        
        
company_name("username@companyname.com")