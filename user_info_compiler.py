#Initialize an empty list of users info
users_info = []
while True:
   user_name = input("Enter your name: ").title()
   #Use while not, to repeat task until condition is met
   #for user name
   while not (user_name.isalpha() and len(user_name) >= 2): #only accepts alphabet and atleast more than 2 characters long
      print("Not a valid name. Enter a name that only contains alpahabet and atleast 2 letters long.")
      user_name = input("Enter your name: ").title()

   #for user age
   while True:
      try:
         user_age = int(input("Enter your age: "))  
         if 0 <= int(user_age) <= 150: #only accepts integer between 0-150
            print(f"{'-'* 50}\nUser information:\nName:{user_name} \nAge: {user_age}\n{'-'* 50}")
            break
         else:
            print("Not a valid age. Enter Age between 0 and 150.")
      except ValueError: #for the program to not stop when a string is entered
         print("Not a valid age. Enter Age between 0 and 150.")

   #stores the info in the list  
   users_info.append({"Name": user_name, "Age": int(user_age)})
   
   #ask the user if they want to input another entry
   new_user_entry = input("Up for another entry (yes/no) ? ")
      #set a condition using if statements
   if new_user_entry == "no":
      break
   while new_user_entry != "yes":
      print("Invalid answer.")
      new_user_entry = input("Up for another entry (yes/no) ? ")
   
#when user do not want to continue, it will display the oldest person 
if users_info:
   oldest_user = max(users_info, key=lambda user: user["Age"])
print(f"{'-'* 50}\nOldest user: \nName: {oldest_user['Name']}\nAge: {oldest_user['Age']}\n{'-'* 50}")