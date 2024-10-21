#Initialize an empty list of users info
users_info = []
while True:
   user_name = input("Enter your name: ")
   #Use while not, to repeat task until condition is met
   while not (user_name.isalpha() and len(user_name) >= 2): #only accepts alphabet and atleast more that 2 characters long
      print("Not a valid name. Enter a name that only contains alpahabet and atleast 2 letters long.")
      user_name = input("Enter your name: ")
      break     
