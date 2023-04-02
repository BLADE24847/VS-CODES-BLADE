x = "Nvidia Geforce RTX 4090"
y = "Intel Core i9-13900KF"
z = "There are different opinions on which is the best monitor in the world however according to a source its the Dell Alienware AW3423DW"

user = input("You can ask me the names of the  best CPU GPU and monitor in the world, if you have any questions regarding the three asking me 'name the best' followed by one of the three CPU GPU or monitor--")

if user == "name the best CPU":
    print(y)
elif user == "name the best GPU":
    print(x)
elif user == "name the best monitor":
    print(z)
else:
    print("I dont know what that means, make sure you get the spelling same as what you are told")
