
import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="venkatesh@143",
    database="HotelManagement"
)
mycursor=mydb.cursor()
#mycursor.execute("create table Add_customer(Name varchar(30),Age int,Gender varchar(10),Address varchar(50),ID_Proof_Name varchar(50),ID_Proof_NO varchar(50),Check_IN varchar(50),Check_OUT varchar(60),Room_NO int)")
def Add_customer(Name,Age,Gender,ID_Proof_Name,ID_Proof_No,Address,Check_IN,Check_OUT,Room_NO):
    sql="insert into Add_customer(Name,Age,Gender,ID_Proof_Name,ID_Proof_No,Address,Check_IN,Check_OUT,Room_NO)values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    val=(Name,Age,Gender,ID_Proof_Name,ID_Proof_No,Address,Check_IN,Check_OUT,Room_NO)
    mycursor.execute(sql,val)
    mydb.commit()
def Customer_list():
    mycursor.execute("select*from Add_customer")
    result=mycursor.fetchall()
    for i in result:
        print(i)
def roomrent():
    print ("We have the following rooms for you:-")
    print ("1.  type A---->rs 6000 PN\-")
    print ("2.  type B---->rs 5000 PN\-")
    print ("3.  type C---->rs 4000 PN\-")
    print ("4.  type D---->rs 3000 PN\-")
    x=int(input("Enter Your Choice Please->"))
    n=int(input("For How Many Nights Did You Stay:"))
    if(x==1):
        print ("you have opted room type A")
        s=6000*n
    elif (x==2):
        print ("you have opted room type B")
        s=5000*n
    elif (x==3):
        print ("you have opted room type C")
        s=4000*n
    elif (x==4):
        print ("you have opted room type D")
        s=3000*n
    else:
        print("please choose a room")
    print(f"your room rent is ={s}\n")
def laundrybill():
        print ("******LAUNDRY MENU*******")
        print ("1.Shorts----->Rs3\n","2.Trousers----->Rs4\n","3.Shirt--->Rs5\n","4.Jeans---->Rs6\n","5.Girlsuit--->Rs8\n","6.Exit\n")
        while (1):
            e=int(input("Enter your choice:"))
            if (e==1):
                f=int(input("Enter the quantity:"))
                w=f*3
            elif (e==2):
                f=int(input("Enter the quantity:"))
                w=f*4
            elif (e==3):
                f=int(input("Enter the quantity:"))
                w=f*5
            elif (e==4):
                f=int(input("Enter the quantity:"))
                w=f*6
            elif (e==5):
                f=int(input("Enter the quantity:"))
                w=f*7
            elif (e==6):
                break;
            else:
                print ("Invalid option")
        print ("Total Laundary Cost=Rs",w,"\n")
def restaurentbill():
    print("*****RESTAURANT MENU*****")
    print("1.water----->Rs20","2.tea----->Rs10","3.breakfast combo--->Rs90","4.lunch---->Rs110","5.dinner--->Rs150","6.Exit")
    while (1):
        c=int(input("Enter your choice:"))
        if (c==1):
            d=int(input("Enter the quantity:"))
            r1=d*20
        elif (c==2):
            d=int(input("Enter the quantity:"))
            r1=d*10
        elif (c==3):
            d=int(input("Enter the quantity:"))
            r1=d*90
        elif (c==4):
            d=int(input("Enter the quantity:"))
            r1=d*110
        elif (c==5):
            d=int(input("Enter the quantity:"))
            r1=d*150
        elif (c==6):
            break;
        else:
            print("Invalid option")
    print ("Total food Cost=Rs",r1,"\n")
def Totel():
        print ("******HOTEL BILL******")
        s=input(f"Please Enter Room Rent:")
        w=input(f"Please Restaurant Bill:")
        u=input(f"Please Lanundry Bill:")
        totel=s+w+u
        print ("Your sub total bill is:",totel)
def main():
    while (1):
        print("1.Enter Customer Data")
        print("2.Calculate rommrent")
        print("3.Calculate restaurant bill")
        print("4.Calculate laundry bill")
        print("5.Show total cost")
        print("6.EXIT")
        b=int(input("\nEnter your choice:"))
        if (b==1):
            Name=(input("Enter Customer Name:"))
            Age=(input("Enter Cutsomer Age:"))
            Gender=(input("Enter Customer Gender:(Male/Female)"))
            ID_Proof_Name=(input("Please Enter Customer IDProofName:(1.AadhaarCard,2.PanCard,3.DrivingLincese,4.VoterID)"))
            ID_Proof_No=(input("Enter Customer Id_Number:"))
            Address=(input("Enter YouProof_Namr Cutomer Address:"))
            Check_IN=str(input("Please Room CheckIN Date:"))
            Check_OUT=str(input("Please Room CheckOUT Date:"))
            Room_NO=int(input("Please Enter Customer Room NO:"))
            print(f"Customer Name:{Name}\nAge:{Age}\nGender:{Gender}\nID_Proof_Name:{ID_Proof_Name}\nID_Proof_No:{ID_Proof_No}\n Address:{ Address}\nCheck_IN:{Check_IN},Check_OUT:{Check_OUT},Room_NO:{Room_NO}")
            Add_customer(Name,Age,Gender,ID_Proof_Name,ID_Proof_No,Address,Check_IN,Check_OUT,Room_NO)
        if (b==2):
            roomrent()
        if (b==3):
            restaurentbill()
        if (b==4):
            laundrybill()
        if (b==5):
            Totel()
        if (b==6):
            quit()
        
main()


