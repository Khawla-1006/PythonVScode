# Write your solution here
my_word = []
occurence = 1
while True :
    word = input("Word: ")
    my_word.append(word)
    if word in my_word[0 : len(my_word) - 1] :
            occurence += 1 
    if occurence == 2 :
        break
print("You typed in", len(my_word)-1,"different words")
