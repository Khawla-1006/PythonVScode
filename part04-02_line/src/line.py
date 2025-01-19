# Write your solution here
# You can test your function by calling it within the following block
def line(number, string) : 
    if string == "" : 
        print("*" * number)
    else :
        print(string[0] * number)
if __name__ == "__main__":
    line(5, "x")