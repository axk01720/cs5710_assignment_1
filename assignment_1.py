# question 1
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
# sorting
ages.sort()
print("After sorting the list: ", ages)
# after sorting first item in list will be minimum and last item will be maximum
minimum = ages[0]
maximum = ages[-1]
print("Minimum : ", minimum, "Maximum : ", maximum)
# to add minimum , maximum I am using insert
ages.insert(0, minimum)
ages.insert(-1, maximum)
print(ages, 'after inserting')
# median
# after adding min, max values to list now there are 12 values in the list
median = (ages[5] + ages[6]) / 2
print("Median: ", median)
# average
sum_of_all_values = 19 + 19 + 19 + 20 + 22 + 24 + 24 + 24 + 25 + 25 + 26 + 26
total_items_in_list = len(ages)
average = sum_of_all_values / total_items_in_list
print("Average: ", average)
# range (max - min)
range = maximum - minimum
print("Range: ", range)

# question 2
# dog dictionary
dog = {}
dog["name"] = "Ruby"
dog["color"] = "white"
dog["breed"] = "part Australian shepherd and part border collie"
dog["legs"] = "4 in good position"
dog["age"] = "9 years"
print("Dog dictionary -- ", dog)
# student dictionary
student = {}
student["first_name"] = "Abhiram Reddy"
student["last_name"] = "Komma"
student["gender"] = "male"
student["age"] = "26 years"
student["marital status"] = "single"
student["skills"] = ["JavaScript", "HTML", "CSS"]
student["country"] = "USA"
student["city"] = "Kansas"
student["address"] = "Overland Park , KS"
student_dictionary_length = len(student);
print("Student Dictionary Length: ", student_dictionary_length)
get_student_skills = student["skills"]
print("Skills: ", get_student_skills, "Data type: ", type(get_student_skills))
add_student_skills = student["skills"] + ["React JS", "Node JS"]
print("after adding skills: ", add_student_skills)
student_keys = student.keys();
print("Student Keys: ", student_keys)
student_values = student.values();
print("Student values: ", student_values)

# question 3
# tuple
sisters_tuple = ("Nora", "Charlotte", "Emily")
brothers_tuple = ("Trace", "Kevin", "Connor")
siblings = sisters_tuple + brothers_tuple
print("Siblings: ", siblings)
print("Siblings Length: ", len(siblings))
# to modify tuple I am changing it to list and adding values later
modifying_tuple = list(siblings)
# adding mother and father
modifying_tuple.append("Lyndie Greenwood")
modifying_tuple.append("Wes Brown")
family_members = modifying_tuple
print("Family Members: ", family_members)

# question 4
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
age = [22, 19, 24, 25, 26, 24, 25, 24]
length_of_it_companies = len(it_companies)
print("it_companies length: ", length_of_it_companies)
# add 'Twitter'
it_companies.add('Twitter')
print("after adding" , it_companies)
# adding multiple items to set
it_companies.update(["PayPal", "Honeywell International", "JP Morgan", "Wells Fargo"])
print("after adding multiple items: ", it_companies)
# removing item from set
it_companies.remove("Wells Fargo")
print("after removing item ", it_companies)
# Note: Difference between remove and discard is remove will throw an error if the item does not exist in set whereas
# discard do not throw any error
# it_companies.remove("Wells Fargo")
it_companies.discard("Wells Fargo")
# Traceback (most recent call last):
#   File "C:\Users\abhiram\CS5710\assignment 1\home_work\assignment_1.py", line 91, in <module>
#     it_companies.remove("Wells Fargo")
# KeyError: 'Wells Fargo'
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
# join A and B
join_A_and_B = A.union(B)
print("join A and B, ", join_A_and_B)
# intersection of A and B
intersection_A_and_B = A.intersection(B)
print("intersection A and B, ", intersection_A_and_B)
# checking subset
A_subset_of_B = A.issubset(B);
print("is A subset of B ", A_subset_of_B)
# check for disjoint
check_for_disjoint = A.isdisjoint(B);
print("are A and B disjoint? ", check_for_disjoint)
# join A with B
join_A_with_B = A.union(B)
# join B with A
join_B_with_A = B.union(A)
# symmetric difference
symmetric_diff = A.symmetric_difference(B)
print("Symmetric Difference: ", symmetric_diff)
# delete sets
del A
del B
# print("after deleting sets, ", A , B)
age = [22, 19, 24, 25, 26, 24, 25, 24]
ages_set = set(age)
print("ages set: ", ages_set)
ages_set_length = len(ages_set);
ages_list_length = len(age)
print("ages set length: ", ages_set_length , "ages list length: ", ages_list_length)
difference = ages_list_length - ages_set_length
print("difference between list and set lengths , ", difference)


# question 5
radius = 5
pi = 3.14159
area = pi * radius * radius
_area_of_circle_ = area
print("Area of circle: ", _area_of_circle_)
circumference = 2*pi*radius
_circum_of_circle_ = circumference
print("Circumference: ", _circum_of_circle_)
# input from user
radius = input("Enter radius value: ");
convert_to_int = int(radius)
area = pi * convert_to_int * convert_to_int
print("Area of circle with user radius, " , area)


# question 6
# I will split sentence using " " and then convert list to set to get unique words
sentence = "I am a teacher and I love to inspire and teach people"
words = sentence.split(" ")
print("words: ", words)
unique_words = set(words);
print("Unique words: ", unique_words)
unique_words_length = len(unique_words);
print("Unique words length: ", unique_words_length)


# question 7
tab_escape_sequence = "\nName\t Age\t Country\t City\nAsabeneh 250\t Finland\t Helsinki"
print("escape sequence: ", tab_escape_sequence)


# question 8
# using format method
radius = 10
area = 3.14 * radius ** 2
sentence_to_format = "The area of a circle with radius 10 is {circle_area} meter square"
print("Sentence after formatting: ",sentence_to_format.format(circle_area = area))


# question 9
item1 = input("Enter first value: ")
item2 = input("Enter second value: ")
item3 = input("Enter third value: ")
item4 = input("Enter fourth value: ")
item5 = input("Enter fifth value: ")
weights_list = [item1, item2, item3, item4, item5]
weights_kilograms_list = []
print("weights_list: ", weights_list)
for item in weights_list:
    weight_in_kg = int(item)*0.453592
    weights_kilograms_list.append(weight_in_kg)
print("weights_kg_list: ", weights_kilograms_list)


# question 10
# solution was provided in the word document