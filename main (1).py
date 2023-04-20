import string

fn, ln, cn, sn = input("Enter your first name,last name,city,state(in the same order): ").split(",")
print(fn, ln, cn, sn)


#============================================mobile_no=====================================================
def mobile_no():
    mn = input("enter your mobile no.:")
    if mn.isnumeric() and len(mn) == 10:
        print("valid mobile")
    else:
        print("invalid")
        mobile_no()

#============================================aadharcard=====================================================
def aadhar_card():
    aadhar = input("enter your aadhar no. :")

    if aadhar[0] not in ['0', '1'] and ''.join(c for (i, c) in enumerate(aadhar, 1) if i % 5 == 0) == '  ' and aadhar.replace(' ', '').isnumeric() and len(aadhar) <= 14:  # aadhar.replace(' ','').isnumeric() and aadhar[4].isspace() and aadhar[9].isspace()
        print("valid aadhar card number")
        return aadhar
    else:
        print("invalid aadhar number")
        return aadhar_card()

#===========================================pancard========================================================
def pancard():
    invalid_char = set(string.punctuation)
    pan = input("enter your pancard number :")
    if " " not in pan and (not any(char in invalid_char for char in pan)) and len(pan) == 10 and pan[:2] == fn[:2] and pan[2:4] == ln[:2] and pan[4:8].isnumeric() and pan[8] == cn[0] and pan[9] == sn[0]:
        print("valid pancard number ")
        return pan
    else:
        print("invalid pancard number ")
        return pancard()

#===============================================================

#option to choose from
print("       to validate pancard enter: 1")
print("       to validate aadharcard enter: 2")

#taking input from user
x = int(input("enter:"))


if x == 1:
    print("pancard validation")
    pancard()
elif x == 2:
    print("aadhar validation")
    aadhar_card()
else:
    print("invalid input")