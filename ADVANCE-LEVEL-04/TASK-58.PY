'''
Question 58
Assuming that we have some email addresses in the "username@companyname.com" format, please write program to print the user name of a given email address. Both user names and company names are composed of letters only.

Example: If the following email address is given as input to the program:

john@google.com

Then, the output of the program should be:

john

In case of input data being supplied to the question, it should be assumed to be a console input.

Hints:

Use \w to match letters.
'''
import re



def email_func(user_email:str):
    match = re.match(r"^[^@]+",user_email)
    #the r shows its a raw string meaning every literal literaly means itself or not any other thing means \n mean \ and n not new line
    
    if match:
        print(match.group())
        #the match fucn returns an object of match and the group fucntion collects the desired data from it
        
    else:
        print("No match found")
        
        
        
        
email_func("john@google.com")