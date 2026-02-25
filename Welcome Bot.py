'''
Welcome Bot Simulator with Lists

Write a function welcome_bot() that simulates a chatbot introduction using a Python list. The function should store the words of a welcome message in a list, print the first three words, then re-initialize the list to a larger size and print the first element again.

Requirements

    Store the words:
    "Hello", "world,", "I","am", "learning", "Python!" in a list.

    Print only the first three words (each on a new line).

    Re-initialize the list to a size of 10 (filled with None).

    Print the first element of the new list (should be None).
'''

def welcome_bot():
    # Step 1: Create a list of size 6
    BOT_LIST = []
    # Step 2: Store each word of the message "Hello world, I am learning Python!" into the list
    BOT_LIST = ["Hello", "world,", "I","am", "learning", "Python!"]
    # Step 3: Print only the first 3 words ("Hello" , "world," , "I")
    print (BOT_LIST[0])
    print (BOT_LIST[1])
    print (BOT_LIST[2])
    # Step 4: Reassign the list to a new size of 10 (filled with None)
    BOT_LIST =  [None] * 10
    # Step 5: Try printing words[0] again and observe what happens
    print (BOT_LIST[0])
    pass

welcome_bot()
