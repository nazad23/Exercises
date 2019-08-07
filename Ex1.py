# There is a file containing a word and its possible meanings (like a dictionary). The contents of the file
# look like this: Apple - a fruit, a tech firm. Table - an object, contains rows and columns when used in context of
# computers. Orange - a fruit.
#
# Given a path to the file, do the following:
# a) Create a method call doesFileExist(String path) which takes the path of the file and tells the user if the file
# exists at that path or not. Assume all paths are relative to your project structure. If the file does not exist, catch
# the requisite exception.
#
# b) Read out each word and its possible meanings and print them out. Your output should look like this:
# Word1
# Meaning 1
# Meaning 2
# Word2
# Meaning 1
# Meaning 2
#
# User appropriate data structures wherever necessary
import re
import os.path

class Example1():
    def __init__(self, filePath):
        self.filePath = filePath

    def doesFileExist(self, path):
        return os.path.exists(path)

    def readFileContent(self):
        if self.doesFileExist(self.filePath):
            print("File exists\n")
            with open(self.filePath) as file:
                for sentence in file.readlines():
                    words = re.split(', | -', sentence)
                    for word in words:
                        print(word.strip())
        else:
            raise FileExistsError(str(self.filePath) + " : file doesn't exist.")

if __name__ == '__main__':
    Example = Example1('local_dict.txt')
    try:
        Example.readFileContent()
    except FileExistsError as e:
        print(str(e))


