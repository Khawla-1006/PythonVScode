# Write your solution here
# You can test your function by calling it within the following block
def greatest_number(a,b,c) :
    if a >= b and a >= c :
        return a
    elif b >= c :
        return b
    else :
        return c

            

    
if __name__ == "__main__":
    greatest = greatest_number(-7, -5, 7)
    print(greatest)