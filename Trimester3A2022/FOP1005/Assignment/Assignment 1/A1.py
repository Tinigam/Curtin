import matplotlib.pyplot as plt
import csv
from Emission import *
def main():
    path = "/home/tinigam/FOP1005/Assignment/Assignment 1/Emission.csv"
    with open(path) as headerline:
        header = ((headerline.readline()).strip()).split(",")
    data = []
    with open(path) as data_file:
        reader = csv.DictReader(data_file)
        record = {}
        for row in reader:
            year = row.get(header[0])
            make = row.get(header[1])
            model = row.get(header[2])
            engine_size = row.get(header[3])
            transmission = row.get(header[4])
            consumption_city = row.get(header[5])
            consumption_long_route = row.get(header[6])
            consumption_average = row.get(header[7])
            emission_CO2 = row.get(header[8])

            record = Emission(year, make, model, engine_size, transmission, consumption_city, consumption_long_route, consumption_average, emission_CO2)
            data.append(record)

# min_year = min(record.year for record in data)
# max_year = max(record.year for record in data)
# min_CO2 = min(record.emission_CO2 for record in data)
# max_CO2 = max(record.emission_CO2 for record in data)

# yearlist = []
# makelist = []
# modellist = []
# CO2list = []
# filterlist = [yearlist, makelist, modellist, CO2list]

def yearFilter():
    min_year = min(record.year for record in data)
    max_year = max(record.year for record in data)
    print("Please select a year between ",min_year, " & ", max_year)
    yearStart = input("Please ENTER the START of year range here ")
    yearEnd = input("Please ENTER the END of year range here ")
    try:
        yearStart = int(yearStart)
        yearEnd = int(yearEnd)
    except ValueError:
        print("\nERROR: Input is not a INT, please try again:\n")
        return yearFilter()
    finally:
        if yearStart <= max_year and yearStart >= min_year and yearEnd <= max_year and yearEnd >= min_year and yearStart <= yearEnd:
            yearlist.append((yearStart, yearEnd))
            return yearlist
        else:
            print("\nERROR! Please enter year range between ", min_year, " & ", max_year,"\n")
            return yearFilter()

# yearFilter()
# print(yearlist)

def makeFilter():
    print("please choose car make from:")
    listofmake = []
    for car in data:
        make = car.make.strip()
        if [make, 0] not in listofmake:
            listofmake.append([make, 0])
    listofmake.sort()
    for make in listofmake:
        for record in filtration(filterlist):
            if record.make.strip() == make[0]:
                make[1] += 1
    # listofmake = list(car.make.strip() for car in data)
    # listofmake.sort()
    # uniquelist = [[listofmake[0], 1]]
    # for i in range(len(listofmake)):
    #     if i < len(listofmake) - 1:
    #         if listofmake[i] == listofmake[i + 1]:
    #             uniquelist[-1][1] += 1
    #         else:
    #             uniquelist.append([listofmake[i + 1], 1])
    # car_makes = set((record.make).strip() for record in data)
    # car_makes = list(car_makes)
    # car_makes.sort()
    car_make_index = 1
    for make in listofmake:
        print(str(car_make_index), ": ", make[0], "\tAmount: ", make[1])
        car_make_index += 1
    filternum = input("Please ENTER the number for the car make filter ")
    try:
        makelist.append(listofmake[int(filternum) - 1][0])
    except ValueError:
        print("\nERROR! Please enter a INT value!\n")
        return makeFilter()
    except IndexError:
        print("\nERROR! Please enter a number in the list!\n")
        return makeFilter()
    finally:
        return makelist

# makeFilter()
# print(makelist)

def modelFilter():
    print("please choose car model from:")
    listofmodel = []
    for car in data:
        model = car.make.strip() + " " + car.model
        if [model, 0] not in listofmodel:
            listofmodel.append([model, 0])
    listofmodel.sort()
    for model in listofmodel:
        for record in filtration(filterlist):
            if record.make.strip() + " " + record.model == model[0]:
                model[1] += 1
    # car_models = set((record.make).strip() + " " + record.model for record in data)
    # car_models = list(car_models)
    # car_models.sort()
    car_model_index = 1
    for car in listofmodel:
        print(str(car_model_index), ":", car[0], "\tAmount: ", car[1])
        car_model_index += 1
    filternum = input("Please ENTER the number for the car model filter ")
    try:
        modellist.append(listofmodel[int(filternum) - 1][0])
    except ValueError:
        print("\nERROR! Please enter a INT value!\n")
        return modelFilter()
    except IndexError:
        print("\nERROR! Please enter a number in the list!\n")
        return modelFilter()
    finally:
        print(modellist)
        return modellist

# listofmodel = []
# for car in data:
#     model = car.make.strip() + " " + car.model
#     if [model, 0] not in listofmodel:
#         listofmodel.append([model, 0])
# listofmodel.sort()
# for model in listofmodel:
#     for record in data:
#         if record.make.strip() + " " + record.model == model[0]:
            # model[1] += 1
# uniquelist = [[listofmodel[0], 1]]
# for i in range(len(listofmodel)):
#     if i < len(listofmodel) - 1:
#         if listofmodel[i] == listofmodel[i + 1]:
#             uniquelist[-1][1] += 1
#         else:
#             uniquelist.append([listofmodel[i + 1], 1])
# for i in uniquelist:
#     print(i)

# modelFilter()
# print(modellist)

def CO2Filter():
    min_CO2 = min(record.emission_CO2 for record in data)
    max_CO2 = max(record.emission_CO2 for record in data)
    print("Please select a CO2 range between ",min_CO2, " & ", max_CO2)
    CO2Start = input("Please ENTER the START of CO2 range here ")
    CO2End = input("Please ENTER the END of CO2 range here ")
    try:
        CO2Start = float(CO2Start)
        CO2End = float(CO2End)
    except ValueError:
        print("\nERROR: Input is not a float, please try again:\n")
        return CO2Filter()
    finally:
        if CO2Start <= max_CO2 and CO2Start >= min_CO2 and CO2End <= max_CO2 and CO2End >= min_CO2 and CO2Start <= CO2End:
            CO2list.append((CO2Start, CO2End))
            return CO2list
        else:
            print("ERROR! Please enter CO2 range between ", min_CO2, " & ", max_CO2,)
            return CO2Filter()

# CO2Filter()
# print(CO2list)

def addFilter():
    print("Filter list:\nYear (Y)\nMake (M)\nModel (O)\nCO2 Emission (C)")
    filter = input("Please ENTER letter of the filter:").upper()
    if filter == "Y":
        yearFilter()
    elif filter == "M":
        makeFilter()
    elif filter == "O":
        modelFilter()
    elif filter == "C":
        CO2Filter()
    else:
        print("ERROR! Please start over!")
        addFilter()

def filtration(filterlist):
    yearedlist = []
    makedlist = []
    modeledlist =[]
    CO2edlist = []
    if filterlist[0] == []:
        yearedlist = data
    else:
        i = 0
        for year in filterlist[0]:
            for record in data:
                if record.year >= filterlist[0][i][0] and record.year <= filterlist[0][i][1]:
                    yearedlist.append(record)
            i += 1
    if filterlist[1] == []:
        makedlist = yearedlist
    else:
        for make in filterlist[1]:
            for record in yearedlist:
                if record.make == make:
                    makedlist.append(record)
    if filterlist[2] == []:
        modeledlist = makedlist
    else:
        for model in filterlist[2]:
            for record in makedlist:
                if (record.make).strip() + " " + record.model == model:
                    modeledlist.append(record)
    if filterlist[3] == []:
        CO2edlist = modeledlist
    else:
        i = 0
        for CO2 in filterlist[3]:
            for record in modeledlist:
                if record.emission_CO2 >= filterlist[3][i][0] and record.emission_CO2 <= filterlist[3][i][1]:
                    # print(filterlist[3][i][0], filterlist[3][i][1])
                    CO2edlist.append(record)
            i += 1
    filteredlist = CO2edlist
    return filteredlist

# filterlist = [[], [], ["Volkswagen ID.4 Pro"], []]
# result = filtration(filterlist)
# for i in result:
#     print(i)

def printNames(list):
    for record in list:
        print(record)

# printNames(filtration(filterlist))

def plotting(xaxis, xlabel, yaxis):
    xaxis = list(xaxis)
    yaxis = list(yaxis)
    plt.suptitle("CO2 emission")
    plt.subplot(2, 2, 1)
    plt.title("Histogram")
    plt.xlabel(xlabel)
    plt.ylabel("Emission CO2 (g/km)")
    plt.hist(xaxis, yaxis.sort())
    plt.subplot(2, 2, 2)
    plt.title("Scatter")
    plt.xlabel(xlabel)
    plt.ylabel("Emission CO2 (g/km)")
    plt.scatter(xaxis, yaxis)
    plt.subplot(2, 2, 3)
    plt.title("Bar")
    plt.xlabel(xlabel)
    plt.ylabel("Emission CO2 (g/km)")
    plt.bar(xaxis, yaxis)
    plt.subplot(2, 2, 4)
    plt.title("line")
    plt.xlabel(xlabel)
    plt.ylabel("Emission CO2 (g/km)")
    plt.plot(xaxis, yaxis)
    plt.show()

def graphData(list):
    print("Please choose x-axis data from:\nMake (M)\nYear (Y)\nEngine Size (E)\n")
    xaxis = input("Please ENTER X-axis letter here ").upper()
    # for record in list:
    #     print(record)
    graphemission = (record.emission_CO2 for record in list)
    if xaxis == "M":
        graphmakelist = (record.make for record in list)
        plotting(graphmakelist, "Emission by Make", graphemission)
    elif xaxis == "Y":
        graphyearlist = (record.year for record in list)
        plotting(graphyearlist, "Emission by Year", graphemission)
    elif xaxis == "E":
        graphenginesizelist = (record.engine_size for record in list)
        plotting(graphenginesizelist, "Emission by Engine Size", graphemission)
    else:
        print("ERROR! Please try again!")
        return graphData(list)

# graphData(filtration(filterlist))

def resetFilter():
    yearlist.clear()
    makelist.clear()
    modellist.clear()
    CO2list.clear()


def DisplayMenu():
    print("\nFilters: ")
    if filterlist[0] == [] and filterlist[1] == [] and filterlist[2] == [] and filterlist[3] == []:
        print("You have not choose filter yet")
    else:
        print("You have chosen:\nYear filter: ", yearlist, "\nMake filter: ", makelist, "\nModel filter: ", modellist, "\nEmission CO2 Filter: ", CO2list)
    print("\nAction Menu:\nAdd Filters (A)\nPrint names (P)\nGraph data (G)\nReset filter (R)\nExit (X)")
    option = input("Please ENTER letter of the action:").upper()
    if option == "A":
        print("You choosed Add filter")
        addFilter()
        DisplayMenu()
    elif option == "P":
        print("You choosed Print names")
        printNames(filtration(filterlist))
        DisplayMenu()
    elif option == "G":
        print("You choosed Graph data")
        graphData(filtration(filterlist))
        DisplayMenu()
    elif option == "R":
        print("You choosed Reset filter")
        resetFilter()
        DisplayMenu()
    elif option == "X":
        print("You choosed Exit, Thanks for using!")
        exit
    else:
        print("ERROR! Please try again!")
        return DisplayMenu()

# DisplayMenu()


def readingCSVFile():
    path = input("Please enter the path of the csv file here: \n")
    try:
        with open(path) as headerline:
            header = ((headerline.readline()).strip()).split(",")

        with open(path) as data_file:
            reader = csv.DictReader(data_file)
            record = {}
            for row in reader:
                year = row.get(header[0])
                make = row.get(header[1])
                model = row.get(header[2])
                engine_size = row.get(header[3])
                transmission = row.get(header[4])
                consumption_city = row.get(header[5])
                consumption_long_route = row.get(header[6])
                consumption_average = row.get(header[7])
                emission_CO2 = row.get(header[8])

                record = Emission(year, make, model, engine_size, transmission, consumption_city, consumption_long_route, consumption_average, emission_CO2)
                data.append(record)
    except FileNotFoundError:
        print("No such file or directory")
        readingCSVFile()
    finally:
        DisplayMenu()

data = []

yearlist = []
makelist = []
modellist = []
CO2list = []
filterlist = [yearlist, makelist, modellist, CO2list]

min_year = 0
max_year = 0
min_CO2 = 0
max_CO2 = 0

readingCSVFile()

# path = "/home/tinigam/FOP1005/Assignment/Assignment 1/Emission.csv"

if __name__ == "__main__":
    main()