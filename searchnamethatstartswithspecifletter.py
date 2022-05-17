def searchnamee():
    w = input("Enter any letter : ").title()
    infile = open("names.txt", "r")
    for s in infile:
        if s.startswith(w):
            print(s)


searchnamee()