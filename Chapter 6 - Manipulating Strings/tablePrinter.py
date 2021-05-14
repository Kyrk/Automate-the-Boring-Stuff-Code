#!/usr/bin/env python3
# Program with a function that takes a list of lists of strings and displays it
# in a well-organized table with each column right-justified.
# Assumes all inner lists will contain the same number of strings.
def printTable(table):
    longestString = 0   # Store size of longest string
    listSize = len(table[0])    # Get size of inner list

    # Get longest string in table
    for tableList in table:
        for item in tableList:
            if len(item) > longestString:
                longestString = len(item)

    # Print inverted table row by row with right-justified columns using the
    # size of longestString
    for i in range(listSize):
        tableString = ""    # Empty string at beginning of loop
        # Add right-justified values of each list at current index to
        # tableString
        for tableList in table:
            tableString += tableList[i].rjust(longestString)
        print(tableString)

tableData = [['apples', 'oranges', 'cherries', 'banana'],
        ['Alice', 'Bob', 'Carol', 'David'],
        ['dogs', 'cats', 'moose', 'goose']]

printTable(tableData)
