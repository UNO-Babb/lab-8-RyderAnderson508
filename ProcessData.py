#ProcessData.py
#Name:Ryder Anderson
#Date:04/01/2025
#Assignment: Lab 08

import random

def main():

  #Open the files we will be using
  inFile = open("names.dat", 'r')
  outFile = open("StudentList.csv", 'w')

  #Process each line of the input file and output to the CSV file
  for line in inFile:
    data = line.split()
    first = data[0]
    last = data[1]
    IDNUM = data[3]
    student_id = makeID(first, last, IDNUM)
    output = data[0]
    outFile.write(output)


    print(student_id)
  
 

  #Close files in the end to save and ensure they are not damaged.
  inFile.close()
  outFile.close()

def makeID(first, last, IDNUM):
  print(first, last, IDNUM)
  idlen = len(IDNUM)

  while len(last) < 5:
    last = last + "X"
  id = first[0] + last + IDNUM[idlen - 3: ]
  print(id)

  return id 

if __name__ == '__main__':
  main()
