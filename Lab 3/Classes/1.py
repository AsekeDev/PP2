class string_methods:
    def __init__(self):
        self.text = ""
    def getString(self):
        self.text = input()
    def printString(self):
        print(self.text.upper())

string = string_methods()
string.getString()
string.printString()