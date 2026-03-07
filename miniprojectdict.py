'''Create a program that manages a dictionary of word meanings. The program should allow users to perform the following actions:
1.Add a Word: Allow users to add new words along with their meanings to the dictionary.
2. Search for Meaning: Enable users to search for the meaning of a word in the dictionary.
3.Display All Words: Provide an option to display all words and their meanings currently stored in the dictionary.
4.Update Meaning: Implement a feature to update the meaning of an existing word in the dictionary. After updating, display the updated meaning.
5.Delete Word: Implement a feature to delete a word and its meaning from the dictionary. Confirm the deletion and handle cases where the word doesn't exist.
Ensure the program handles invalid inputs gracefully. Use a while loop to keep the program running until the user chooses to exit'''
dict={}

while True:
    print("\n Dictionary Management System")
    print("1.Add a Word")
    print("2.Search for the word meaning")
    print("3.Display all the words")
    print("4.Update meaning")
    print("5.Delete the word")
    print("6.Exit")

    choice=input("Enter your choice:")

    if choice =="1":
        word = input("Enter the word:").lower()
        meaning = input("Enter the meaning of the word:")
        dict[word]=meaning
        print("word entered successfully")

    elif choice =="2":
        word = input("Enter the word to search:").lower()
        if word in dict:
            print("meaning:",dict.get(word))
        else:
            print("word not found in dict")

    elif choice =="3":
        if dict:
            print("words and their meanings:")
            for word,meaning in dict.items():
                print(f"{word}:{meaning}")
        else:
            print("Dict is empty")

    elif choice =="4":
        meaning=input("Enter the word for the new meaning to update:").lower()
        if word in dict:
            new_meaning=input("Enter the new meaning for the word:")
            dict[word]=new_meaning
            print("new meaning updated successfully")
            print(f"updated meaning:{new_meaning}")
            
        else:
            print("word not found")

    elif choice =="5":
        word=input("Enter the word to delete:")
        if word in dict:
            dict.pop(word)
            print("word deleted successfully!")
        else:
            print("word not found")

    elif choice =="6":
        print("Exiting the program ")
        break

    else:
        print("Invalid choice!please enter valid option")
        

    

               

    


       


 

