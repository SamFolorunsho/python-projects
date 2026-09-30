# define the function "hello" so you won't have to type multiple times
def hello():

    #Collect the user's name, remove whitespaces from the right and left sides and capitalize every first letter of the names 
    name = input("What's your name? ").strip().title()

    # seperate the fullname into the first name and the surname
    first, surname = name.split(" ")
    
    # Greet the user with hello on the screen coupled with his first name 
    print("hello,", first)




hello()