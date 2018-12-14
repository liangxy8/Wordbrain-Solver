#!/user/bin/python

import numpy as np
from collections import Counter
import sys
from sys import argv


class Trie:
    
    def __init__(self):
        """
        Initialize your data structure here
        """
        self.root = {}
        self.word_end = -1
    
    def insert(self, word):
        """
        Insert a word into the trie
        """
        curNode = self.root
        for c in word:
            if not c in curNode:
                curNode[c] = {}
            curNode = curNode[c]

        curNode[self.word_end] = True
    
    def search(self, word):
        """
        Returns if the word is in the trie
        """
        curNode = self.root
        for c in word:
            if not c in curNode:
                return False
            curNode = curNode[c]
        if self.word_end not in curNode:
            return False
        return True


def overflow(x, y):
    if x < 0 or x >= LENGTH or y < 0 or y >= LENGTH:
        return False
    else:
        return True  


def find_word(grid, i, j, n_star ):
    for x in [-1, 0, 1]:
        for y in [-1, 0, 1]:
            if overflow(x+i, y+j) and [x+i,y+j] not in trace:
                a.append(grid[x+i][y+j])
                trace.append([x+i,y+j])
                if len(a) < n_star:
                    find_word(grid, x+i, y+j, len(star[0]))
                elif len(a) == n_star:
                    b.append(tuple(a))
                    traces.append(tuple(trace))
                    del a[-1]
                    del trace[-1]
    del trace[-1]
    del a[-1]
    return b, traces


def update_position(grid, delete_word_trace):
    grid_copy = grid
    for i in delete_word_trace:
        a = int(i[0])
        b = int(i[1])
        grid_copy[a][b] = None

    column = []
    for i in delete_word_trace:
        column.append(int(i[1])) 
    # Find the first None element:column[a][b] in b column
    for b in set(column):
        a = LENGTH-1
        while grid_copy[a][b] != None:
            a = a-1
        
        while True:
            FLAG = a-1
            # find the first non_empty element above the None element, and replace it
            if a > 0:
                while grid_copy[FLAG][b] == None:
                    FLAG = FLAG-1
                if FLAG >= 0:
                    grid_copy[a][b] = grid_copy[FLAG][b]
                    grid_copy[FLAG][b] = None
                    a = a-1
                else:
                    break
            else:
                break
    return grid_copy
            





if __name__ == '__main__':
    
    # Read word_list and insert all words in Trie 
    trie = Trie()
    TEXT = sys.argv[1]
    WORDS_LIST = open(TEXT).read().splitlines()
    for i in range(len(WORDS_LIST)):
        trie.insert(WORDS_LIST[i])


    # Initialize grid
    grid = sys.stdin.read().splitlines()
    star = grid[-1].split()
    LENGTH = len(grid[0])
    for i in range(LENGTH):
        grid[i] = list(grid[i])

    
#def find_all_case(len_star, gird):

    # Find all possible trace and case according to the first***
    all_case = []
    all_trace = []
    for i in range(LENGTH):
        for j in range(LENGTH):
            trace = [[i,j]]
            b = []
            traces = []
            a = [grid[i][j]]
            b, traces = find_word(grid, i, j, len(star[0]) )
            print("b is:",b)
            print("traces is:",traces)
            for m in b:
                all_case.append(list(m))
            for m in traces:
                all_trace.append(m)

    
    # Find all possible solutions according to first*** and update grid
    for n in range(len(all_case)):
        q = ''.join(all_case[n])
        #if trie.search(q):
            #new_grid = update_position(grid, all_trace[n])

    
    
    
    
    n = 48
    new_grid = update_position(grid, all_trace[n])
    print(new_grid)
    #new_grid = update_position(grid, all_trace[1200])
    #print(new_grid)
