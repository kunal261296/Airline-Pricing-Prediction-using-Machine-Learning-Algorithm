from calendar import Calendar
from tkinter import *
from tkinter import messagebox
import tkcalendar
from datetime import date

if __name__ == "__main__":

    root = Tk()
    root.configure(back='LightBlue')
    root.title("Airline Ticket Pricing")
    root.geometry("600x600")
    heading = Label(root, text="Enter the Details", bg="White")

    source = Label(root, text="Source")
    destination = Label(root, text="Destination")
    Date = Label(root, text="Date")
    airline = Label(root, text="Airline")
    travelclass = Label(root, text="Class")


    heading.grid(row=1, column=6,pady=30)
    source.grid(row=2, column=4,padx=65,pady=10)
    destination.grid(row=4, column=4,pady=10)
    Date.grid(row=6, column=4,pady=10)
    airline.grid(row=8, column=4,pady=10)
    travelclass.grid(row=10, column=4,pady=10)

    sourcelist=["Mumbai","Bangalore","Kathmandu","Delhi","NewYork", "Geneva", "Tokyo","Dubai","Paris",
                                                                         "Ahmedabad", "Singapore", "Bali"]
    destinationlist = ["Mumbai", "Bangalore", "Kathmandu", "Delhi", "NewYork", "Geneva", "Tokyo", "Dubai", "Paris",
                                                                                                      "Ahmedabad",
                  "Singapore", "Bali"]
    airlinelist = ["British","Delta","Jet","Singapore","Virgin","Boeing"]

    citysource=StringVar()
    citydestination = StringVar()
    airlines=StringVar()
    afield=OptionMenu(root,airlines,*airlinelist)
    source_field=OptionMenu(root,citysource,*sourcelist)
    destination_field = OptionMenu(root, citydestination,*destinationlist)
    cal = tkcalendar.DateEntry(root, selectmode="day", year=2019, month=6, day=4)

    classlist=StringVar()
    travelclass_field = OptionMenu(root,classlist,"Economy","Premium")



    source_field.grid(row=2, column=6)
    destination_field.grid(row=4, column=6 )
    cal.grid(row=6,column=6)
    afield.grid(row=8, column=6)
    travelclass_field.grid(row=10, column=6)




    AirlineEconomyPrice=[-1452.9590,-641.9328,-2000.0798,-2021.2584,-1110.3890,253.0085];
    IsInternationalEconomy=1282.5530;
    FlightDurationEconomy=93.9876;
    SeatsEconomy=-0.2511;
    PitchEconomy=7.4696;
    WidthEconomy=20.0074;
    PercentPremiumEconomy=17.9548;

    AirlinePremiumPrice = [-1077.7499,-233.0559,-1984.5662,-2116.2916,-462.1511,320.6584];
    IsInternationalPremium = 1065.0417;
    FlightDurationPremium = 176.2330;
    SeatsPremium = 2.8240;
    PitchPremium = 104.2921;
    WidthPremium = 24.4222;
    PercentPremiumPremium = 7.9231;
    NoOfSeatsEconomy = 202
    NoOfSeatsPremium = 34
    NoOfPitchEconomy = 31
    NoOfPitchPremium = 38
    NoOfWidthEconomy = 18
    NoOfWidthPremium = 19
    NoOfPercentPremiumSeats = 15




    def bclick():
        flag=True;
        if not citysource.get():
            messagebox.showinfo("Error !!!" ,"Please enter all the fields !")
            flag=False;
        elif not citydestination.get():
            messagebox.showinfo("Error !!!" ,"Please enter all the fields !")
            flag = False;
        elif not airlines.get():
            messagebox.showinfo("Error !!!" ,"Please enter all the fields !")
            flag = False;
        elif not classlist.get():
            messagebox.showinfo("Error !!!" ,"Please enter all the fields !")
            flag = False;
        elif cal.get_date()<date.today():
            messagebox.showinfo("Error !!!" ,"Invalid Date")
            flag=False;




        domestic = ["Delhi", "Ahmedabad", "Mumbai", "Bangalore"]

        international = ["Kathmandu", "Singapore", "Bali", "Dubai", "Tokyo", "Paris", "Geneva", "NewYork"]
        flag1=True
        if (citysource.get() == citydestination.get() and flag==True):
            messagebox.showinfo("Error!!!","Source and Destination should be different !")
            flag1=False;



        if(flag==True and flag1==True):
            if (citysource.get() in domestic and citydestination.get() in domestic):
                domestictravel = True;
            else:
                domestictravel = False;

            if (classlist.get() == "Economy"):
                if (domestictravel == True):
                    duration = abs((domestic.index(citydestination.get()) - domestic.index(citysource.get()))) ;
                    price = int(AirlineEconomyPrice[airlinelist.index(airlines.get())] + (FlightDurationEconomy * duration) + (SeatsEconomy * NoOfSeatsEconomy) + (PitchEconomy * NoOfPitchEconomy) + (WidthEconomy * NoOfWidthEconomy) + (PercentPremiumEconomy * NoOfPercentPremiumSeats))
                else:
                    if (citydestination.get() in international and citysource.get() in domestic):
                        duration = abs((international.index(citydestination.get()) + 3 - domestic.index(citysource.get()))) * 3;
                    elif(citydestination.get() in domestic and citysource.get() in international):
                        duration = abs((domestic.index(citydestination.get()) - international.index(citysource.get())) + 3) * 3;
                    else:
                        duration = abs((international.index(citydestination.get()) - international.index(citysource.get())) + 3) * 3;
                    price = int(AirlineEconomyPrice[airlinelist.index(airlines.get())] + IsInternationalEconomy + (FlightDurationEconomy * duration) + (SeatsEconomy * NoOfSeatsEconomy) + (PitchEconomy * NoOfPitchEconomy) + (WidthEconomy * NoOfWidthEconomy) + (PercentPremiumEconomy * NoOfPercentPremiumSeats))
            else:
                if (domestictravel == True):
                    duration = abs((domestic.index(citydestination.get()) - domestic.index(citysource.get()))) ;
                    price = int(AirlineEconomyPrice[airlinelist.index(airlines.get())] + (FlightDurationPremium * duration) + (SeatsPremium * NoOfSeatsPremium) + (PitchPremium * NoOfPitchPremium) + (WidthPremium * NoOfWidthPremium) + (PercentPremiumPremium * NoOfPercentPremiumSeats))
                else:
                    if (citydestination.get() in international and citysource.get() in domestic):
                        duration = abs((international.index(citydestination.get()) + 3 - domestic.index(citysource.get()))) * 3;
                    elif (citydestination.get() in domestic and citysource.get() in international):
                        duration = abs((domestic.index(citydestination.get()) - international.index(citysource.get())) + 3) * 3;
                    else:
                        duration = abs((international.index(citydestination.get()) - international.index(citysource.get())) + 3) * 3;
                    price = int(AirlineEconomyPrice[airlinelist.index(airlines.get())] + IsInternationalPremium + (FlightDurationPremium * duration) + (SeatsPremium * NoOfSeatsPremium) + (PitchPremium * NoOfPitchPremium) + (WidthPremium * NoOfWidthPremium) + (PercentPremiumPremium * NoOfPercentPremiumSeats))
            if(flag1==True):
             messagebox.showinfo("Predicted Price", str(abs(price))+" $")




    btn = Button(root, text="Show Price", fg="Black",
                    bg="White", command= bclick)
    btn.grid(row=12, column=6,pady=35)



    root.mainloop()
