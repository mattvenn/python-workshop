numbers = [5, 2, 3, 1, 4]
print "numbers"
print sorted(numbers)

student_tuples = [
    ('john', 'A', 15),
    ('jane', 'B', 12),
    ('dave', 'B', 10),]

def sort_students(arg):
    return arg[2]

print "tuples"
print sorted(student_tuples, key=sort_students)
