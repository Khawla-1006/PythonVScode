# Write your solution here
# Note, that at this time the main program should not be written inside
# if __name__ == "__main__":
# block!
def palindromes(string):
    while True : 
        string = input("Please type in a palindrome:")
        for x, y in zip(string, reversed(string)) :
            if x == y :
                print(string,"is a palindrome!")
                return
            else :
                print("that wasn't a palindrome")
                # continue

palindromes("python")