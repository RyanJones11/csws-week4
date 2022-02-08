usernames = ["Bill", "Joel", "Tommy", "Sam", "admin"]
print("Please enter your username: \n")
username = input()
i =0
for i in range(len(usernames)):
    if usernames[i] == "admin":
        print("Hello Admin, would you like to see a report?")
    else:
        print("Hello, "+ usernames[i] + " thank you for logging in.")