import getopt
import sys

import pandas


def get_data_frame(url):
    return pandas.read_csv(url)


def distance(a, b):
    distance_square = 0
    for a_feature, b_feature in zip(a, b):
        distance_square += (a_feature - b_feature) ** 2
    return distance_square ** 0.5


def mode(data):
    return max(set(data), key=data.count)


def is_smaller_find(find, closest_rows):
    classifications = closest_rows[0]
    distances = closest_rows[1]
    # Check for Nones before finding rows to replace
    for classification in classifications:
        if classification is None:
            return classifications.index(classification)

    smallest_distance_index = distances.index(max(distances))
    if find < distances[smallest_distance_index]:
        return smallest_distance_index


def get_initial_rows(k):
    x = []
    for i in range(k):
        x.append(None)
    return [x, x.copy()]


def get_classification(df, k, features):
    closest_rows = get_initial_rows(k)

    for row in df.values:
        row_classification = row[0]
        row_distance = distance(features, row[1::])

        replace_index = is_smaller_find(row_distance, closest_rows)
        if replace_index is not None:
            closest_rows[0][replace_index] = row_classification
            closest_rows[1][replace_index] = row_distance

    return mode(closest_rows[0])


# TODO add validation
if __name__ == '__main__':
    data_url = None
    k = 11
    features = None

    try:
        opts, args = getopt.getopt(sys.argv[1:], "hd:k:q:", ["help", "data=", "features="])
    except getopt.GetoptError:
        print("SimpleKNN.py -d <data_url> -k <k_value> -q <query_features>")
        sys.exit(2)

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            # TODO add more help information
            print("usage: SimpleKNN.py -d <data_url> -k <k_value> -q <query_features>")
            sys.exit(2)
        elif opt in ("-d", "--data"):
            data_url = arg
        elif opt in ("-q", "--features"):
            features = list(map(int, arg.split(",")))
        elif opt == "-k":
            k = arg

    if data_url is not None and features is not None:
        print("Classification: {}".format(get_classification(get_data_frame(data_url), int(k), features)))

# python SimpleKNN.py -d weight-height.csv -k 5 --features 70,170
