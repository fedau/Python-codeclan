
#SET is_it_raining = INPUT is it raining
#IF is_it_raining is "yes"
# print("you should take car")
#ELSE 
#   IF distance < 5
#       THEn PRINT "you should walk"
#   ELSE 
#       THEN PRINT "you hsould get the bus"
#end
distance = 3
is_it_raining = input("is it raining? ")

if is_it_raining == "yes":
   print("you should take car") 
elif distance < 5:
    print("you should walk")
else:
    print("you should take the bus")