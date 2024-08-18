# Write a class train which has methods to book a ticket , get status(nof seats) 
# and get fare information of train running under Indian railways

class Train:
    def __init__(self,name,seatNum,fare):
        self.name=name
        self.seatNum=seatNum
        self.fare=fare
        self.bookedSeats=set()  #Created an empty set to keep track of booked seats

    def bookTicket(self):
        if(len(self.seatNum)>0):
            seat=self.seatNum.pop()
            self.bookedSeats.add(seat)
            print(f"Your ticket has been booked.Your seat number is: {seat}")
        else:
            print("Sorry,all tickets have been booked,kindly try in Tatkal")

    def getStatus(self):
        print(f"The name of the train is {self.name}")
        print(f"Number of seats left: {len(self.seatNum)}")

    def getFareInfo(self):
        print(f"The price of a ticket is: Rs {self.fare}")

    def cancelTicket(self):
        cancel_num=int(input("Enter your seat number: "))
        if cancel_num in self.bookedSeats:
            self.bookedSeats.remove(cancel_num)
            self.seatNum.add(cancel_num)
            print(f"Your ticket for seat number {cancel_num} has been cancelled. Refund amount will be credited soon.")

        else:
            print("Invalid seat number or the seat was not booked")
        

intercity=Train("Intercity Transport: 15674",set(range(1,51)),50)
intercity.getStatus()
intercity.getFareInfo()
intercity.bookTicket()
intercity.bookTicket()
intercity.bookTicket()
intercity.bookTicket()
intercity.cancelTicket()
intercity.getStatus()
intercity.bookTicket()
intercity.bookTicket()



