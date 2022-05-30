# https://leetcode.com/problems/add-and-search-word-data-structure-design/

import re

class WordDictionary:

    def __init__(self):
        self.data = {}

    def addWord(self, word: str) -> None:
        length = len(word)
        if self.data.get(length) == None:
            self.data[length] = word.split()
        else:
            self.data.get(length).append(word)
            self.data[length] = self.data.get(length)
        print("added! ",self.data)

    def search(self, word: str) -> bool:
        print("search: ",word)
        length = len(word)
        lenlist = list(self.data.keys())
        for i in lenlist:
            print("i:", i)
            if i == length:
                wordlist = self.data[i]
                print("i==length", i)
                print("wordlist:", wordlist)
                if word in wordlist:
                    print("True1")
                    return True
                else:
                    for j in wordlist:
                        print("j:",j)
                        if re.compile(word).fullmatch(j):
                            print("True2")
                            return True
                    print("False1")
                    return False
        print("False2")
        return False


wd = WordDictionary()
wd.addWord('at')
wd.addWord('and')
wd.addWord('an')
wd.addWord('add')

wd.search('a')
wd.search('.at')

wd.addWord('bat')

wd.search('.at')
wd.search('an.')
wd.search('a.d.')
wd.search('b.')
wd.search('a.d')
wd.search('.')
