# #Global varibales
# x='stupid'

# def test_global():
#     global x
#     x="fantastic"
#     print("Python is %s" %(x))    

# test_global()

# print("Python is %s" %(x))

# #check the data type of a variable
# x=5
# print(type (x))

# #Create a tuple
# check_tuple=("mike","shina","tolu","jide")

# print(type(check_tuple))
# print(check_tuple)
# print(check_tuple[3])

# #Create a list

# fruit_list=["apple","banana","cherry"]
# print(fruit_list)
# fruit_list[2]="orange"
# print(fruit_list)

# for i in fruit_list:
#     print ("I love", i)
    
# #Dictionary
# student={
#     "student_fname":"Tom",
#     "student_lname":"Smith"
# }


# for x in student:
#     print (student[x])
#     print(x)
    
    
# cars={
#         "Brand":{"main_brand":"Audi","Sub_brand":"Porche"},
#         "model":"Panamera",
#         "Year":"1964"
#         }

# print(cars["Brand"]["main_brand"])
# print(cars["Brand"])
# print(cars["model"])


days={"monday":[{"morning":"breakfast", "afternoon":"lunch","night":"dinner"},{"morning":"aro","afternoon":"osan","night":"ale"}],
      "Tuesday":"fasting",
      "wednesday":{"date":"mercy"}
    
}

print(days["monday"][1]["night"])
print(days["monday"][1])
print(days["monday"][0])