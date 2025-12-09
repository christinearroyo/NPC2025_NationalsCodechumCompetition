# Problem 1
bill = float(input())
tip = float(input())

calc = bill * tip / 100
total = bill + calc

print(f"Tip: {calc:.2f}, Total: {total:.2f}")

# Problem 2
user = input().strip().upper()

vowel = {
    'a': "Vowel",
    'b': "Vowel",
    'c': "Vowel",
    'd': "Vowel",
    'e': "Vowel",
}

final = vowel.get(user, "Consonant")
print(final)

# Problem 3
user = int(input())

n = 0
for i in range(2, user + 1, 2):
    n += i

print(n)

#Problem 4
user = input()

if user == user[::-1]:
    print("Palindrome")
else:
    print("Not a Palindrome")

#Problem 5
user = input().strip()

arr = [
    int(user[0]), int(user[1]), int(user[2]),
    int(user[3]), int(user[4]), int(user[5]),
    int(user[6]), int(user[7]), int(user[8])
]

sum_1 = arr[0] + arr[1] + arr[2]
sum_2 = arr[3] + arr[4] + arr[5]
sum_3 = arr[6] + arr[7] + arr[8]

print(f"Row 1 Sum: {sum_1}, Row 2 Sum: {sum_2}, Row 3 Sum: {sum_3}")

#Problem 6
user = input().strip()

arr = [
    int(user[0]), 
    int(user[4]), 
    int(user[8])
]

output = arr[0] + arr[1] + arr[2]
print(output)

#Problem 7
user = input()

final = ""
for i in user:
    if i.isupper():
        final += i.lower()
    elif i.islower():
        final += i.upper()
    else:
        final += i
print(final)

#Problem 8
user = input().strip()

matrix = []
for i in range(4):
    row = user[i*4 : (i+1)*4]
    matrix.append(row)

for i in range(4):
    for j in range(4):
        if matrix[i][j] == '0':  
            print("~", end="  ")
        elif matrix[i][j] == '1':  
            print("G", end="  ")
        elif matrix[i][j] == '2': 
            print("M", end="  ")