class string_methods:
    def getstring(self):
        self.string=input("Your string:")
    def printstring(self):
        print("Print with uppercase" + self.string.upper())
str = string_methods()
str.getstring()
str.printstring()