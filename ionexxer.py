#Ionosphere Visuals
#Script by Brian Cantrell
#
#
import csv

def getLat(line):

    #strip trailing white space and split on white space
    newStr = line.strip().split(' ')
    #index first element of resulting list
    latLon = newStr[0]
    #strip off last six elements
    latLon = latLon[:-6]
    #cast as float
    lattitude = float(latLon)
    return lattitude

#def mapData():

def main():
    
    joined = ' '
    theVals = []
    theLats = []
    values = []
    finalVals = []
    #open textfile
    userFile = raw_input("\nPlease enter the full path of the data file you'd like to process and press 'Enter':\n\n")
    
    theData = open(userFile, "r")
    
    #split lines into iterable list
    datlist = theData.read().splitlines()
    theData.close()
    
    #loop over list and get lattitudes and values - Fill arrays
    for i in range(len(datlist)):
        if "LAT/LON1/LON2/DLON/H" in datlist[i]:
            lats = getLat(datlist[i])
            theLats.append(lats)
            vals = [datlist[i+1], datlist[i+2], datlist[i+3], datlist[i+4], datlist[i+5]]
            for e in vals:
                joined = ' '.join(e.split()).replace(" ", ",")
                theVals.append(joined)
                
   #Group value lists by lattitude
    innerList = []
    outerList = []
    for i in theVals:
        innerList.append(i)
        if len(innerList) > 4:
            outerList.append(innerList)
            innerList = []
    
    #Massage the data
    for i in outerList:
        x = ' '.join(i).replace(' ', ',').replace("[",'').split(",")
        #Map values to integers and assign to values
        values.append(map(int, x))
   
    #Create dictionary for final output  
    #legend = dict(zip(theLats,values))

# -- Writing contents of lat and val lists to csv -- #

#    latFile = csv.writer(open('ionLatsFull.csv', 'w'))
#    for item in theLats:
#      latFile.writerow([item])
       
    valFile = csv.writer(open('ionVals.txt','w'))
    for item in values:
        valFile.writerow([item])


        
# -- Writing legend to csv or txt -- #

#    theFile = csv.writer(open('ion.csv', 'w'))
#    for key in legend.items():
#        theFile.writerow([key])
#    theFile = open('ion.txt', 'w')
#    theFile.write(str(legend))
   
    
if __name__ == "__main__": main()

