import pyinputplus as pyip
import csv
from actualtkinter import filterUI
from generalVariables import specs
from time import sleep

def User_Intro():
    print("Greetings traveller!! Welcome to The Motorhouse (version 1.0.1), a database of motorcycles where you can easily find the bike of your dreams!")
    print("You will be directed to the search filter screen shortly...")
    sleep(2)
    while True:
        bikesFound = bikeSearch()
        if bikesFound:
            again = pyip.inputYesNo(prompt = "Do you want to search again?")
            if again == 'no':
                break
        else:
            userChoice = pyip.inputInt(prompt = "No bikes found. Press '1' to try again, '2' to put in a request to the admins, or '3' to exit.",min = 1, max = 3)
            if userChoice == 1:
                continue
            elif userChoice == 2:
                #print("That feature isn't ready yet.")
                #break
                requester()
                again = pyip.inputYesNo(prompt = "Do you want to search again?(Yes/No)")
                if again == 'no':
                    break
            else:
                break

def bikeDisplay(bike):
    for spec in specs:
        print(spec+' : '+bike[specs.index(spec)])
    print('---------------------')

def bikeSearch():
    rerun = True
    while rerun:
        found = False
        fL = list(filterUI())
        with open('bikeproj.csv','r') as motorhouse:
            rows = list(csv.reader(motorhouse))
            bikerows = rows[1:]
            for bike in bikerows:
                #print((bike[0:4]+[bike[7]]+bike[9:11]+[bike[16],bike[19]]))
                #print(fL)
                if bike and len(bike[0])>5 and fL[0] in bike[0] and float(bike[1][:-2])>fL[1] and float(bike[2][:-3])>fL[2] and float(bike[3][:-2])>fL[3]:
                    #print('Beans1')
                    if float(bike[7][:-1]) > fL[5] and float(bike[9][:-4])>fL[6] and fL[7] in bike[10]:
                        #print('Beans2')
                        if float(bike[16][:-2]) < fL[8] and float(bike[19][:-1]) < fL[9]:
                           bikeDisplay(bike)
                           found = True
                            #print('beans3')
        rerun = False
        return found
#bikeSearch()

def requester():
    with open('bikeRequests.csv','a') as requests:
        request = input("Enter name of the bike.")
        req = []
        req.append([request])
        requestWriter = csv.writer(requests, delimiter = ',')
        requestWriter.writerow(req)
        