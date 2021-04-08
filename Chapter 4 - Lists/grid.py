#!/usr/bin/env python3
"""
Program that prints image from a list by list data structure
"""
grid = [['.','.','.','.','.','.'],
    ['.','O','O','.','.','.'],
    ['O','O','O','O','.','.'],
    ['O','O','O','O','O','.'],
    ['.','O','O','O','O','O'],
    ['O','O','O','O','O','.'],
    ['O','O','O','O','.','.'],
    ['.','O','O','.','.','.'],
    ['.','.','.','.','.','.']]

for x in range(len(grid[0])):
    for y in range(len(grid)):
        print(grid[y][x], end='')
    print()
