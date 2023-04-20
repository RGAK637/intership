# intership
Exercise no 1:
Mobile number,  Pan number and Aadhar number validation with and without using Regular expression.

Step 1 : Get  First name, Last name, State, District , and mobile number as input.
Step 2:  Validate mobile number ( should be 10 digit, alphabets or other special characters , and white spaces in between are not allowed)
Step 2 : To get Pan number or aadhar number , give it as a choice as 1. Pan number, 2. Aadhar.
Step 3 : If the choice is '1'  Pan number validation
                   a) Number of digits = 10, should not contain whitespace or special characters.
                   b) first 2 digit is from first name's first 2 letter and should be an alphabet
                   c) 3rd and 4th digits is from last name's first 2 letter.and should be  an alphabet
                   d) 5th to 8th should be digit(non alphabets or special characters/spaces) .
                   e) 9th digit is from District's first letter and  should be an alphabet
                   f) The 10th digit is from State's first letter and should be an alphabet.
 
step 4: If the choice is '2'. do Aadhar validation.
                   a) It should have 12 digits.
                  b) It should not start with 0 and 1.
                  c) It should not contain any alphabet and special characters.
                  d) It should have white space after every 4 digits.
Step 4 : Check the above conditions if true display its valid else get input again and do revalidation (recursive).

- Do it with RegEx (Regular expressions) and a program without regular expressions.(2 programs)  Go through predefined functions and RegEx in python , and try on your own.
- If you know any Backend DB like postgres , oracle or any SQL lang, connect with python and  try to save the inputs and outputs after validation in the backend. 
- Saving in the backend is optional and it's for your own practice.
- Complete the above task within 2 or 3 days and send me the .py files. 
