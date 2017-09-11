from collections import Counter
import string

class User:
    def __init__(self, name, msgList):
        self.messageList = msgList
        self.name = name
        self.init_word_stats()

    def init_word_stats(self):
        self.wordList = []
        self.wordLinesList = []
        for element in self.messageList:
            split = [x.translate(str.maketrans('', '', string.punctuation)).lower() for x in element.split()] # removes punctuation
            self.wordList += split
            self.wordLinesList.append(split)
        self.init_word_map()
        self.init_character_stats()

    def init_character_stats(self):
        self.characterList = []
        for element in self.wordList:
            self.characterList += list(element)
        self.init_character_map()

    def init_word_map(self):
        self.wordMap = Counter(self.wordList)

    def init_character_map(self):
        self.characterMap = Counter(self.characterList)

    def compare(self, other):
        return (len(self.messageList) / len(other.messageList), len(self.wordList) / len(other.wordList), len(self.characterList) / len(other.characterList))

    def compare_pretty(self, other):
        result = self.compare(other)
        return self.name + " sends " + str(result[0]) + " times as many messages, " + str(result[1]) + " times as many words, and " + str(result[2]) + " times as many characters as " + other.name

    def verbose(self):
        return self.__str__() + "\nWord frequency: " + str(self.wordMap) + "\nCharacter frequency: " + str(self.characterMap)

    def __str__(self):
        return (self.name + " has sent " + str(len(self.messageList)) + " messages, " + str(len(self.wordList)) + " words, and " + str(len(self.characterList)) + " characters")