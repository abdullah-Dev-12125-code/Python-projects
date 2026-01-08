marks = []

# taking input
marks_insert = input("Enter your marks separated by space: ").split()

# check for "0, 1"
if marks_insert == ["0", "1"]:
    print("No zero")
else:
    # convert each value to integer and append to list
    for m in marks_insert:
        marks.append(int(m))

    # average
    avg = sum(marks) / len(marks)
    print("Average Marks:", avg)

    print("Heighest Marks:", max(marks))
    print("Lowest Marks:", min(marks))

    # students above average
    print("Students score greater then average")
    for i in marks:
        if i > avg:
            print(i)

    # ascending
    print("Ascending")
    for a in sorted(marks):
        print(a)

    # descending
    print("Descending")
    for d in sorted(marks, reverse=True):
        print(d)
