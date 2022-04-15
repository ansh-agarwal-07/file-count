def countwordsfromfiles():
    filename = input ( "enter the file name" )
    wordcount = 0

    file = open(filename,'r')
    for line in file:
        words = line.split(" ")
        wordcount = wordcount + len(words)
        print(words)
    print("number of words " )
    print(wordcount)
  

countwordsfromfiles()







