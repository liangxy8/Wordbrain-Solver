#!/user/bin/python
import numpy as np
from sys import argv


import copy
import re

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


def find_word(puzzle, i, j, star ):
    for x in [-1, 0, 1]:
        for y in [-1, 0, 1]:
            if overflow(x+i, y+j) and [x+i,y+j] not in trace and puzzle[x+i][y+j] != None:
                q = ''.join(a_word)
                if trie.check(q):
                    a_word.append(puzzle[x+i][y+j])
                    trace.append([x+i,y+j])
                    if len(a_word) < len(star):
                        find_word(puzzle, x+i, y+j, star)
                    elif len(a_word) == len(star):
                        #print("{}??{}".format(star_, a_word))
                        #if ''.join(a_word) == 'holly':
                        #    print("hehehe  {}".format("holly shit"))
                        if re.match(star.replace('*', '[a-z]'), ''.join(a_word)) is not None:
                            words.append(tuple(a_word))
                            traces.append(tuple(trace))
                            del a_word[-1]
                            del trace[-1]

    #print(words)
    #print("a_word is:", a_word)
    del trace[-1]
    del a_word[-1]
    return words, traces


def update_position(old_grid, delete_word_trace):
    #print('old_grid shape[0] is:{},shape[1] is:{}'.format(old_grid.shape[0], old_grid.shape[1]))
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
            


#def update_position(matrix):
#    '''Drop the used letters in the matrix'''
#    matrix = np.array(matrix)
#    result = np.copy(matrix)
#    previous = [None] * matrix.shape[0]
#    for j in range(0, matrix.shape[1]):
#        temp_mat = np.array(previous)
#        index = matrix.shape[0] - 1
#        for i in range(matrix.shape[0] - 1, -1, -1):
#            if result[i][j] != None:
#                temp_mat[index] = result[i][j]
#                index = index - 1
#        result[:, j] = temp_mat
#    return result
#


def find_all_case(letter, puzzle):
    # Find all possible trace and case according to the first***
    #case = []
    #for i in letter:
    #    if i != '*':
    #        case.append(i)
    #q = ''.join(case)

    #print(letter)
    all_case = []
    all_trace = []
    for i in range(LENGTH):
        for j in range(LENGTH):
            if puzzle[i][j] != None:
                global trace
                trace = [[i,j]]
                global words
                words = []
                global traces
                traces = []
                global a_word
                a_word = [puzzle[i][j]]
                
                words, traces = find_word(puzzle, i, j, letter)
                #print(words)
                #print("b is:",b)
                #print("traces is:",traces)
                for m in words:
                    all_case.append(list(m))
                for m in traces:
                    all_trace.append(m)
    #print(all_case)
    # Find all possible solutions according to first*** and update grid
    global k
    k = k+1
    for n in range(len(all_case)):
        q = ''.join(all_case[n])
        if trie.search(q):
            #print("hehe",k)
            solution.append(q)
            #print("q is:",q)
            #print("{} 用于更新位置的grid: {}".format(ii, puzzle))
            
            new_grid = update_position(puzzle, all_trace[n])
            #new_grid = update_position(puzzle)

            #print("new_grid is:",new_grid)
            if k < len(star):
               # print("进入递归")
                find_all_case(star[k], new_grid)
            elif k == len(star):
                #print(solution)
                all_solution.append(tuple(solution))
                del solution[-1]
    #print("循环外（前）",solution)
    try:
        del solution[-1]
    except IndexError:
        pass
    k = k-1
    #print("循环外（后）",solution)



    
    
if __name__ == '__main__':

    # Read word_list and insert all words in Trie
    grids = []
    while True:
        try:
            a = input()
            grids.append(a)
            if a == '':
                break
        except EOFError:
            break

    del grids[-1]

    num = 0
    while True:
        try:
            num_ = num
            for index in [1, 2]:
                num = num_
                trie = Trie()
                TEXT = argv[index]
                WORDS_LIST = open(TEXT).read().splitlines()
                for i in range(len(WORDS_LIST)):
                    trie.insert(WORDS_LIST[i])

                #grids = sys.stdin.read().splitlines()
                #print("grids is:",grids)
                # Initialize grid
                #print("num is:",num)
                LENGTH = len(grids[num])
                star = grids[LENGTH+num].split()
                grid = []
                for i in range(LENGTH+1):
                    grid.append(list(grids[num+i]))
                #print("grid is:",grid)
                num = num + LENGTH + 1

                #print(grid)

                k = 0
                solution = []
                trace = []
                a_word = []
                words = []
                traces = []
                all_solution = []
                
                find_all_case(star[k], grid)
                if all_solution != []:
                    for i in sorted(set(all_solution)):
                        print(' '.join(i))
                    print(".")
                    break
        except IndexError:
            break

    
    
    
    
   # while exit:
   #     for TEXT in sys.argv[1:]:
   #         # Read word_list and insert all words in Trie
   #         WORDS_LIST = open(TEXT).read().splitlines()
   #         for i in range(len(WORDS_LIST)):
   #             trie.insert(WORDS_LIST[i])


   #         # Initialize grid
   #         grid = sys.stdin.read().splitlines()
   #         if grid == '\n':
   #             exit = True
   #             break
   #         star = grid[-1].split()
   #         LENGTH = len(grid[0])
   #         for i in range(LENGTH):
   #             grid[i] = list(grid[i])

   #         k = 0
   #         solution = []
   #         trace = []
   #         a_word = []
   #         words = []
   #         traces = []
   #         all_solution = []
   #         find_all_case(len(star[k]), grid)
   #         if len(all_solution) != 0:
   #             exit = False
   #             break
   #     for i in sorted(set(all_solution)):
   #         print(' '.join(i))
   #     print(".")

