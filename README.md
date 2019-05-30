# SimpleKNNAlgorithm
A simple implementation of the k-nearest neighbours algorithm in Python.

The .py file comes with the "weight-height.csv" file already implemented, you can change this to any other dataset as long as it meets the formatting requirements which are:
* have the classifications in the first column (can be any datatype)
* columns after the first one will be considered for attributes in that order (explained further in the example below)

When running the python application you have to call ```predict()``` with a list of the features you want classified.

# Example

```
predict([61.9, 111.1])
```
This will consider columns 2 and 3 as attributes.
```
predict([61.9])
```
This will only consider column 2 as an attribute.
```
predict([61.9, 111.1, 43])
```
This won't work as column 4 in the dataset is empty.

I've included some other datasets you can use in the folder "DemoDataSets", although they are not all actually use use cases for this algorithm.

# Sources
weight-height.csv : https://www.kaggle.com/mustafaali96/weight-height/version/1
heart.csv : https://www.kaggle.com/ronitf/heart-disease-uci
london / seattle data : http://insideairbnb.com/get-the-data.html (I have edited the data)
k-nearest neightbors algorithm : https://en.wikipedia.org/wiki/K-nearest_neighbors_algorithm
