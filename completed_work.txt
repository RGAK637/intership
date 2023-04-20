# validation of pan , mobile and aadhar number

import re
import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", password="1230", database="cv")
mycurser = mydb.cursor()



fn, ln, cn, sn = input("Enter your first name,last name,city,state(in the same order): ").split(",")
print(fn, ln, cn, sn)

# sql = "insert into customer(first_name,last_name,city,state)values('{}','{}','{}','{}')".format(fn,ln,cn,sn)
# mycurser.execute(sql)
# mydb.commit()

# fn = input("enter your first name :")
# ln = input("enter your last name :")
# cn = input("enter your city :")
# sn = input("enter your state :")


#=======================================mobile validation===============================================
def mobile():
    num = input("enter your mobile number:")
    # sql = "insert into customer(mobile_no)values('{}')".format(num)
    # mycurser.execute(sql)
    # mydb.commit()

    pattern = re.compile("(0|91)?[-\s]?[6-9]\d{9}")                   # \d  - (0-9)only
    if pattern.match(num) and len(num) <= 13:            #  ?  -  option
        print("vaild")
    else:
        print("invalid")
        mobile()

    return num
# ======================================aadhar validation===============================================
def aadhar_card():
    aadhar = input("enter your aadhar no. :")
    # sql = "insert into customer(aadhar_no)values('{}')".format(aadhar)
    # mycurser.execute(sql)
    # mydb.commit()

    pattern = re.compile(r"[2-9]\d{3}[-\s]\d{4}[-\s]\d{4}[-\s]\d{4}")

    if pattern.match(aadhar) and len(aadhar) <= 19:
        print("valid aadhar card number")
        return aadhar
        # sql = "INSERT INTO customer(validate)VALUES('invalid')"
        # mycurser.execute("INSERT INTO customer(validate)VALUES('valid')")

    else:
        print("invalid aadhar number")
        # sql = "INSERT INTO customer(validate)VALUES('invalid')"
        # mycurser.execute("INSERT INTO customer(validate)VALUES('invalid')")
        return aadhar_card()


#==========================================pancard vaildation=============================================
def pancard():
    pan = input("enter your pancard number :")
    # sql = "insert into customer(pancard_no)values('{}')".format(pan)
    # mycurser.execute(sql)
    # mydb.commit()

    pattern = re.compile("\w{4}\d{4}\w{2}", re.I)
    if pattern.match(pan) and len(pan) == 10 and pan[:2] == fn[:2] and pan[2:4] == ln[:2] and pan[8] == cn[0] and pan[9] == sn[0]:
        print("valid pancard number ")
        return pan
        # sql = "INSERT INTO customer(validate)VALUES('invalid')"
        # mycurser.execute("INSERT INTO customer(validate)VALUES('valid')")
    else:
        print("invalid pancard number ")
        # sql = "INSERT INTO customer(validate)VALUES('invalid')"
        # mycurser.execute("INSERT INTO customer(validate)VALUES('invalid')")
        return pancard()


#=========================================================================================================

mo = mobile()

# mn = input("enter your mobile number :")
# if mobile(mn) and len(mn) == 10:
#     print("valid mobile number")
# else:
#     print("invalid mobile number")
#     print("exiting...")
#     sys.exit()

#option to choose from
print("       to validate pancard enter: 1")
print("       to validate aadharcard enter: 2")

#taking input from user
x = int(input("enter:"))

#condition
if x == 1:
    print("pancard validation")
    pa = pancard()
    sql = "insert into customer(first_name, last_name, city, state, mobile_no, pancard_no, validate)values('{}','{}','{}','{}','{}','{}','valid')".format(fn, ln, cn, sn, mo, pa)
    mycurser.execute(sql)
    mydb.commit()
elif x == 2:
    print("aadhar validation")
    ad = aadhar_card()
    sql = "insert into customer(first_name, last_name, city, state, mobile_no, aadhar_no, validate)values('{}','{}','{}','{}','{}','{}','valid')".format(fn, ln, cn, sn, mo, ad)
    mycurser.execute(sql)
    mydb.commit()
else:
    print("invalid input")


