
import pyinputplus as pyip
import csv

def adminCheck():
    correctPassword = 'nithisgodnow'
    wrongPasswordMsg = 'Incorrect password.'
    for i in range(5):#only 5 tries
        password = pyip.inputStr(prompt = 'Enter password:\n')
        if password == correctPassword:
            break
        else:
            print(wrongPasswordMsg)
            continue
    if password != correctPassword:
        print("You have exceeded the maximum number of attempts. The program will end now.")#hits limit, leaves program
        raise Exception("You cannot lie to us.")
    else:
        print("You're in. Welcome, Nithilan.")#right password, function returns True
    return password == correctPassword

def confirm(action = 'do this'):#confirm function
    surity = pyip.inputYesNo(prompt = "Are you sure you wish to "+action+"?(Yes/No)") 
    return surity == 'yes'

def Data_Choice():
    rerunAdmain = True
    while rerunAdmain:
        ch = pyip.inputInt(prompt="Type '1' to add new data, '2' to modify/delete existing data, '3' to check requests, and '4' to exit:\n",min=1,max=4)
        if ch == 1:
            add_data()#addition function
        elif ch == 2:
            modify_data()#modification function
        elif ch == 3:
            request_checker()#request checking function
        else:
            if confirm('exit'):
                print('Exiting...')
                break
            else:
                continue
        #rerunAdmain = False
def create_record():
    bikeValid = False
    while  not bikeValid:
        bikeDet = eval(input("Enter bike details in the form of a list."))
        if len(bikeDet) == 20:
            bikeValid = True
        else:
            DetEnter = pyip.inputYesNo(prompt = "That's not a valid bike. Do you wish to try again?(y/n)\n")
            if DetEnter == 'yes':
                continue
            else:
                break
            
    return bikeDet #returns a list, NOT a nested list

def add_data():
    rerun = True
    while rerun:
        cont = confirm('add data')
        if not cont:
            print("Exiting...")
            break
        bikeRecs = []
        moreRecs = 'yes'
        while moreRecs == 'yes':
            bikeDet = create_record()
            bikeRecs.append(bikeDet)#creates a nested list w/ each sublist being one record
            print(len(bikeRecs))
            moreRecs = pyip.inputYesNo("Do you wish to add more records?")
        fileName = 'bikeproj.csv'
        with open(fileName,'a') as motorhouse:
            bikeRow = csv.writer(motorhouse,delimiter = ',')#writer object, comma delimiter
            bikeRow.writerows(bikeRecs)#appends the new data
            print("Records have been added.")
        rerun = False
#add_data()

def modify_data():
    rerun = True
    while rerun:
        cont = confirm('modify data')
        if not cont:
            print("Exiting...")
            break
        moreRecs = 'yes'
        while moreRecs == 'yes':
            fileName = 'bikeproj.csv'
            found = False
            with open(fileName,'r') as motorhouse:
                bikeRows = csv.reader(motorhouse) #reader object
                changedRecs = list(bikeRows) #changed recs, for now only the original, actually begins to change in a few lines
                #print(changedRecs)
                primKey = pyip.inputStr(prompt = "Enter the name of the bike whose records you wish to modify.\n")#asks for input to match against primary keys
                for row in changedRecs:
                    if row and row[0] == primKey:#searching for the requested data so admin can modify it
                        found = True
                        print(row)
                        rightBike = confirm("modify this bike's records")
                        if not rightBike:
                            again = pyip.inputYesNo(prompt = "Sorry, no other records were found. Do you wish to try again?(Yes/No)\n")
                            if again == 'yes':
                                continue
                            else:
                                break
                                print("Exiting...")
                        else:
                            edit = pyip.inputInt(prompt = "Type '1' to edit the record and '2' to delete the record.\n",max = 2, min = 1)
                            if edit == 1:
                                bikeDet = create_record()
                                for row in changedRecs:
                                    if row and row[0] == primKey:
                                        changedRecs[changedRecs.index(row)] = bikeDet #actually changes the aforementioned changedRecs
                            elif edit == 2:
                                for row in changedRecs:
                                    if row and row[0] == primKey:
                                        changedRecs.remove(row)

                if not found:#no matches w/ primary keys
                    moreRecs = pyip.inputYesNo(prompt = "Sorry, no records were found. Do you wish to try again?(Yes/No)\n")#try again?
                    if moreRecs == 'no':
                        rerun = False
                else:#matched with primary key
                    with (open(fileName, 'w')) as motorhouse:
                        writer = csv.writer(motorhouse,delimiter = ',')#basically truncates the existing data with the new changed data
                        writer.writerows(changedRecs)
                        moreRecs = pyip.inputYesNo(prompt = 'Would you like to modify more records?(Yes/No)\n')#do you want MORE?
                        if moreRecs == 'no':
                            rerun = False
#modify_data()

def request_checker():
    rerun = True
    while rerun:
        cont = confirm('check requests')
        if not cont:
            print("Exiting...")
            break
        else:
            with open('bikeRequests.csv','r') as requestFile:
                requestList = list(csv.reader(requestFile))
                #requestList = list(requests)
                pending = False
                for request in requestList[1:]:
                    if request:
                        pending = True
                        print(request[0])
                        accept = pyip.inputYesNo(prompt = 'Do you wish to attend to this request?\n')
                        if accept == 'yes':
                            dismiss = pyip.inputInt(prompt = "Type '1' to update the records and  '2' to dismiss this request.\n",max = 2, min = 1)
                            if dismiss == 1:
                                add_data()
                                requestList.remove(request)
                                print("Request fulfilled. Data added.")
                            else:
                                requestList.remove(request)
                                print("Request has been dismissed.")
            with open('bikeRequests.csv','w') as requestFile:
                checkedRequests = csv.writer(requestFile, delimiter = ',')
                checkedRequests.writerows(requestList)
            if pending == False:
                print("No pending requests.")
            rerun = False

#request_checker()




