#Initialize an empty list of users info
users_info = []
while True:
   user_name = input("Enter your name: ")
   #Use while not, to repeat task until condition is met
   #for user name
   while not (user_name.isalpha() and len(user_name) >= 2): #only accepts alphabet and atleast more than 2 characters long
      print("Not a valid name. Enter a name that only contains alpahabet and atleast 2 letters long.")
      user_name = input("Enter your name: ")
   #for user age
   user_age = int(input("Enter your age: "))  
   while not ((user_age.is_integer()) and 0 <= int(user_age) <= 150):#only accepts integer between 0-150 
      print("Not a valid age. Enter Age between 0 and 150.")
      user_age = int(input("Enter your age: "))
   #stores the info in the list  
   users_info.append({"Name": user_name, "Age": int(user_age)})

