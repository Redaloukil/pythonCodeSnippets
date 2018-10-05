def result(marks):
    return float(int(marks[0]) + int(marks[1]) + int(marks[2]))/3

n = int(raw_input())

student_marks = {}

for _ in range(n):
    line = raw_input().split()
    name, scores = line[0], line[1:]
    scores = map(float, scores)
    student_marks[name] = scores

print(student_marks)

query_name = raw_input()
info = student_marks[query_name]

_result = result(info) 
    

print(_result.quantize())


