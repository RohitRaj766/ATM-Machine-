# Create_Account_Function



total_balance=0
def create_account():
    global username
    global password
    global accnumb
    username=str(input("\nEnter your username : "))
    password=str(input("Enter your password : "))
    accnumb=str(input("Enter your account : "))
    confirm_password=str(input("Enter your password again : "))
    if(password==confirm_password):
        print("\nRegistration Successfull")
        x=str(input("\nLogin now  (y/n) : "))
        if(x=="y"):
            login()
        elif(x=="n"):
            menu1()  
        else:
            print("\n Choose the correct option")       
    else:
        print("\nYour Password does not Match")

#Login_Account_Function
    
def login():
    username1=str(input("\nEnter your username : "))
    accnumb1=str(input("Enter your account number : "))
    password1=str(input("Enter your password : "))
    if(username1==username and password1==password and accnumb1==accnumb):
        print("\nLogin successfull")
        menu2()
    else:
        print("\nInvalid user details")
        a=str(input(("\nWould You like to try again (y/n) : ")))
        if(a=="y"):
            login()
        elif(a=="n"):
            exit()
            
# Widthdraw

def withdraw():
    global total_balance
    global withdrawal_balance
    # total_balance=0
    withdrawal_balance=int(input("Enter the amount : "))
    if(total_balance<withdrawal_balance):
        print("Not have enough money!")
        menu2()
    else:    
        total_balance=total_balance-withdrawal_balance
        print("Your new balance is : Rs ",total_balance)
        menu2()
                
# Deposit

def deposit():
    deposit_balance=int(input("Enter your amount : "))
    global total_balance
    total_balance=total_balance+deposit_balance
    print("Your new balance is : Rs ",total_balance)
    menu2()
                
# Account_details

def account_details():
    print("Account Holder Name : ",username)
    print("Account number      : ",accnumb)    
    print("Total Amount        : ",total_balance,"\n")
    menu2()    
    
        
                
            
#After_Creating_Account_Menu
        
def menu1():
    print("\n1. Update account")
    print("2. Login now")
    global x
    x=str(input("\nChoose 1 OR 2 : "))
    if (x=="1"):
       print("\nYou all ready have created your account. Please login!")
       login()
    elif(x=="2"):
        print("Login here")
        login()
    else:
        print("Please select valid option")
     
# Menu_Before_Creating_Account

def menu0():
    print("\nWelcome To Jamshedpur Bank\n")
    print("1. Create your account : ")
    print("2. Already have account : \n")
    x=str(input("Choose 1 OR 2 : "))
    if (x=="1"):
       print("\nRegister with us")
       create_account()
    elif(x=="2"):
       print("\nYou don't have any account. Please create account to login ")
       x=str(input(("\nWould you like to create a account (y/n) : ")))
    if(x=="y"):
       create_account()
    elif(x=="n"):
        exit()
    else:
      print("\nPlease select valid option from below")
      menu0() 

      
# Menu_2
def menu2():
    print("1. Check account details")
    print("2. deposit money")
    print("3. Widthdraw money")
    print("3. Exit Now")
    x=str(input("Choose from above 1 - 2 - 3 - 4 : ")) 
    if(x=="1"):
        account_details()
    elif(x=="2"):
        deposit()
    elif(x=="3"):
        withdraw()
    elif(x=="4"):
          exit()      
    else:
      print("\nPlease select valid option from below")
      menu2() 
    
#Called_Menu0()
    
menu0()    

    
 
