#Ticket Price With AC and Without AC
Chennai=1500
Chennai_AC=2000
Coimbatore=800
Coimbatore_AC=1000
Madurai=500
Madurai_AC=700
Nagercoil=250
Nagercoil_AC=350
Salem=1300
Salem_AC=800
Tuticorin=150
Tuticorin_AC=300
Virudhunagar=500
virudhunagar_AC=700
import mysql.connector
mydb=mysql.connector.connect(
host="localhost",
 user="root",
 password="venkatesh@143",
 database="Ticket_Booking"
)
mycursor=mydb.cursor()
def travel(Name,Phone_No,From_loc,To_loc,Tickets,Price):
    sql="insert into customer_list (Name,Phone_No,From_loc,To_loc,Tickets,Price) values(%s,%s,%s,%s,%s,%s)"
    val=(Name,Phone_No,From_loc,To_loc,Tickets,Price)
    mycursor.execute(sql,val)
    mydb.commit()
def Ticket_Detailes():
    print("\t\t*****Ticket Detailes**********")
    print(f"Name:{Name}")
    print(f"Phone_No:{Phone_No}")
    print(f"From:{From_loc}")
    print(f"To:{To_loc}")
    print(f"Tickets:{Tickets}")
    print(f"Totel Price:{Price}")
    print("Your Tickets Was Booked \n Happy Journey")
    print("***************************************************")
    user=input("Enter **start** To Book Tickets:").lower().strip()
    if user=="start":
        print("***Welcome To Ticket Booking***")
        Name=input("Enter Your Name:")
        Phone_No=int(input("Enter Your Phone_No:"))
        From_loc="Tirunelveli"
        print("TirunelveliTo:\n1.Chennai\n2.Coimbatore\n3.Madurai\n4.Nagercoil\n5.Salem\n6.Tuticorin\n7.Virudhunagar\n")
        To_loc=input("Enter Your Destination:").lower().strip()
        print("")
        print("1.A/c\n2.NON-A/C")
        Type=int(input("Select Your Choice:"))
        if To_loc=="chennai" and Type==1:
            print(f"{From_loc}->Chennai")
            print(f"Ticket Price:{Chennai_AC}")
            Tickets=int(input("Please Enter how many tickets:"))
            Price=Tickets*1500
            Ticket_Detailes()
        elif To_loc=="chennai" and Type==2:
            print(f"{From_loc}->{To_loc}")
            print(f"Ticket Price:{Chennai}")
            Tickets=int(input("Please Enter how many tickets:"))
            Price=Tickets*Chennai
            Ticket_Detailes()
        elif To_loc=="comibatore" and Type==1:
            print(f"{From_loc}->{To_loc}")
            print(f"Ticket Price:{Coimbatore}")
            Tickets=int(input("Please Enter how many tickets:"))
            Price=Tickets*Coimbatore
            Ticket_Detailes()
        elif To_loc=="coimbatore" and Type==2:
            print(f"{From_loc}->{To_loc}")
            print(f"Ticket Price:{Coimbatore_AC}")
            Tickets=int(input("Please Enter how many tickets:"))
            Price=Tickets*Coimbatore_AC
            Ticket_Detailes()
        elif To_loc=="madurai" and Type==1:
            print(f"{From_loc}->{To_loc}")
            print(f"Ticket Price:{Madurai}")
            Tickets=int(input("Please Enter how many tickets:"))
            Price=Tickets*Madurai
            Ticket_Detailes()
        elif To_loc=="madurai" and Type==2:
            print(f"{From_loc}->{To_loc}")
            print(f"Ticket Price:{Madurai_AC}")
            Tickets=int(input("Please Enter how many tickets:"))
            Price=Tickets*Madurai_AC
            Ticket_Detailes()
        elif To_loc=="nagercoil" and Type==1:
            print(f"{From_loc}->{To_loc}")
            print(f"Ticket Price:{Nagercoil}")
            Tickets=int(input("Please Enter how many tickets:"))
            Price=Tickets*Nagercoil
            Ticket_Detailes()
        elif To_loc=="nagercoil" and Type==2:
            print(f"{From_loc}->{To_loc}")
            print(f"Ticket Price:{Nagercoil_AC}")
            Tickets=int(input("Please Enter how many tickets:"))
            Price=Tickets*Nagercoil_AC
            Ticket_Detailes()
        elif To_loc=="salem" and Type==1:
            print(f"{From_loc}->{To_loc}")
            print(f"Ticket Price:{Salem}")
            Tickets=int(input("Please Enter how many tickets:"))
            Price=Tickets*Salem
            Ticket_Detailes()
        elif To_loc=="coibatore" and Type==2:
            print(f"{From_loc}->{To_loc}")
            print(f"Ticket Price:{Salem_AC}")
            Tickets=int(input("Please Enter how many tickets:"))
            Price=Tickets*Salem_AC
            Ticket_Detailes()
        elif To_loc=="tuticorin" and Type==1:
            print(f"{From_loc}->{To_loc}")
            print(f"Ticket Price:{Tuticorin}")
            Tickets=int(input("Please Enter how many tickets:"))
            Price=Tickets*Tuticorin_AC
            Ticket_Detailes()
        elif To_loc=="tuticorin" and Type==2:
            print(f"{From_loc}->{To_loc}")
            print(f"Ticket Price:{Tuticorin_AC}")
            Tickets=int(input("Please Enter how many tickets:"))
            Price=Tickets*Tuticorin_AC
            Ticket_Detailes()
        elif To_loc=="virudhunagar" and Type==1:
            print(f"{From_loc}->{To_loc}")
            print(f"Ticket Price:{Virudhunagar}")
            Tickets=int(input("Please Enter how many tickets you want:"))
            Price=Tickets*Virudhunagar
            Ticket_Detailes()
        elif To_loc=="virudhunagar" and Type==2:
            print(f"{From_loc}->{To_loc}")
            print(f"Ticket Price:{virudhunagar_AC}")
            Tickets=int(input("Enter how many tickets you want:"))
            Price=Tickets*virudhunagar_AC
            Ticket_Detailes()
        else:
            print("Enter Destination Correctly")
    else:
        print("Enter Start Correctly")
    travel(Name,Phone_No,From_loc,To_loc,Tickets,Price)