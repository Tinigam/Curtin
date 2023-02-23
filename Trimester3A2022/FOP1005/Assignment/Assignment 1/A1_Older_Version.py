import matplotlib.pyplot as plt

path = "/home/tinigam/FOP1005/Assessment/Assessment 1/Emission.csv"
file = open(path)
datalist = file.readlines()
datalist = datalist[1:]

file.close()

car = []
year = []
make = []
model = []
engine_size = []
transmisson = []
consumption_city = []
consumption_long_route = []
consumption_average = []
emission_CO2 = []

yearlist = []
makelist = []
modellist = []
co2list = []
filterlist = [yearlist, makelist, modellist, co2list]

for line in datalist:
    line = line.strip()
    line_s = line.split(",")
    for data in line_s:
        year.append(int(line_s[0]))
        make.append(line_s[1])
        model.append(line_s[2])
        engine_size.append(int(line_s[3]))
        transmisson.append(line_s[4])
        consumption_city.append(float(line_s[5]))
        consumption_long_route.append(float(line_s[6]))
        consumption_average.append(float(line_s[7]))
        emission_CO2.append(float(line_s[8]))
    car.append(line_s)
    
for i in car:
    i[0] = int(i[0])
    i[3] = int(i[3])
    i[5] = float(i[5])
    i[6] = float(i[6])
    i[7] = float(i[7])
    i[8] = float(i[8])

# def yearFilter():
#     print("Please select a year between ",min(year), " & ", max(year))
#     yearRange = input("Please ENTER the year range here such as '2015-2020': ")
#     yearStart = int(yearRange[:4])
#     yearEnd = int(yearRange[-4:])
#     if yearStart < max(year) and yearStart > min(year) and yearEnd < max(year) and yearEnd > min(year) and yearStart < yearEnd:
#         for i in range(yearStart, yearEnd + 1):
#             yearlist.append(i)
#         return yearlist
#     else:
#         print("ERROR! Please enter a correct year range!\n")
#         return yearFilter()

# yearFilter()
# print(yearlist)

def yearFilter():
    print("Please select a year between ",min(year), " & ", max(year))
    filter = input("Please ENTER the year here ")
    if filter.isdigit():
        filter = int(filter)
        if filter < max(year) and filter > min(year):
            return filter
        else:
            print("ERROR! Please try again!")
            return(yearFilter())
    else:
        print("ERROR! Please try again!")
        return yearFilter() 

# yearFilter()
# print(yearlist)

def makeFilter():
    print("please choose car make from:")
    car_make = set(make)
    car_make_index = 1
    for car in car_make:
        print(str(car_make_index), ": ", car)
        car_make_index = car_make_index + 1
    filter = input("Please ENTER the number for the car make filter ")
    if filter.isdigit() and filter > 0 and filter < len(car_make):
        return car_make[car_make_index]
    print("ERROR! Please try again!")
    return makeFilter()

# makeFilter()

def modelFilter():
    print("please choose car model from:")
    car_model = set(model)
    print(car_model)
    filter = input("Please ENTER the car model filter ")
    for i in car_model:
        if i == filter:
            return filter
    print("ERROR! Please try again!")
    return modelFilter()

def co2Filter():
    print("Please select a co2 between ",min(emission_CO2), " & ", max(emission_CO2))
    co2Range = input("Please ENTER the emission of CO2 range here such as '5.0-10.0': ")
    co2Start = int(co2Range[:4])
    co2End = int(co2Range[-4:])
    if co2Start < max(emission_CO2) and co2Start > min(emission_CO2) and co2End < max(emission_CO2) and co2End > min(emission_CO2) and co2Start < co2End:
        for i in range(co2Start, co2End + 1):
            co2list.append(i)
        return co2list
    else:
        print("ERROR! Please enter a correct year range!\n")
        return yearFilter()

# co2Filter()

# def co2Filter():
#     print("Please select a range between ",min(emission_CO2), " & ", max(emission_CO2))
#     filter = input("Please ENTER the range here ")
#     filter = float(filter)
#     if filter < max(emission_CO2) and filter > min(emission_CO2):
#         return filter
#     else:
#         print("ERROR! Please try again!")
#         return co2Filter()

def addFilter():
    print("Filter list:\nYear (Y)\nMake (M)\nModel (O)\nCO2 Emission (C)")
    filter = input("Please ENTER letter of the filter:").upper()
    if filter == "Y":
        # yearlist.append(yearFilter())
        yearFilter()
    elif filter == "M":
        makelist.append(makeFilter())
    elif filter == "O":
        modellist.append(modelFilter())
    elif filter == "C":
        co2list.append(co2Filter())
    else:
        print("ERROR! Please start over!")
        addFilter()


def filtration(list, index, filter):
    filteredlist = []
    for i in list:
        if i[index] != filter:
            filteredlist.append(i)
    return filteredlist

def printNames(list):
    print("You have choosed these filters:")
    print(filterlist)
    for i in yearlist:
        list = filtration(list, 0, i)
    for i in makelist:
        list = filtration(list, 1, i)
    for i in modellist:
        list = filtration(list, 2, i)
    for i in co2list:
        list = filtration(list, 8, i)
    for i in list:
        print(i)

def plotting(xaxis, xlabel):
    plt.suptitle("CO2 emission")
    # add filter in str
    plt.xlabel(xlabel)
    plt.ylabel("Emission CO2 (g/km)")
    plt.subplot(2, 2, 1)
    plt.title("Histogram")
    plt.hist(xaxis, emission_CO2)
    plt.subplot(2, 2, 2)
    plt.title("Scatter")
    plt.scatter(xaxis, emission_CO2)
    plt.subplot(2, 2, 3)
    plt.title("Bar")
    plt.bar(xaxis, emission_CO2)
    plt.subplot(2, 2, 4)
    plt.title("line")
    plt.plot(xaxis, emission_CO2)

def graphData(list):
    print("Please choose x-axis data from:\nMake (M)\nYear (Y)\nEngine Size (E)\n")
    xaxis = input("Please ENTER X-axis letter here").upper()
    if xaxis == "M":
        plotting(make, co2list)
    elif xaxis == "Y":
        plt.xlabel("Model of cars")
    elif xaxis == "E":
        plt.xlabel("Engine Size of cars (Kw)")
    else:
        print("ERROR! Please try again!")
        return graphData(list)

def resetFilter():
    filterlist[0] = []
    filterlist[1] = []
    filterlist[2] = []
    filterlist[3] = []

def DisplayMenu():
    print("WELCOME TO MENU")
    print("Action Menu:\nAdd Filters (A)\nPrint names (P)\nGraph data (G)\nReset filter (R)\nExit (X)")
    option = input("Please ENTER letter of the action:").upper()
    if option == "A":
        print("You choosed Add filter")
        addFilter()
    elif option == "P":
        print("You choosed Print names")
        printNames(car)
    elif option == "G":
        print("You choosed Graph data")
        graphData(car)
    elif option == "R":
        print("You choosed Reset filters")
        resetFilter()
    elif option == "X":
        print("You choosed Exit, Thanks for using!")
    else:
        print("Action Menu:\nAdd Filters (A)\nPrint names (P)\nGraph data (G)\nReset filter (R)\nExit (X)")
        return DisplayMenu()


# # TEST CASES of printNames:
# filterlist[0].append("2022")
# filterlist[0].append("2021")
# filterlist[1].append("Volkswagen")
# filterlist[1].append("Tesla")
# filterlist[2].append("Taycan Turbo S")
# filterlist[2].append("Taycan Turbo")
# filterlist[3].append("10.5")
# #printNames(car)
# DisplayMenu()




