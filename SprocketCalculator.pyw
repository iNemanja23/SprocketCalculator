import tkinter as tk
from tkinter import *
from TkToolTip import ToolTip

window = tk.Tk()
window.title("Cost calculator")
window.geometry("550x475")

Label(window, text='CANNON').grid(row=0)

caliber = Label(window, text='Caliber')
caliber.grid(row=1)
ToolTip(caliber, text="The caliber of the gun in millimeters", relief='raised')

propLen = Label(window, text='Propellant length')
propLen.grid(row=2)
ToolTip(propLen, text="The propellant length of the gun's ammo in millimeters", relief='raised')

barLen = Label(window, text='Barrel length')
barLen.grid(row=3)
ToolTip(barLen, text="The total barrel length of the gun in millimeters", relief='raised')

Label(window, text='ARMOUR').grid(row=5)

weight = Label(window, text='Total weight')
weight.grid(row=6)
ToolTip(weight, text="The weight of the tank, in tonnes (floating point)", relief='raised')

weightPercentage = Label(window, text='Armour weight %')
weightPercentage.grid(row=7)
ToolTip(weightPercentage, text="The percentage of the total weight of the tank that the armour makes up (floating point)", relief='raised')

Label(window, text='ENGINE').grid(row=9)

cylCount = Label(window, text='Cylinder count')
cylCount.grid(row=10)
ToolTip(cylCount, text="The number of cylinders of the engine", relief='raised')

disp = Label(window, text='Displacement')
disp.grid(row=11)
ToolTip(disp, text="The displacement of a single cylinder in liters (floating point)", relief='raised')

Label(window, text='TRANSMISSION').grid(row=13)

gears = Label(window, text='Gear count')
gears.grid(row=14)
ToolTip(gears, text="The total number of gears, backwards and reverse", relief='raised')

gearType = Label(window, text='Type')
gearType.grid(row=15)
ToolTip(gearType, text="The type of the transmission", relief='raised')

TrT = IntVar()

Label(window, text='SUSPENSION').grid(row=0, column=4)

susCount = Label(window, text='Suspension count')
susCount.grid(row=1, column=4)
ToolTip(susCount, text="For torsion bar, the number of roadwheels\nFor HVSS, the number of bogies", relief='raised')

axleCount = Label(window, text='Axle count')
axleCount.grid(row=2, column=4)
ToolTip(axleCount, text="The number of axles for the roadwheels/bogies and rollers", relief='raised')

rollCount = Label(window, text='Roller count')
rollCount.grid(row=3, column=4)
ToolTip(rollCount, text="The number of return rollers", relief='raised')

wheelDia = Label(window, text='Wheel diameter')
wheelDia.grid(row=4, column=4)
ToolTip(wheelDia, text="The diameter of roadwheels in meters (floating point)", relief='raised')

susType = Label(window, text='Suspension type')
susType.grid(row=5, column=4)
ToolTip(susType, text="The type of the suspension", relief='raised')

SusT = IntVar()

Label(window, text='TRACKS').grid(row=7, column=4)

trackW = Label(window, text='Width')
trackW.grid(row=8, column=4)
ToolTip(trackW, text="The width of the tracks in millimeters", relief='raised')

trackH = Label(window, text='Thickness')
trackH.grid(row=9, column=4)
ToolTip(trackH, text="The thickness of the tracks in millimeters", relief='raised')

trackL = Label(window, text='Length')
trackL.grid(row=10, column=4)
ToolTip(trackL, text="The length of the tracks in millimeters\nTo view this, unsync the tracks from the chassis", relief='raised')

Label(window, text='ADDITIONAL ARMOUR').grid(row=12, column=4)

segCount = Label(window, text='Segment Count')
segCount.grid(row=13, column=4)
ToolTip(segCount, text="The total number of segments of reserve tracks", relief='raised')

wheelCount = Label(window, text='Wheel count')
wheelCount.grid(row=14, column=4)
ToolTip(wheelCount, text="The number of reserve roadwheels", relief='raised')

Label(window, text='FUEL').grid(row=16, column=4)

fuel = Label(window, text='Fuel Capacity')
fuel.grid(row=17, column=4)
ToolTip(fuel, text="The total fuel tank capacity in liters", relief='raised')

Label(window, text='AMMO').grid(row=17)

ammo = Label(window, text='Ammo count')
ammo.grid(row=18)
ToolTip(ammo, text="The total number of shells", relief='raised')

button = tk.Button(window, text='Calculate', width=12, height=2)

button.grid(row=19, column=4)


for i in range(0,20):
  Label(window,text='               ').grid(row=i,column=3)

def handle_click(event):
    cannon_cost = int((int(Ce1.get()) / 10) ** 1.5 * (int(Ce2.get()) + 300) / 300 * (int(Ce3.get()) + 2000) / 1000 * 12)

    armour_cost = int(float(ARe1.get()) * float(ARe2.get()) * 2.5)

    engine_cost = int((int(Ee1.get()) ** 2) * float(Ee2.get()) * 5)

    transmission_cost = int(TMe1.get()) * 50
    if TrT.get() == 2:
        transmission_cost *= 1.5
        transmission_cost = int(transmission_cost)
    if SusT.get() == 1:
        suspension_cost = int((int(Se1.get()) * 5) + (int(Se1.get()) * int(Se2.get()) * float(Se4.get()) * 20 / 0.5) + (int(Se3.get()) * 10)) * 2
    else:
        suspension_cost = int((int(Se1.get()) * 50) + (int(Se2.get()) * 40 * float(Se4.get()) / 0.5) + (int(Se3.get()) * 10)) * 2

    tracks_cost = int((int(Te1.get()) / 300 * int(Te2.get()) / 50 * int(Te3.get()) / 5000) ** 2) * 200

    additional_armour_cost = int((int(AAe1.get()) * ((int(Te2.get()) / 50) ** 2) * 15) + int(AAe2.get()) * 50)

    fuel_cost = int(float(Fe1.get()) * 2)

    ammo_cost = int(AMe1.get()) * ((int(Ce1.get())/10) ** 2) * int(Ce2.get()) / 300 / 10

    result = int(cannon_cost + armour_cost + engine_cost + transmission_cost + suspension_cost + additional_armour_cost + fuel_cost + tracks_cost + ammo_cost)

    Re1.delete(0, 'end')
    Re1.insert(END, str(result))

button.bind("<Button-1>", handle_click)

Ce1 = Entry(window)
Ce2 = Entry(window)
Ce3 = Entry(window)
ARe1 = Entry(window)
ARe2 = Entry(window)
Ee1 = Entry(window)
Ee2 = Entry(window)
TMe1 = Entry(window)
Se1 = Entry(window)
Se2 = Entry(window)
Se3 = Entry(window)
Se4 = Entry(window)
Te1 = Entry(window)
Te2 = Entry(window)
Te3 = Entry(window)
AAe1 = Entry(window)
AAe2 = Entry(window)
Fe1 = Entry(window)
AMe1 = Entry(window)
Re1 = Entry(window)

Ce1.insert(0, '0')
Ce2.insert(0, '0')
Ce3.insert(0, '0')
ARe1.insert(0, '0')
ARe2.insert(0, '0')
Ee1.insert(0, '0')
Ee2.insert(0, '0')
TMe1.insert(0, '0')
Se1.insert(0, '0')
Se2.insert(0, '0')
Se3.insert(0, '0')
Se4.insert(0, '0')
Te1.insert(0, '0')
Te2.insert(0, '0')
Te3.insert(0, '0')
AAe1.insert(0, '0')
AAe2.insert(0, '0')
Fe1.insert(0, '0')
AMe1.insert(0, '0')
Re1.insert(0, '0')

Ce1.grid(row=1, column=1)
Ce2.grid(row=2, column=1)
Ce3.grid(row=3, column=1)
ARe1.grid(row=6, column=1)
ARe2.grid(row=7, column=1)
Ee1.grid(row=10, column=1)
Ee2.grid(row=11, column=1)
TMe1.grid(row=14, column=1)
Se1.grid(row=1, column=5)
Se2.grid(row=2, column=5)
Se3.grid(row=3, column=5)
Se4.grid(row=4, column=5)
Te1.grid(row=8, column=5)
Te2.grid(row=9, column=5)
Te3.grid(row=10, column=5)
AAe1.grid(row=13, column=5)
AAe2.grid(row=14, column=5)
Fe1.grid(row=17, column=5)
AMe1.grid(row=18, column=1)
Re1.grid(row=19, column=5)

Radiobutton(window, text='Clutch', variable=TrT, value=1).grid(row=15, column=1)
Radiobutton(window, text='Twin    ', variable=TrT, value=2).grid(row=16, column=1)
Radiobutton(window, text='Torsion bar', variable=SusT, value=1).grid(row=5, column=5)
Radiobutton(window, text='HVSS          ', variable=SusT, value=2).grid(row=6, column=5)




tk.mainloop()