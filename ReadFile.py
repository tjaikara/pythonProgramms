

fileOne = open("/Users/taikara/Desktop/AllCompanies.txt", "r")
fileTwo = open("/Users/taikara/Desktop/wantedCompanies.txt", "r")

companies = open("/Users/taikara/Desktop/test.txt", "r")

fileThree = open("/Users/taikara/Desktop/temp.txt", "w")

fileDataListOne = []
fileDataListTwo = []

fileDataListOne = fileOne.read().splitlines()
fileDataListTwo = fileTwo.read().splitlines()

companyList = companies.read().splitlines()

i = 0
for line in fileDataListOne:

    i += 1
    if line not in fileDataListTwo:
        fileThree.write(line+'\n')


fileThree.close()