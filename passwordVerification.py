ActualPassword = 4567
attemptsCount = 3
for i in range(3):
     currentPassword = int(input())
     if currentPassword == actual_password:
         print("successfully logged in")
         break
else:
        if attemptsCount == 1:
            print("Your account blocked,try after 24 hrs")
        else:
            print("Incoorect password, you are left with",attemptsCount - 1,"attempts")
    attemptsCount -= 1
