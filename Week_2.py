# Kem
# November 15, 2024
# Week 2 : Lists
# def. of list : store items
# ex. of list : list_var = [item1 , item2]
# LIST OF STRINGS
# ex. of list of strings : listA (fruits) = ["apple" , "banana" , "orange"]
# LIST OF INTEGERS
# ex. of list of integers : listB (numbers) = [1 , 2 , 3 , 4]
# LIST OF BOTH
# ex. of list of both : listC (things) = ["apple" , 1 , "banana" , 4]
# PRINTING LISTS
# item1 = input ("Enter one thing you need to survive: ")
# item2 = input ("Enter another item you need to survive: ")
# item3 = input ("Enter one last item you need to survive: ")
# survivalitems = [item1 , item2 , item3]
# print(survivalitems)
# ANOTHER WAY TO PRINT "LISTS"
# items = input ("Enter 3 items you need to survive: ")
# print(items)
# INDEX
# def. of index : the psition or location of the item in a list (start counting at 0 [zero])
# ex. of list with index : listA = ["apple" , "banana" , "pear"] 
# listA[1] = "grape"
# print(listA) will print : ["apple" , "grape" , "pear"]
# CONCATENATE
# def. of concatenate : to link things together
# ex. of concatenated lists : newlist = things + fruits
# print(newlist) will print :  ["apple" , "banana" , "orange" , "apple" , 1 , "banana" , 4]
# APPEND , INSERT AND REMOVE
# def. of .append : add smt to the end of the list
# def. of .insert : add smt to anywhere in the list
# def. of remove : remove smt from a list
# ex. of .append : newlist.append("CAR") will add "CAR" to the end of the list
# ex. of .insert : newlist.insert(0, "BUS") will add "BUS" to index 0
# ex. of .remove : newlist.remove("BUS") will remove "BUS" from the list

# WORK
 
num_list = [1, 1000 , 2 , 4 , 3 , 24 , 77 , 6 , 7 ,11 ,8]
num_list.remove(1)
num_list.remove(1000)
num_list.remove(2)
num_list(3) == 45
num_list(4) == 87
num_list(6) == 5
num_list.append(9)
num_list.append(10)