#!/user/bin/python

# copyright liangxy8@bu.edu
# copyright tysun@bu.edu
# copyright joeyang@bu.edu


from sys import argv
import copy
import re
#import numpy as np

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

    def check(self, word):
        """
        Return if the prefix is in the trie
        """
        curNode = self.root
        for c in word:
            if not c in curNode:
                return False
            curNode = curNode[c]
        return True


def overflow(x, y):
    if x < 0 or x >= LENGTH or y < 0 or y >= LENGTH:
        return False
    else:
        return True


def find_word(puzzle, i, j, star):
    for x in [-1, 0, 1]:
        for y in [-1, 0, 1]:
            if overflow(x+i, y+j) and [x+i, y+j] not in trace and puzzle[x+i][y+j] != None:
                Q = ''.join(a_word)
                if trie.check(Q):
                    a_word.append(puzzle[x+i][y+j])
                    trace.append([x+i, y+j])
                    if len(a_word) < len(star):
                        find_word(puzzle, x+i, y+j, star)
                    elif len(a_word) == len(star):
                        if re.match(star.replace('*', '[a-z]'), ''.join(a_word)) is not None:
                            words.append(tuple(a_word))
                            traces.append(tuple(trace))
                            del a_word[-1]
                            del trace[-1]

    del trace[-1]
    del a_word[-1]
    return words, traces


def update_position(old_grid, delete_word_trace):
    grid_copy = copy.deepcopy(old_grid)

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

            # Find the first non_empty element above the None element, and replace it
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




def find_all_case(letter, puzzle):
    all_case = []
    all_trace = []
    for i in range(LENGTH):
        for j in range(LENGTH):
            if puzzle[i][j] != None:
                global trace
                trace = [[i, j]]
                global words
                words = []
                global traces
                traces = []
                global a_word
                a_word = [puzzle[i][j]]
                words, traces = find_word(puzzle, i, j, letter)
                for m in words:
                    all_case.append(list(m))
                for m in traces:
                    all_trace.append(m)

    # Find all possible solutions according to first*** and update grid
    global k
    k = k+1
    for n in range(len(all_case)):
        Q = ''.join(all_case[n])
        if trie.search(Q):
            solution.append(Q)
            new_grid = update_position(puzzle, all_trace[n])
            if k < len(star):
                find_all_case(star[k], new_grid)
            elif k == len(star):
                all_solution.append(tuple(solution))
                del solution[-1]
    try:
        del solution[-1]
    except IndexError:
        pass
    k = k-1



if __name__ == '__main__':

    # Read word_list and insert all words in Trie
    GRID = []
    while True:
        try:
            A = input("")
        except EOFError:
            break
        if "*" in A:
            GRID.append(A)

            try:
                for index in [1, 2]:
                    trie = Trie()
                    TEXT = argv[index]
                    WORDS_LIST = open(TEXT).read().splitlines()
                    for i in range(len(WORDS_LIST)):
                        trie.insert(WORDS_LIST[i])

                    LENGTH = len(GRID[0])
                    star = GRID[-1].split()

                    k = 0
                    solution = []
                    trace = []
                    a_word = []
                    words = []
                    traces = []
                    all_solution = []
                    find_all_case(star[k], GRID)
                    if all_solution != []:
                        for i in sorted(set(all_solution)):
                            print(' '.join(i))
                        break
                print('.')
            except IndexError:
                break
            GRID = []
        else:
             GRID.append(list(A))
