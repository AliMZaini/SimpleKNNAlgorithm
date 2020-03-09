# Importing pandas and csv to work with datasets
import pandas
import csv
import math

# Reading data and making its dataframe
with open("weight-height.csv", "r") as readfile:
    reader1 = csv.reader(readfile)
    read = []

    for row in reader1:
        if len(row) != 0:
            read = read + [row]

readfile.close()
df = pandas.DataFrame(read)


# Main function which takes a list of the features of the thing you want to classify.
# It ignores the first column in the dataset and then assumes the features come in the same order as in the CSV.

def predict(features):
    new_lowest_distance = 0  # This is the "distance" between your input and the current row it's being compared to. Reset after every for loop.
    lowest = ""  # This is the current lowest distance found
    lowest_finds = [""]
    k = 3
    for a in range(1, 10):
        lowest_finds.append("")
    # print(lowest_finds)
    lowest_finds_labels = lowest_finds.copy()  # This is where just their labels are to be stored

    for row in range(1, len(df)):  # Loops the whole dataframe, comparing every row with the input
        # for row in range(1, 1000): #Use if dataset is taking too long to run.

        for x in features:  # Finds the distance between the input and current row
            new_lowest_distance += (x - float(df[features.index(x) + 1][row])) ** 2

        # The following procedure looks very but. What it does is add the new lowest distances to the lowest_finds list and also their labels, keeping the shortest distances at all times and filling the list ASAP.
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

            else:
                pass

        if lowest == "":
            lowest = new_lowest_distance
            prediction = df[0][row]

        elif new_lowest_distance < lowest:
            lowest = new_lowest_distance
            prediction = df[0][row]

        else:
            pass
        new_lowest_distance = 0  # Reset the lowest distance for the next row.

    prediction = None
    for label in set(lowest_finds_labels):
        prob_of_label = 100 * (lowest_finds_labels.count(label) / len(lowest_finds_labels))
        # print(label, prob_of_label)
        if prediction == None:
            prediction = label
        elif prob_of_label > 100 * (lowest_finds_labels.count(prediction) / len(lowest_finds_labels)):
            prediction = label
    # print(lowest_finds_labels)
    return prediction  # 1 = male, 0 = female, mode is what really matters


for data_row in [[61.97212119, 132.9074143], [62.18508321, 132.2470703], [72.66524188, 219.0951656],
                 [68.09296485, 169.936601], [63.81484661, 132.2134162], [60.14955877, 100.7512358],
                 [71.12708285, 207.5751785], [68.26284966, 169.22503469999998], [64.52043061, 138.7898093],
                 [72.24774718, 217.3784983]]:
    print("height, weight: ", data_row)
    print("prediction: ", predict(data_row))
# For Height-Weight
# predict([61.9, 111.1])

# This is the average height and weight, where obviously the program would be least accurate
# predict([66.36755975, 161.4403568])