dictBorn = {}                     # ...........dictionary for stroing the birth year and number of person born in that year.......
dictDeath = {}                    # .......... dictionary for stroing the death year and number of person born in that year .......
dictPopulation = {}               # ........... dictionary for stroing the population per year.............
fileInputPs21 = open(r"C:\Users\mohitg\Desktop\Bits-1stSem\Data Structure\Assignment\inputPs21.txt", "r")           # .........for read all data from inputPs21.txt file......
fileOutputPS21=open(r"C:\Users\mohitg\Desktop\Bits-1stSem\Data Structure\Assignment\outputPS21.txt", "w")           # ........for write  all data in  outputPS21.txt file.....
filePromptsPS21 = open(r"C:\Users\mohitg\Desktop\Bits-1stSem\Data Structure\Assignment\promptsPS21.txt", "r")       # ........for read command from promptsPS21.txt file.....


# .......This function takes the output of all the other functions and prints it to output file outputPS21.txt........
def printOutput(string):
    fileOutputPS21.write(string)

#...........The function will then make one or more dictionaries where key is the year and value can be either the number of births, number of deaths and number of people alive.
# ......... a. Dictionary for number of births
# ......... b.Dictionary for number of deaths
#......... c. Dictionary for population
def readInputData():
    count = 0                           # ........for counting how many records processed
    minBirthYear = int()                #.........for storing minimum birth in data
    maxBirthYear = int()                #.........for storing maximum birth in data

    minDeathYear = int()                # ........ for storing minimum death in data
    maxDeathYear = int()                # .........for storing maximum death in data

    minYear=int()                       # ..........for storing minimum year in records
    maxYear=int()                       # ...........for storing maximum year in records
    totalBirth = int()                  # ...........for storing totalBirth in records
    totalDeath = int()                  # ...........for storing totalDeath in records
    totalPopulation = int()             # ...........for storing totalPopulation in records

    for line in fileInputPs21:           # ....... for loop is used for reading data line by line form input file
        line = line.strip()
        if line:
            record = line.split(",")
# ......... finding  birth year and number of births and stroing in dictonary..............
            dateOfBirth = record[2]
            dob_split = dateOfBirth.split("-")
            birthYear = dob_split[2]
            if not bool(dictBorn):
                dictBorn[birthYear] = 1
                minBirthYear = birthYear
                maxBirthYear = birthYear
            else:
                if birthYear < minBirthYear:
                    minBirthYear = birthYear
                elif birthYear > maxBirthYear:
                    maxBirthYear = birthYear

                if birthYear in dictBorn:
                    dictBorn[birthYear] += 1
                else:
                    dictBorn[birthYear] = 1
# ......... finding  death year and number of deaths and stroing in dictonary..............
            dateOfDeath = record[3]
            if  dateOfDeath :
                dod_split = dateOfDeath.split("-")
                deathYear = dod_split[2]
                if not bool(dictDeath):
                    dictDeath[deathYear] = 1
                    minDeathYear = deathYear
                    maxDeathYear = deathYear
                else:
                    if deathYear < minDeathYear:
                        minDeathYear = deathYear
                    elif deathYear > maxDeathYear:
                        maxDeathYear = deathYear

                    if deathYear in dictDeath:
                        dictDeath[deathYear] += 1
                    else:
                        dictDeath[deathYear] = 1

#............ printing birth year and number of person per year ................
    minBirthYear = int(minBirthYear)
    maxBirthYear = int(maxBirthYear)+1
    for key in range(minBirthYear, maxBirthYear):
        count+=1
        k=str(key)
        if k in dictBorn:
            s1="No. of people born in "+ k+": "+str(dictBorn[k])+"\n"
            printOutput(s1)

# ............. printing death year and number of person per year ..............
    minDeathYear = int(minDeathYear)
    maxDeathYear = int(maxDeathYear) + 1
    for key in range(minDeathYear, maxDeathYear):
        count += 1
        k = str(key)
        if k in dictDeath:
            s1 = "No. of people died in " + k + ": " + str(dictDeath[k]) + "\n"
            printOutput(s1)

# ............ storing  record of population per year in dictonary and printing population per year in output txt file .........
    if minBirthYear <= minDeathYear:
        minYear = int(minBirthYear)
    else:
        minYear = int(minDeathYear)
    if maxBirthYear >= maxDeathYear:
        maxYear = int(maxBirthYear) + 1
    else:
        maxYear = int(maxDeathYear) + 1
    for key in range(minYear, maxYear):
        count += 1
        k = str(key)
        if k in dictBorn:
            totalBirth += dictBorn[k]
        if k in dictDeath:
            totalDeath += dictDeath[k]

        totalPopulation = totalBirth - totalDeath
        dictPopulation[k] = totalPopulation
        s1 = "No. of people alive in " + k + ": " + str(dictPopulation[k]) + "\n"
        printOutput(s1)

    s2 = str(count) + " records captured.\n"
    printOutput(s2)

readInputData()

#........This function returns the number of people born in a particular year by looking up the year from the dictionary.
# The function is called when the following tag ‘bornIn’ is encountered in the promptsPS21.txt file........
def countBorn(dictBorn, bornInYear):
    key=bornInYear.strip()
    s2="No. of people born in "+key+" : "+str(dictBorn[key])+"\n"
    printOutput(s2)

#......This function returns the number of people who died in a particular year by looking up the year from the dictionary.
# The function is called when the following tag ‘diedIn’ is encountered in the promptsPS21.txt file.............
def countDied(dictDeath, deadInYear):
    key = deadInYear.strip()
    s2 = "No. of people died in " + key+ " : " + str(dictDeath[key])+"\n"
    printOutput(s2)

#......This function returns the year of maximum population by looking up the year from the dictionary.
# The function is called when the following tag ‘maxPopulation’ is encountered in the promptsPS21.txt file........
def maxPop(dictPopulation):
    maxPopu=int()
    year=int()
    for i in dictPopulation:
        if not maxPopu:
            maxPopu=dictPopulation[i]
            year = i
        else:
            if dictPopulation[i] > maxPopu:
                maxPopu=dictPopulation[i]
                year=i
    s1="Maximum population was in year "+ str(year) +" with " +str(maxPopu) +" people alive."+"\n"
    printOutput(s1)

#........This function returns the year of minimum population by looking up the year from the dictionary.
# The function is called when the following tag ‘minPopulation’ is encountered in the promptsPS21.txt file.........
def minPop(dictPopulation):
    minPopu = int()
    year = int()
    for i in dictPopulation:
        if not minPopu:
            minPopu = dictPopulation[i]
            year = i
        else:
            if dictPopulation[i] < minPopu:
                minPopu = dictPopulation[i]
                year = i
    s1 = "Minimum population was in year " + str(year) + " with " + str(minPopu) + " people alive." + "\n"
    printOutput(s1)

#........This function returns the year of maximum births by looking up the year from the dictionary.
# The function is called when the following tag ‘maxBirth’ is encountered in the promptsPS21.txt file........
def maxBirth(dictBorn):
    maxBorn=int()
    year=int()
    for i in dictBorn:
        if not maxBorn:
            maxBorn=dictBorn[i]
            year=i
        else:
            if dictBorn[i]>maxBorn:
                maxBorn = dictBorn[i]
                year = i
    s1 = "Maximum births were in year " + str(year) + " with " + str(maxBorn) + " people born." + "\n"
    printOutput(s1)

#.........This function returns the year of maximum deaths by looking up the year from the dictionary.
# The function is called when the following tag ‘maxDeath’ is encountered in the promptsPS21.txt file.......
def maxDeath(dictDeath):
    maxDeaths = int()
    year = int()
    for i in dictDeath:
        if not maxDeaths:
            maxDeaths = dictDeath[i]
            year = i
        else:
            if dictDeath[i] > maxDeaths:
                maxDeaths = dictDeath[i]
                year = i
    s1 = "Maximum deaths were in year " + str(year) + " with " + str(maxDeaths) + " people death." + "\n"
    printOutput(s1)

# ......... this for loop is used to read promptsPS21.txt file line by line and calling the particular function according to the keyword read.....
for line in filePromptsPS21:
    line = line.strip()
    if line:
        record = line.split(":")
        data=record[0]
        if data=="bornIn":
            bornInYear=record[1]
            if bool(dictBorn):
                countBorn(dictBorn, bornInYear)
        elif data=="diedIn":
            deadInYear=record[1]
            if bool(dictDeath):
                countDied(dictDeath, deadInYear)
        elif data == "maxPopulation":
            if bool(dictPopulation):
                maxPop(dictPopulation)
        elif data == "minPopulation":
            if bool(dictPopulation):
                minPop(dictPopulation)
        elif data == "maxBirth":
            if bool(dictBorn):
                maxBirth(dictBorn)
        elif data == "maxDeath":
            if bool(dictDeath):
                maxDeath(dictDeath)

fileInputPs21.close()
fileOutputPS21.close()





