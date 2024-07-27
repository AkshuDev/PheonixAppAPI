#Made by Aarav Nayak -- This is a calculator idk why but heres the code for it
#note:: this is a utility, if you wanna add it in Minigame do it or make a new comand for Utilities
#This is a general utilities program
#This has a calculator, Wikipedia and more to come
# try to add this to the pheonix app cuz why not
#Anyways developed by pheonix community
import math
import wikipedia
import math
import os
import sys

mainDIR = os.path.dirname(os.path.abspath(__file__))

if __name__ == "__main__":
    os.chdir(mainDIR)
    sys.path.append(mainDIR)

from PheonixAppAPI.pheonixapp.files import LIB
from PheonixAppAPI.pheonixapp.files import PSSbridge

class LINE():
    def __init__(self, line:str) -> None:
        self.line = line

    def compile_v0_1(self):
        os.system(f"set /a {self.line}")
        print("\n")

# Calculator
def calculator():
    Operation = input("Hello, what operation would you like to perform today?\n1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n5.Sqaure ROOT\n6.Sqaure\n7. Line\n(Enter the number of the operation you want to perform): " )

    #Addition
    if Operation == "1":
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        sum = int(num1 + num2)
        print("The sum is",sum)
        return None
    #Subtraction
    elif Operation == "2":
        num1S = int(input("Enter the first number: "))
        num2S = int(input("Enter the second number: "))
        if num1S > num2S:
            difference = int(num1S - num2S)
            print("The difference is",difference)
            return None
        else:
            print("ERROR, number 1 is bigger than number 2\nERROR code [PEC002]")
            return None

    #Multiplication
    elif Operation == "3":
        num1M = int(input("Enter the first number: "))
        num2M = int(input("Enter the second number: "))
        product = int(num1M * num2M)
        print("The product is", product)
        return None

    #Division
    elif Operation == "4":
        num1D = int(input("Enter the first number: "))
        num2D = int(input("Enter the second number: "))
        if num1D > num2D:
            division = int(num1D / num2D)
            print("The division is", division)
            return None
        else:
            print("ERROR, number 1 is bigger than number 2\nERROR code [PEC004]")
            return None

    #Spuare root
    elif Operation == "5":
        num1R = int(input("Enter the number: "))
        if num1R < int(0):
            print("ERROR, number must be greater or equal to 0\nERROR code [PEC005]")
            return None
        else:
            root = math.sqrt(num1R)
            print("The Square root is", root)
            return None

    #Square
    elif Operation == "6":
        num1SQR = int(input("Enter the number: "))
        square = int(num1SQR)*int(num1SQR)
        print("The square is", square)
        return None

    elif Operation == "7":
        line = input(f"{os.getcwd()}->\nCALC $> ")
        LINE(line).compile_v0_1()

    #Exception error message
    else:
        print("Unsuported Operation\nERROR CODE [PECuc001]")
        return None


#This is a wikipedia search thingy
#Made by Aarav Nayak (CO - Founder)

def wikipediasearch():
    query = input(f"{os.getcwd()}->\nWIKI $> ")
    print(wikipedia.search(query)+"\n")

def api_wiki_search(search):
    return wikipedia.search(search)