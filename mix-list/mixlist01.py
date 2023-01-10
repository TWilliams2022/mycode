#!/usr/bin/env python3

my_list = [ "192.168.0.5", 5060, "UP" ]
# index      0             1      2 
print("The first item in the list (IP): " + my_list[0] )

print("The second item in the list (port): " + str(my_list[1]) )

print("The last item in the list (state): " + my_list[2] )


iplist = [ 5060, "80", 55, "10.0.0.1", "10.20.30.1", "ssh" ]

print("only ip addresses " + iplist[3])

print("2nd ip address " + iplist[4])



# exercise 31
import random
def main():
wordbank= ["indentation", "spaces"]
wordbank.append(4)
num= int( input("Pick a student number between 1 and {len(tlgstudents)} !"))-1
name= tlgstudent[num]
print("You picked: " + num)
print(wordbank)


tlgstudents= ['Albert', 'Anthony', 'Brenden', 'Craig', 'Deja', 'Elihu', 'Eric', 'Giovanni', 'James', 'Joshua', 'Maria', 'Mohamed', 'PJ', 'Philip', 'Sagan', 'Suchit', 'Meka', 'Trey', 'Winton', 'Xiuxiang', 'Yaping']

print(tlgstudents)

  name2 = random.choice(tlgstudents)
    print(f"{name2}")



main()

