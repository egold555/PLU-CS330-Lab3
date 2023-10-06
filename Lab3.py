"""
 Name: Eric Golde
 Assignment: Lab 3 - Process dataset
 Course: CS 330
 Semester: 2023
 Instructor: Dr. Cao
 Date: 10/5/2023
 Sources consulted: any books, individuals, etc consulted

 Known Bugs: description of known bugs and other program imperfections

 Creativity: anything extra that you added to the lab

 Instructions: instructions to user on how to execute your program

"""
import sys
import argparse
import math
import random


def splitData(data, trainData, testData, ratio):
    """
    Input: data
    Output: trainData, used for training your machine learning model
            testData, used to evaluate the performance of your machine learning model
            ratio, decide the percentage of training data on the whole dataset.
    Example:
            You have a training data with 10000 data record, ratio is 0.7, so you will split the whole dataset and store the first 7000 of them in trainData, and the rest 3000 in testData
    Instruction:
            There is no grading script for this function, because different group may select different dataset depending on their course project, but generally you should make sure that you code can divide the dataset correctly, since you may use it for the course project
    """
    # your code here

    for d in data:
        if len(trainData) < len(data) * ratio:
            trainData.append(d)
        else:
            testData.append(d)


def splitDataRandom(data, trainData, testData, ratio):
    """
    Input: data
    Output: trainData, used for training your machine learning model
            testData, used to evaluate the performance of your machine learning model
            ratio, decide the percentage of training data on the whole dataset.
    Example:
            You have a training data with 10000 data record, ratio is 0.7, so you will split the whole dataset and store 7000 of them in trainData, and 3000 in testData.
    Instruction:
            Almost same as splitData, the only difference is this function will randomly shuffle the input data, so you will randomly select data and store it in the trainData
    """
    # your code here
    random.shuffle(data)
    splitData(data, trainData, testData, ratio)
    pass


def main():
    options = parser.parse_args()
    mode = options.mode  # first get the mode
    print("mode is " + mode)
    """
    similar to Lab 2, please add your testing code here
    """
    # your code here

    inputFile = options.input

    ratio = float(options.ratio)

    skipNLines = int(options.skiplines)

    inputData = []
    trainData = []
    testData = []

    # read in the data
    with open(inputFile, 'r') as f:
        for line in f:
            inputData.append(line.strip())

    # skip the first n lines
    if skipNLines > 0:
        inputData = inputData[skipNLines:]

    # split the data
    if mode == 'R':
        print("Splitting random with ratio " + str(ratio) + "...")
        splitDataRandom(inputData, trainData, testData, ratio)
    elif mode == 'N':
        print("Splitting normal with ratio " + str(ratio) + "...")
        splitData(inputData, trainData, testData, ratio)
    else:
        print("Invalid mode")
        sys.exit(0)


    # write the data to the files
    with open("trainData.txt", 'w') as f:
        for line in trainData:
            f.write(line + "\n")

    with open("testData.txt", 'w') as f:
        for line in testData:
            f.write(line + "\n")

    print("Finished!")


def showHelper():
    """
    Similar to Lab 2, please update the showHelper function to show users how to use your code
    """
    parser.print_help(sys.stderr)
    # your code here

    sys.exit(0)


if __name__ == "__main__":
    # ------------------------arguments------------------------------#
    # Shows help to the users                                        #
    # ---------------------------------------------------------------#
    parser = argparse.ArgumentParser()
    parser._optionals.title = "Arguments"
    parser.add_argument('--mode', dest='mode',
                        default='R',  # default empty!
                        help='Mode: R for random splitting, and N for the normal splitting')

    parser.add_argument('--ratio', dest='ratio',
                        default='0.5',
                        help='Ratio: the percentage of splitting. Decimal between 0 and 1')

    parser.add_argument('--skiplines', dest='skiplines',
                        default='0',
                        help='Skip n lines: the number of lines to skip in the input file')

    parser.add_argument('--input', dest='input',
                        default='',  # default empty!
                        help='Input file name')

    """
    Similar to Lab 2, please update the argument, and add as you need
    """
    # your code here
    if len(sys.argv) < 3:
        showHelper()
    main()
