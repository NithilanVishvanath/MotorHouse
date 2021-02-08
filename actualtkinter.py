from tkinter import *
from tkinter.ttk import Combobox


def filterUI():
    root =Tk()
    def close():
        root.destroy()
    def AllGet():
        f1 = nameWidget.get()
        f2 = displacementWidget.get()
        f3 = bhpWidget.get()
        f4 = torqWidget.get()
        f5 = cylWidget.get()
        f6 = tankWidget.get() 
        f7 = mileageWidget.get()
        f8 = brakeWidget.get()
        f9 = weightWidget.get()
        f10 = priceWidget.get()
        Fils = [f1,f2,f3,f4,f5,f6,f7,f8,f9,f10]
        for i in Fils:
            Filters[Fils.index(i)] = i
    kill = Button(root, text ='Done', command = close )
    confirm = Button(root, text ='Confirm', command = AllGet)
    
    #List of Filters, 0/empt/huge values by default
    Filters = ['',0,0,0,None,0,0,'',420,30]
    
    nameWidget = Entry(root, width = 50)#Entry widget for the name
    displacementWidget = Scale(root, from_ =500, to = 1500, orient = HORIZONTAL)#Slider widget for displacement
    bhpWidget = Scale(root, from_ = 20, to = 200, orient = HORIZONTAL)#Slider widget for bhp
    torqWidget = Scale(root, from_ = 50, to = 150, orient = HORIZONTAL)#Slider widget for torque
    cylWidget = Scale(root, from_ = 1, to = 10, orient = HORIZONTAL)#Slider widget for cylinders
    tankWidget = Scale(root, from_ = 7, to = 20, orient = HORIZONTAL)#Slider widget for tank capacity
    mileageWidget = Scale(root, from_ = 15, to = 30, orient = HORIZONTAL)#Slider widget for mileage
    brakeWidget = Combobox(root)#Combobox widget for brake type
    brakeWidget['values'] = ('Disc','Drum')
    weightWidget = Scale(root, from_ = 100, to = 300, orient = HORIZONTAL)#Slider widget for kerb weight
    weightWidget.set(300)
    priceWidget = Scale(root, from_ = 1, to = 20, orient = HORIZONTAL)#Slider widget for price
    priceWidget.set(20)
    
    def FilterGet(Specification, filWidget, rowNo):
        
        # def getter1():#function that gets the filter value and appends it to the Filter list
        #     f1 = filWidget.get()
        #     Filters[rowNo-1] = f1
            
        spek = Label(root, text = Specification + '\t:')#label that tells user what filter
        #filt1 = Entry(root, width = 50)
        
        #conf = Button(root,text = 'Confirm', command = getter1)#confirm button, needs to be axed for something more efficient
        
        spek.grid(column = 0, row = rowNo)#label display
        filWidget.grid(column = 1, row = rowNo)#input widget display
        #conf.grid(column = 2, row = rowNo)#confirm button display
    
    FilterGet("Name", nameWidget, 1)
    FilterGet("Minimum Desired Displacement(in cc)", displacementWidget, 2)
    FilterGet("Minimum Desired Max Power(in bhp)", bhpWidget, 3)
    FilterGet("Minimum Desired Torque(in Nm)", torqWidget, 4)
    FilterGet("Desired Number of Cylinders", cylWidget, 5)
    FilterGet("Minimum Desired Tank Capacity(in L)", tankWidget, 6)
    FilterGet("Minimum Desired Mileage(in kmpL)", mileageWidget, 7)
    FilterGet("Desired Brake Type", brakeWidget, 8)
    FilterGet("Maximum Desired Kerb Weight(in kg)", weightWidget, 9)
    FilterGet("Maximum Desired Price(in Lakh Rupees)", priceWidget, 10)
    kill.grid(column = 2, row = 11)
    confirm.grid(column = 1, row = 11)
    root.mainloop()
    return Filters

#Filters = [f1,f2,f3,f4,f5,f,f7,f8,f9,f10]

'''f1 = ''
def getter1():
    global f1
    f1 = filt.get()
    
spek2 = Label(root, text = 'Minimum\t:')
filt2 = Entry(root, width = 50)
conf2 = Button(root,text = 'Confirm', command = getter1)

spek2.grid(column = 0, row = 2)
filt2.grid(column = 1, row = 2)
conf2.grid(column = 2, row = 2)'''