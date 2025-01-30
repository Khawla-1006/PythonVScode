# Write your solution here
# Note, that at this time the main program should not be written inside
# if __name__ == "__main__":
# block!
def palindromes(string):
    status = False

    while True : 
        string = input("Please type in a palindrome:")
        for i in range(len(string)//2):
            if string[i] == string[-(i + 1)] :
                status = True
        if status == True :
            print(string,"is a palindrome") 
            return
        else :
            print("that is not a palindrome!")

palindromes("khawla")