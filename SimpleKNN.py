#Importing pandas and csv to work with datasets
import pandas
import csv
from statistics import mode

#Reading data and making its dataframe
with open("weight-height.csv","r") as readfile:
    reader1 = csv.reader(readfile)
    read = []
    
    for row in reader1:
        if len(row)!= 0:
            read=read+[row]
            
readfile.close()
df = pandas.DataFrame(read)

#Main function which takes a list of the features of the thing you want to classify.
#It ignores the first column in the dataset and then assumes the features come in the same order as in the CSV.
#It produces a list top 13 (depends on the length of the lowest_finds list) labels which have features most closely resembeling the input.

def predict(features):
    new_lowest_distance = 0 #This is the "distance" between your input and the current row it's being compared to. Reset after every for loop.
    lowest = "" #This is the current lowest distance found
    lowest_finds = ["","","","","","","","","","","","",""] #This is where the top 13 closest rows are stored
    lowest_finds_labels = lowest_finds.copy() #This is where just their labels are to be stored
    
    for row in range(1, len(df)): #Loops the whole dataframe, comparing every row with the input
    #for row in range(1, 1000): #Use if dataset is taking too long to run.

        for x in features: #Finds the distance between the input and current row
            new_lowest_distance += (x-float(df[features.index(x)+1][row]))**2

        #The following procedure looks very but. What it does is add the new lowest distances to the lowest_finds list and also their labels, keeping the shortest distances at all times and filling the list ASAP.
        for i, oldlowest in enumerate(lowest_finds):
            if lowest_finds[-1] == "":
                for a, oldlowest1 in enumerate(lowest_finds):
                    if oldlowest1 == "":
                        lowest_finds[a] = new_lowest_distance
                        lowest_finds_labels[a] = df[0][row]
                break
                
            elif new_lowest_distance < oldlowest:
                lowest_finds[lowest_finds.index(max(lowest_finds))] = new_lowest_distance
                lowest_finds_labels[lowest_finds.index(max(lowest_finds))] = df[0][row]
                break
            
            else: pass

        #Following if statements simply sets "prediction" as the label of the row which is the shortest distance from the input.
        #This will be changed so that the prediction is only based on mode of the "lowest_finds_labels" list.
        if lowest == "":
            lowest = new_lowest_distance
            prediction = df[0][row]
            
        elif new_lowest_distance < lowest:
            lowest = new_lowest_distance
            prediction = df[0][row]

        else: pass
        #Code between previous comment to this one can be removed as we should be using the mode of lowest_finds_labels instead of the single best prediction
        new_lowest_distance = 0 #Reset the lowest distance for the next row.

    print(lowest_finds, "\n", lowest_finds_labels) #Mainly for debugging
    print("Mode of lowest_finds_labels: ", mode(lowest_finds_labels)) #This is the mode of the predictions and should be better than just using the latest prediction
    
    return prediction #1 = male, 0 = female, mode is what really matters

#For Height-Weight
#predict([61.9, 111.1])

#This is the average height and weight, where obviously the program would be least accurate
#predict([66.36755975, 161.4403568])
