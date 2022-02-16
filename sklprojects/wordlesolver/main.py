import random, solver

#task 2
def importwords():
    word_list = []
    with open("WordleList.txt", 'r') as f:
      for lines in f:
        lines.strip("\n")
        word_list.append(lines)
    return word_list

def input_guess(prompt):
    my_input = solver.Solve()
    if my_input == None: return "     " # if you press cancel or submit with nothing
    elif len(my_input) != 5: return my_input[0:5] #sends the first five characters
    else: return my_input.lower() #sends lower case of the word. Means case does not make a difference.

def check_guess(my_input,answer):
    count = 0 #Need a count, because of for loop used
    colourting = ""
    for i in range(len(my_input)):
        if my_input[i] == answer[count]: 
          colourting += "🟩"
        elif my_input[i] in answer: 
          colourting += "🟨"
        else: 
          colourting += "🟥" # otherwise draws red
        count+=1 # add 1 to the count
    return colourting


if __name__ == "__main__":
    word_list = importwords()
    answer = random.choice(word_list) # choose a random word from the list
    print(answer)
    for i in range(6): #Where the program starts
        guess_prompt = "What is your guess?" #Makes a nice string for the prompt
        my_input = input_guess(guess_prompt) #calls input_guess function
        print(my_input)
        c = check_guess(my_input,answer)
        print(c)
        solver.TakeInput(my_input, c)#checks the guess
        if my_input in answer:
            print("hell yeah you got it")
            break

        
    else: #Only runs if the for loop executes completely. i.e. You've used all your guesses.
        print(answer)
