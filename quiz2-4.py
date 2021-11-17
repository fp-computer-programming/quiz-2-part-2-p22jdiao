# Author: JD 11/17/2021

comm1 = input("Enter  the first instruction: ")

comm2 = input("Enter the second instruction: ")

comm1 = comm1. split()
c1_u = comm1.copy()
comm2 = comm2. split()
c2_u = comm2.copy()

north1 = comm1.index("north")
if north1 != -1:
    c1_u[north1] = 1
south1 = comm1.index("south")
if south1 != -1:
    c1_u[south1] = 3
west1 = comm1.index("west")
if west1 != -1:
    c1_u[west1] = 4
east1 = comm1.index("east")
if east1 != -1:
    c1_u[east1] = 2

north2 = comm2.index("north")
if north2 != -1:
    c2_u[north2] = 1
south2= comm2.index("south")
if south2 != -1:
    c2_u[south2] = 3
west2 = comm2.index("west")
if west2 != -1:
    c2_u[west2] = 4
east2 = comm2.index("east")
if east1 != -1:
    c2_u[east2] = 2
comm1.extend(comm2)
c1_u.extend(c2_u)
print("In order to have the robot move {0}, give it this sequence, {1}".format(comm1,c1_u))

