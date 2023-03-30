import numpy as np
import pandas as pd
import csv
import math
import argparse

def fetch_data(filepath):
    file = open(filepath)
    file_read = csv.reader(file)
    read_List = list(file_read)
    read_List = [read_List[i] for i in range(len(read_List)) if read_List[i] != []]
    file.close()
    return read_List

def sample_entropy(df, log_base):
    unique_target = list(df[df.columns[-1]].value_counts())
    overallentropy = 0
    N = sum(unique_target)
    for i in unique_target:
        temp = (-1) * (i / N) * (math.log((i / N), log_base))
        overallentropy += temp
    return overallentropy


def attr_entropy(attr):
    unique_attr, N = np.unique(attr, return_counts=True)
    entropy = sum([(-cnt / len(attr)) * math.log((cnt / len(attr)), log_base) for cnt in N])
    return entropy, unique_attr, N

#Calculating maximum entropy
def max_entropy(entropy_dictonary):
        max_infogain = -800
        max_infogain_attr = ""
        for key, value in entropy_dictonary.items():
            if value["info_gain"] > max_infogain:
                max_infogain = value["info_gain"]
                max_infogain_attr = key
        return max_infogain_attr


def build_tree(entropy_dataset, dataset, depth, dictonary_track={}, parent_index=-1):
    entropy_dictonary = {}
    dataset_len = len(dataset[0])
    completed_node = dictonary_track.get(parent_index, [])
    for i in range(dataset_len - 1):
        if i not in completed_node:
            attr = [dataset[row][i] for row in range(len(dataset))]
            attrib_class, attrib_count = np.unique(attr, return_counts=True)
            attrib_dict = {attrib_class[i]: attrib_count[i] for i in range(len(attrib_class))}
            entropy_attr = {}
            info_gain = entropy_dataset
            for c in attrib_class:
                # calculate entropy
                d = [dataset[row][dataset_len - 1] for row in range(len(dataset)) if dataset[row][i] == c]
                feature_ent, target_classes, tgt_class_len = attr_entropy(d)
                entropy_attr[c] = [feature_ent, target_classes, tgt_class_len]
                info_gain = info_gain - (attrib_dict[c] / len(dataset)) * entropy_attr[c][0]
            entropy_attr["info_gain"] = info_gain
            entropy_attr["attr_index"] = i
            entropy_dictonary["att" + str(i)] = entropy_attr
    
    max_infogain_attr = max_entropy(entropy_dictonary)

    dictonary_track[entropy_dictonary[max_infogain_attr]["attr_index"]] = completed_node + [parent_index]
    for key, value in entropy_dictonary[max_infogain_attr].items():
        if (key != "info_gain") and (key != "attr_index"):
            if len(set(completed_node)) == feature_len:
                tgt_class_len = entropy_dictonary[max_infogain_attr][key][2]
                node = entropy_dictonary[max_infogain_attr][key][1][np.argmax(tgt_class_len)]
                #print(dictonary_track)
                print(str(depth) + "," + max_infogain_attr + "=" + str(key) + "," + str(
                     entropy_dictonary[max_infogain_attr][key][0]) + "," + str(node))
            else:
                node = "no_leaf" if entropy_dictonary[max_infogain_attr][key][0] != 0 else entropy_dictonary[max_infogain_attr][key][1][0]
                #print(dictonary_track)
                print(str(depth) + "," + max_infogain_attr + "=" + str(key) + "," + str(
                    entropy_dictonary[max_infogain_attr][key][0]) + "," + node)
                attr_d = [dataset[i] for i in range(len(dataset)) if
                          dataset[i][entropy_dictonary[max_infogain_attr]["attr_index"]] == key]
                if node == "no_leaf":
                    build_tree(entropy_dataset, attr_d, depth + 1, dictonary_track, entropy_dictonary[max_infogain_attr]["attr_index"])


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--data')
    args = parser.parse_args()
    df = pd.read_csv(args.data)
    X = fetch_data(args.data)
    feature_len = len(X[0]) - 1
    Y = [X[row][feature_len] for row in range(len(X))]
    log_base = len(df[df.columns[-1]].value_counts())
    entropy_dataset = sample_entropy(df, log_base)
    print("0,root," + str(entropy_dataset) + ",no_leaf")
    build_tree(entropy_dataset, X, 1)
