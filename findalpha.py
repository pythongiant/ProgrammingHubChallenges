first_occur = 0
counter = 0
string = input("Enter a String:")
alpha = input("Enter the alphabet to be searched:")
lString = list(string)

for i in range(len(string)):
    if lString[i] == alpha:
        counter += 1
    if counter == 1:
        first_occur = i

if counter == 0:
    print("not present")
else:

    print("Position of first occurrence:" + str(first_occur-2))
    print("Number of occurrence:"+str(counter))

