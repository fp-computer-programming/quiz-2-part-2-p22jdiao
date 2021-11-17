# Author: JD 11/17/2021

ans = input("A possitive statement? ")
ans = ans.lower()
word = ans.find("not")

if word == -1:
    print("You are not {0}. Now SCRAM!".format(ans))
elif word != -1 and ans != "not":
    print("Yes! You are {0}, woohooo!".format(ans))
elif word != -1 and ans == "not":
    print("Don't just say {0} to me, say something possitive!".format(ans))
