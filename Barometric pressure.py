import pandas as pd
import numpy as np


#Read all the files to csv and add them to an iterable list
data2012=pd.read_csv('Environmental_Data_Deep_Moor_2012.txt', delimiter='\t')
data2013=pd.read_csv('Environmental_Data_Deep_Moor_2013.txt', delimiter='\t')
data2014=pd.read_csv('Environmental_Data_Deep_Moor_2014.txt', delimiter='\t')
data2015=pd.read_csv('Environmental_Data_Deep_Moor_2015.txt', delimiter='\t')
files=[data2012, data2013, data2014, data2015]

#finds the indexes of user input for search within a year
def findIndexes(startDT,endDT):
    startIndex, endIndex, fileIndex=0,0,0
    #iterate over all the files
    for i in range(len(files)):
        file=files[i]
        for j in range(len(file)):
            if file['date       time    '][j]==startDT:
                startIndex, fileIndex=j,i
            if file['date       time    '][j]==endDT:
                endIndex=j
                if i>fileIndex:
                    print('Select two dates within the same year please')
                    startIndex, endIndex=0,0
                    break
    if startIndex==0 or endIndex==0:
        print('Entry not found, please try again')
        return []
    return fileIndex, startIndex, endIndex

#return the slope of the barometric pressure over inputted range
def barometricSlope(indexes):
    barometricPressure=[]
    fileIndex=indexes[0]
    startIndex=indexes[1]
    endIndex=indexes[2]
    
    file=files[fileIndex]
    i=startIndex
    while i<=endIndex:
        barometricPressure.append(file['Barometric_Press'][i])
        i+=1

    length=len(barometricPressure)-1
    slope=barometricPressure[length]-barometricPressure[0]

    if slope==0.0:
        result=f'No slope, pressure difference {round(slope,4)}'
    elif slope>0.0:
        result=f'Slope + , pressure difference {round(slope,4)}'
    else:
        result=f'Slope - , pressure difference {round(slope,4)}'
    return result

#process user inputs and run funcitons
def main():  
    start=True
    while start:
        startIndex=input('Enter start date:')
        endIndex=input('Enter end date:')
        indexes=findIndexes(startIndex, endIndex)
        print(indexes)
        if indexes==True:
            slope=barometricSlope(indexes)
            print(slope)
        restart=input('Do you want to enter a new date (Y/N):')
        if restart=='N' or restart=='n':
            start=False

if __name__=="__main__":
    main()
