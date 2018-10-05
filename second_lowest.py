def sort_list_alphabetically(array):
    return sorted(array)


n = eval(raw_input('please enter the number '))

students = []

#enter student name and degrees
for i in range(1 , n+1):
    name = raw_input("please enter the name of student " + str(i) +"\n") 
    degree = input("please enter the degree of student " + str(i) +"\n")

    students.append(
        [
             name , 
            degree
        ]
    )

print(students)

min = []
sl = []

if students[0][1] < students[1][1]: 
    min.append(students[0])
    sl.append(students[1])
    

if students[0][1] == students[1][1]:
    min.append(students[0])
    min.append(students[1])
    

if students[0][1] > students[1][1]: 
    min.append(students[1])
    sl.append(students[0])
    

#find the second lowest degree in student array
for i in range(2 , n):
    #if the lowest degree in low then the degree 
    if min < students[i][1]:
        if len(sl) == 0 :
            sl.append(students[i])
        #if the degree is low than the actual lowest degree
        if students[i][1] < sl[0][1]:
            sl = []
            sl.append(students[i])
        #if the degree is equal to the actual lowest degree
        elif students[i][1] == sl[0][1]:
            sl.append(students[i])
    
    elif min[0][1] == students[i][1]:
        min[len(min)] = students[i]
    
    elif min[0][1] > students[i][1]:
        sl = min 
        min = []
        min.append(students[i])


