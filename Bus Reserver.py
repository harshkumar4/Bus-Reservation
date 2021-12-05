import pandas as pd

pd.DataFrame()
def menu():

    print()
    print("*******************************************************************")
    print("               BUS RESERVATION SYSTEM Project ")
    print("*******************************************************************")
    print()
    print("1. Know about the Project")
    print("2. Reading file bus")
    print("3. Adding New bus Detail in File")
    print("4. Schedule of ALL buses")
    print("5. Sorting Buses Names ")
    print("6. Fare of b953")
    print("7. Fare of a247 ")
    print("8. Bus Enquiry")
    print("9. Cancel Bus")
    print("10. Change of Arrival Timings ")
    print("11. Search By Starting Bus Stop")
    print("12. Find Total No. of Buses")
    print("13. Update Fare of Bus 953")
    print("14. Ticket Reservation")
    print("15. Specific Column")
    print()
    print()
    print("*******************************************************************")


menu()

def about():
    print("The Project is developed on BUS RESERVATION SYSTEM. It contains 25 Options.In the Project 4 CSV files are used..bus, passenger, b953 and 0247.")


def read_buses():
    print("Reading Details of File bus")
    print()
    print()
    df=pd.read_csv("bus.csv", index_col=0)
    print(df)

def new_buses():
    print('Adding new Bus in File bus')

    df=pd.read_csv("bus.csv", index_col=0)
    print(df)
    n=input("Enter Bus No. : ")
    a=input("Enter Bus Name : ")
    b=input("Enter Start : ")
    c=input("Enter Stop: ")
    d=float(input("Enter Departure: "))
    e=float(input("Enter Arrival: "))
    f=float(input("Enter Duration of Journey: "))
    r=int(input ("Enter Frequency: "))
    df.loc[n]=[a,b,c,d,e,f,r]
    print(df)


def schedule():
    print("Schedule of ALL Buses")
    print()
    df=pd.read_csv("bus.csv", usecols=['busno'])
    print(df)


def sort_buses():
    print('sorting of Buses ')
    print()
    df=pd.read_csv("bus.csv", index_col=0)
    df=df.sort_values('busno')
    print(df)


def b953_fare():
    print('Show Fares of b953 Bus')
    print()
    df=pd.read_csv ("b953.csv", usecols=['start','stop','fare'], index_col=0)
    print(df)


def a247_fare():
    print('Show Fares of a247 Bus')
    print()
    df=pd.read_csv("a247.csv", usecols=['start','stop','fare'], index_col=0)
    print(df)


def enquiry():
    print('Find out Time Table a Bus')
    df=pd.read_csv("bus.csv", index_col=0, usecols=['busname','start','arrival','duration'])
    print(df)


def cancelbus():
    print('Deleting Cancelled Bus Detail')
    df=pd.read_csv("bus.csv", index_col='busname')
    print(df)
    tnum=input("Enter Bus Name :")
    df.drop(tnum,axis=0, inplace=True)

    print("Record of Bus Temporarily deleted")
    print()
    print(df)


def changetiming():
    
    df=pd.read_csv("bus.csv")
    print("Previous Timings of Arrival")
    print()
    print(df)
    print()
    df.loc[df[ 'busname'] == 'Taj Express', ['arrival']] =df [ 'arrival']+ .20
    print()
    print(df)


def searchbybusstop():
    print("search by Last Stop")
    df=pd.read_csv("bus.csv", index_col='busname')
    print(df)
    print()
    df=df.loc[df[ 'stop']== 'Agra Cantt']
    print(df)


def totalbuses():
    print('Find Total Buses ')
    df=pd.read_csv("bus.csv", usecols=['busname','frequency'])
    print(df)
    print()
    Totalbuses=df['frequency'].sum()
    print("Total Buses are : ", Totalbuses)


def updateb953():
    print('To increase fare and save ')
    print("Previous Fares")
    print()
    df=pd.read_csv("b953.csv")
    print(df)
    print()
    print('increase fare by Rs. 50')
    print()
    df=pd.read_csv("b953.csv")
    df['fare']+=50
    print(df)


def ticketreservation():
    print("WE HAVE THE FOLLOWING Buses FOR YOU:-")
    print("Bus b953 To Bhopal FROM New Delhi:-")
    print("For b953-----")
    print()
    print("1. If u want to get down at Indore Pay Rs. 1200")
    print("2. If u want to get down at Lalitpur Pay Rs. 1800")
    print("3. If u want to get down at Nagpur Pay Rs. 2500")
    print()
    print ("Bus a247 To Agra FROM New Delhi:-")
    print()
    print("For a247-----")
    print ("1. If u want to get down at Faridabad Pay Rs. 1000")
    print ("2. If u want to get down at Kosi Pay Rs. 1200")

    busname=input("ENTER YOUR CHOICE of Bus No. PLEASE ->")
    print(busname)
    x=int(input("ENTER No. of YOUR CHOICE of Stop PLEASE-> "))
    n=int(input("HOW MANY TICKETS YOU NEED:"))
    
    if (busname=='b953'):
        if(x==1):
            print ("YOU HAVE Chosen 1st Stop Indore")
            s=1280*n

        elif(x==2):
            print ("YOU HAVE Chosen 2nd Stop Lalitpur")
            s=1800*n

        elif(x==3):
            print ("YOU HAVE Chosen 3rd Stop Nagpur")
            s=2500*n

        elif (x==4):
            print("YOU HAVE Chosen Last Stop Bhopal")
            s=3000*n

        else:
            print("Invalid option")
            print ("PLEASE CHOOSE A Correct Bus No.")

        print ("YOUR TOTAL TICKET PRICE is -",s,"\n")

    elif (busname == 'a247'):
        if(x==1):
            print ("YOU HAVE Chosen 1st Stop Faridabad")
            s=1000*n

        elif(x==2):
            print("YOU HAVE Chosen 2nd Stop Kosi")
            s=1200*n

        elif(x==3):
            print ("YOU HAVE Chosen 3rd Stop Mathura")
            s=1500*n

        elif(x==4):
            print ("YOU HAVE Chosen Last Stop Agro")
            s=1800*n

        else:
            print("Invalid option")
            print ("PLEASE CHOOSE A Correct Bus No.")

        print ("Your TOTAL TICKET PRICE is =",s ,"\n")

    else:
        print("Bus Not Available")


def spec_col():
    print("Show only busname, its Last stop and Duration of Journey")
    df=pd.read_csv("bus.csv", usecols=['busname', 'stop', 'duration'])
    print(df)



opt=int(input("Enter your choice : "))
if opt==1:
    about()

elif opt==2:
    read_buses()

elif opt==3:
    new_buses()

elif opt==4:
    schedule()

elif opt==5:
    sort_buses()

elif opt==6:
    b953_fare()

elif opt==7:
    a247_fare()

elif opt==8:
    enquiry()

elif opt==9:
    cancelbus()

elif opt==10:
    changetiming()

elif opt==11:
    searchbybusstop()

elif opt==12:
    totalbuses()

elif opt==13:
    updateb953()

elif opt==14:
    ticketreservation()

elif opt==15:
    spec_col()

else:
    print('Invalid Option')
    print('\a')