marks = []
for i in range(3):
    mark = int(input("Enter mark: "))
    marks.append(mark)
print("Original marks:", marks)
marks.insert(0, 90)
print("After inserting 90:", marks)
marks.extend([75, 85])
print("After extending with 75 and 85:", marks)
if 75 in marks:
    marks.remove(75)
    print("75 removed successfully")
removed_value = marks.pop()
print("Removed final mark:", removed_value)
print("Final list:", marks)
print("Length of final list:", len(marks)) 