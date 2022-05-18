def searchname():
    infile = open("names.txt", "r")
    infile = str(infile)
    for s in infile:
        if s.endswith("5"):
            print(s)


searchname()
