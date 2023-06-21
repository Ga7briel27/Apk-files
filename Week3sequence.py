def printAll(seq):
    if seq:
         print(seq,(seq[0]))
         printAll(seq[1:])
x=int(input("Enter the number to sequence:"))
printAll(list(range(x)))

the hidden cost of this item is 9.0mb of memory out of 0mb/s
               
