# Evan Sauers & Daniel Rush
# Intro to Computer Science I
# Collabortaed with Dr. Neumann 
# lab9.py

#Take the word, turn it into a list, and create spaces inbetween letters
def sortString(word):
    word = word.lower()
    myList = list(word)
    myList.sort()
    sortedWord = " ".join(myList)
    return sortedWord


# Create a Dictionary, read the file
def createDictionary(fileName, dictionary):
    fileHandle = open(fileName, "r")
   
   # Strip and convert to lowercase
    for line in fileHandle:
        line = line.strip()
        word = line.lower()
        
        # Ask Question
        if word[0] == "v":
            sortedWord = sortString(word)
            dictionary[sortedWord] = word
    fileHandle.close()
    
    
# Find the Anagram in the dictionary, read the file, print
def findAnagrams(fileName, aDict):
    fileHandle = open(fileName, "r")
    
    #Strip the lines for the Anagram and convert to lowercase
    for line in fileHandle:
        line = line.strip()
        quizword = line.lower()
        print(quizword, aDict[sortString(quizword)])
    fileHandle.close()


# Define
def main():
    aDict = {}
    filename = 'wordList.txt'
    quizList = 'quizwords.txt'
    createDictionary(filename, aDict)
    findAnagrams(quizList, aDict)

main()

