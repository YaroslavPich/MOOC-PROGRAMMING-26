students = int(input("How many students on the course? "))
size_group = int(input("Desired group size? "))
group = students // size_group + int(bool(students % size_group))
print(f"Number of groups formed: {group}")
