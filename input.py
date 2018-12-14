 Small_Trie = Trie()
    Large_Trie = Trie()
    FINAL = set()

    TEXT1 = sys.argv[1]
    WORDS_LIST1 = open(TEXT1).read().splitlines()
    for i in range(len(WORDS_LIST1)):
        Small_Trie.insert(WORDS_LIST1[i])

    TEXT2 = sys.argv[2]
    WORDS_LIST2 = open(TEXT2).read().splitlines()
    for i in range(len(WORDS_LIST2)):
        Large_Trie.insert(WORDS_LIST2[i])
