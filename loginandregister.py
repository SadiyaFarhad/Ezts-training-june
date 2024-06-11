#Created on Tue Jun 11 20:39:08 2024

def loginandreg():
    d={} # use Dictionary 
    print("Welcome to Registration !!")
    u_name=input("Enter ur Username")
    u_pwd=input("Enter Ur Password")
    name=input("Enter ur Name")
    phone_no=input("Enter ur Phone number")
    d[u_name]=u_pwd
    while True:
        print("Welcome to Login")
        l_name=input("enter login username")
        l_pwd=input("enter login user password")
# if user existss or not
        if l_name in d:
             if d[l_name]==l_pwd:
                    print("Login Success")
                    break
             else:
                    print("Enter valid password")
        else:
                print("user not found")
                break
            
# Call the main function to start the program
loginandreg()
