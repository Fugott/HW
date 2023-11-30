student_id = {111: "Eric",
               112: "Kyle", 
               113: "Butters"}
print("Initial Dictionary: ", student_id)
 
del student_id[111]
 
print(111 in student_id)

print("Updated Dictionary ", student_id)

for i in student_id:
    print(student_id[i])