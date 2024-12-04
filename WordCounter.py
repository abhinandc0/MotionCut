#Function to count words in the input
def count_words(text):
    #Spit words at whitespaces and create a list
    words = text.split()
    #count elements in the list
    return len(words)

def main():
    #get input from the user
    text = input("Enter sentence or paragraph to count words: ")
    #checks if the input is empty
    if not text.strip():
        print("Error! Input cannot be empty..!")
        return
    #counts the number of words
    word_count = count_words(text)

    #print the word count
    print(f"The input has {word_count} words in it.")


#Initiates the funtion with function call
if __name__ == "__main__":
    main()