class IOString():

    def __init__(self):
        self.str1 = ""

    def get_string(self):
        self.str1 = input("Enter word (in lower case letters) to change in Upper case letters : ")

    def print_String(self):
        print("The word with Upper Case Letters is : ",self.str1.upper())


str1 = IOString()

str1.get_string()
str1.print_String()