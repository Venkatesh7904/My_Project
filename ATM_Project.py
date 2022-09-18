#User accounts
username=["user1","user2","user3","user4","user5"]
#username&pin
user1=1234
user2=5678
user3=9012
#useraccountbalance
user1_B=50000
user2_B=100000
user3_B=150000
def user1_withdraw():
    amount=int(input("Enter withdraw amount:"))
    balance=user1_B-amount
    print(f"Get you amount:{amount}")
    print(f"Your balance amount is:{balance}")
    if amount>user1_B:
        print("Not Valid")
def user1_Balanace():
    print(f"Your Balance Amount Is:{user1_B}")

def user2_withdraw():
    amount=int(input("Enter withdraw amount:"))
    balance=user2_B-amount
    print(f"Get you amount:{amount}")
    print(f"Your balance amount is:{balance}")
    if amount>user2_B:
        print("Not Valid")
def user2_Balance():
    print(f"Your Balance Amount Is:{user2_B}")

def user3_withdraw():
    print("")
    amount=int(input("Enter withdraw amount:"))
    balance=user3_B-amount
    print(f"Get you amount:{amount}")
    print(f"Your balance amount is:{balance}")
    if amount>user3_B:
        print("Not Valid")
def user3_Balance():
    print(f"Your Balance Amount Is:{user3_B}")
print("***Welcome To SBI Bank ATM***")
user=input("Enter Your Name:").lower().strip()
if user in username:
    pin=int(input("Enter Your Pin:"))
    print("")
    if user=="user1" and pin==1234:
        print("1.Withdraw\n2.Blance Enquiry")
        choose=int(input("Choose Your Option:"))
        if choose==1:
            user1_withdraw()
        elif choose==2:
            user1_B()
    elif user=="user2" and pin==5678:
        print("1.Withdraw\n2.Blance Enquiry")
        choose=int(input("Choose Your Option:"))
        if choose==1:
            user2_withdraw()
        elif choose==2:
            user2_B()
    elif user=="user3" and pin==9012:
        print("1.Withdraw\n2.Blance Enquiry")
        choose=int(input("Choose Your Option:"))
        if choose==1:
            user3_withdraw()
        elif choose==2:
            user3_B()
else:
    print("Please Enter Correct Username and Password")