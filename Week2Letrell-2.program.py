'Week2Part1Assignment'
'AuthorLetrellHodge'
#Open the input file
#Read the date
#Print the report without duplicate records
def grade(percent):
    grd=''
    if percent>=90:
       grd='A'
    elif percent>=80:
      grd='B'
    elif percent>=70:
        grd='C'
    elif percent>=60:
        grd='D'
    else:
        grd='F'
    return grd
filename=input("Enter the name of the file:")
#Enter the file name
f=open(filename,'r')#Open the file
lines=[]#Create an empty list
for line in f:#loop through the lines in the text file
    words =f.readlines()#.split()
    for word in words:
      if not word in lines:
         lines.append(word)#append the lines to the list
#lines.sort()
for word in lines:
    sp=word.split()
#<student id> <last name> <total score> <letter grade>
    print(sp[0], sp[1], int(sp[2])+ int(sp[3])+ int(sp[4]), grade(int(sp[2])+ int(sp[3])+ int(sp[4])))
f.close
 
