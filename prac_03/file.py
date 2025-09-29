# 1
name = input("What is your name? ")
file = open('name.txt', 'w')
file.write(name)
file.close()

# 2
file = open('name.txt', 'r')
name_from_file = file.read().strip()
file.close()
print(f"Hi {name_from_file}!")

# 3
numbers_total = 0
with open('numbers.txt', 'r') as numbers_file:
    for line in numbers_file:
        current_num = int(line.strip())
        numbers_total += current_num
print(numbers_total)

# 4
with open('numbers.txt', 'r') as file:
    total = 0
    for line in file:
        total += int(line.strip())
print(total)
