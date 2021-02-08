# import pyinputplus as pyip
# import csv
# def adminCheck():
#     correctPassword = 'nithisgodnow'
#     wrongPasswordMsg = 'Incorrect password.'
#     for i in range(5):#only 5 tries
#         password = pyip.inputStr(prompt = 'Enter password:\n')
#         if password == correctPassword:
#             break
#         else:
#             print(wrongPasswordMsg)
#             continue
#     if password != correctPassword:
#         print("You have exceeded the maximum number of attempts. The program will end now.")#hits limit, leaves program
#         pass
#     else:
#         print("You're in.")#right password, function returns True
#     return password == correctPassword
# def Data_Choice():
#     rerun = True
#     while rerun:
#         ch = pyip.inputInt(prompt="Type '1' to add new data, '2' to modify/delete existing data, and '3' to exit:\n",min=1,max=3)
#         if ch == 1:
#             add_data()#addition function
#         elif ch == 2:
#             modify_data()#modification function
#         else:
#             if confirm('exit'):
#                 print('Exiting...')
#                 break
#             else:
#                 continue
#         rerun = False
# def create_record():
#         bikeDet = []#[Brand,Name,Type,Price,CC,NoOfCylinders,DiscSize,TireSize]
#         bikeBrand = pyip.inputStr(prompt = "Please enter the brand name:\n")
#         bikeName = pyip.inputStr(prompt = "Please enter the name of the model.\n")
#         bikeType = pyip.inputStr(prompt = "Please enter the type of bike.\n")
#         bikePrice = pyip.inputInt(prompt = "Please enter the price of the bike in rupees.\n")
#         bikeCC = pyip.inputInt(prompt = "Please enter the CC of the bike.\n")
#         bikeCyl = pyip.inputInt(prompt = "Please enter the number of cylinders of the bike.\n")
#         bikeDet = [bikeBrand,bikeName,bikeType,bikePrice,bikeCC,bikeCyl]#creates a list with all the values
#         return bikeDet#returns a list, NOT a nested list
# def add_data():
#     rerun = True
#     while rerun:
#         cont = confirm('add data')
#         if not cont:
#             print("Exiting...")
#             break
#         bikeRecs = []
#         moreRecs = 'yes'
#         while moreRecs == 'yes':
#             bikeDet = create_record()
#             bikeRecs.append(bikeDet)#creates a nested list w/ each sublist being one record
#             moreRecs = pyip.inputYesNo("Do you wish to add more records?\n")
#         fileName = 'motorhouse.csv'
#         with open(fileName,'a') as motorhouse:
#             bikeRow = csv.writer(motorhouse,delimiter = ',')#writer object, comma delimiter
#             bikeRow.writerows(bikeRecs)#appends the new data
#             print("Records have been added.")
#         rerun = False
# add_data()
# def modify_data():
#     rerun = True 
#     while rerun:
#         cont = confirm('modify data')
#         if not cont:
#             print("Exiting...")
#             break
#         moreRecs = 'yes'
#         while moreRecs == 'yes':
#             fileName = 'motorhouse.csv'
#             found = False
#             with open(fileName,'r') as motorhouse:
#                 bikeRows = csv.reader(motorhouse) #reader object
#                 changedRecs = list(bikeRows) #changed recs, for now only the original, actually begins to change in a few lines
#                 primKey = pyip.inputStr(prompt = "Enter the name of the bike whose records you wish to modify.\n")#asks for input to match against primary keys
#                 for row in changedRecs:
#                     if row and row[1] == primKey:#searching for the requested data so admin can modify it
#                         found = True
#                         print(row)
#                         rightBike = confirm("modify this bike's records")
#                         if not confirm:
#                             again = pyip.inputYesNo(prompt = "Sorry, no other records were found. Do you wish to try again?(Yes/No)\n")
#                             if again == 'yes':
#                                 continue
#                             else:
#                                 break
#                                 print("Exiting...")
#                         else:
#                             edit = pyip.inputInt(prompt = "Type '1' to edit the record and '2' to delete the record.\n",max = 2, min = 1)
#                             if edit == 1:
#                                 bikeDet = create_record()
#                                 for row in changedRecs:
#                                     if row and row[1] == primKey:
#                                         changedRecs[changedRecs.index(row)] = bikeDet #actually changes the aforementioned changedRecs
#                             else:
#                                 for row in changedRecs:
#                                     if row and row[1] == primKey:
#                                         changedRecs.remove(row)
#         if not found:#no matches w/ primary keys
#                             moreRecs = pyip.inputYesNo(prompt = "Sorry, no records were found. Do you wish to try again?(Yes/No)\n")#try again?
#                             if moreRecs == 'no':
#                                 rerun = False
#                         else:#matched with primary key
#                             with (open(fileName, 'w')) as motorhouse:
#                                 writer = csv.writer(motorhouse,delimiter = ',')#basically truncates the existing data with the new changed data
#                                 writer.writerows(changedRecs)
#                                 moreRecs = pyip.inputYesNo(prompt = 'Would you like to modify more records?(Yes/No)\n')#do you want MORE?
#                                 if moreRecs == 'no':
#                                     rerun = False
# def request_checker():
#     rerun = True
#     while rerun:
#         cont = confirm('check requests')
#         if not cont:
#             print("Exiting...")
#             break
#         else:
#             with open('bikeRequests.csv','r') as requestFile:
#                 requests = csv.reader(requestFile)
#                 requestList = list(requests)
#                 pending = False
#                 for request in requestList[1:]:
#                     if request:
#                         pending = True
#                         print(request[0])
#                         accept = pyip.inputYesNo(prompt = 'Do you wish to attend to this request?\n')
#                         if accept == 'yes':
#                             dismiss = pyip.inputInt(prompt = "Type '1' to update the records and  '2' to dismiss this request.\n",max = 2, min = 1)
#                             if dismiss == 1:
#                                 add_data()
#                                 requestList.remove(request)
#                                 print("Request fulfilled. Data added.")
#                             else:
#                                 requestList.remove(request)
#                                 print("Request has been dismissed.")
#             with open('bikeRequests.csv','w') as requestFile:
#                 checkedRequests = csv.writer(requestFile, delimiter = ',')
#                 checkedRequests.writerows(requestList)
#             if pending == False:
#                 print("No pending requests.")
#             rerun = False
# def bikeSearchbySpec():
#     rerun = True
#     while rerun:
#         with open('motorhouse.csv','r') as motorhouse:
#             found = False
#             rows = csv.reader(motorhouse)
#             rowsList = list(rows)
#             print(rowsList)
#             header = rowsList[0]
#             specification = pyip.inputMenu(header,prompt = "By what specification do you wish to search?\n",numbered = True)
#             nameOfSpec = pyip.inputStr(prompt = "Enter the desired " + specification + '.\n')with open('motorhouse.csv','r') as motorhouse:
#             print(rowsList)with open('motorhouse.csv','r') as motorhouse:
#             validNames =[]with open('motorhouse.csv','r') as motorhouse:
#             validBikes = []with open('motorhouse.csv','r') as motorhouse:
#             for row in rowsList:with open('motorhouse.csv','r') as motorhouse:
#                 if str(row[header.index(specification)]).upper() == nameOfSpec.upper():with open('motorhouse.csv','r') as motorhouse:
#                     found = True
#                     validBikes.append(row)
#                     validNames.append(row[1])
#                     options = validNames + ['All']
#             view = pyip.inputMenu(options,prompt = "Which of these bikes would you like to view?",numbered = True)
#             if view == 'All':
#                 for bike in validBikes:
#                     bikeDisplay(header,bike) 
#             else:
#                 for bike in validBikes:
#                     if view == bike[1]:
#                         bikeDisplay(header,bike)
#             if not found:
#                 print("No bikes were found.")
#         rerun = False
# def bikeDisplay(header,row):
#     for spec in header:
#         print(spec+':'+row[header.index(spec)])
#     print('---------------------')
# def filterValidity(filter):
#     checkSpecs = []
#     for spec in specs:
#         checkSpecs.append(spec.lower()) #list containing lowercase versions of all the specs
#     valid = False
#     filterRegex = re.compile(r'(\w+)+:+(\w+)') #must be (word)+(:)+(word)
#     found = filterRegex.findall(filter) #list of tuples, tuples are of the format (spec,specName)
#     if len(found) == 1: #checks if user input is valid
#         print(found[0])
#         if found[0][0].lower() in checkSpecs: #checks if user input contains an actual specification
#             valid = True
#     return valid
import csv
fileName = "bikeproj2.csv"
with open(fileName) as fhandle:
    bikeRows = csv.reader(fhandle)
    recs = list(bikeRows)
    for i in recs:
        for j in i:
            if j.isalpha():
                j = j.capitalize()
                
with open(fileName) as handle:
    newRows = csv.writer(handle)
    newRows.writerows(recs)   
