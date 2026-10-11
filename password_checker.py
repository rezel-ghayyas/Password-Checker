while True:
    password = input("Enter your password : ")

    while len(password) <8:
            print("PASSWORD MUST BE AT LEAST 8 CHARACTERS LONG!")
            password = input("Enter your password : ")

    has_letter = False 
    has_number = False 
    has_symbol = False 

    for character in password:
        if character.isalpha():
            has_letter = True
        if character.isdigit():
            has_number = True
        if not character.isalnum():
            has_symbol = True

    if has_letter and has_number and has_symbol:
        print("YOUR PASSWORD IS STRONG") 
    else:
        print("YOUR PASSWORD IS WEAK")

