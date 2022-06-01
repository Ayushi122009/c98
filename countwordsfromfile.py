def countwordsfromfile():
  filename=  input("Give your file name : ")
  numberofwords = 0
  file= open(filename, "r")
  for line in file:
      words= line.split()
      numberofwords= numberofwords+len(words)
  print("Number of Words: ", numberofwords)

countwordsfromfile()
