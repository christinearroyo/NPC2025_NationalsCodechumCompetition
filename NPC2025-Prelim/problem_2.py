arrSize = int(input("Enter array size: "))
arrElement = list(map(int,input("Enter array elements: ").split()))

peak = 0
valley = 0

for i in range(1, arrSize - 1):
    if arrElement[i] > arrElement[i - 1] and arrElement[i] > arrElement[i + 1]:
        peak += arrElement[i]
    elif arrElement[i] < arrElement[i - 1] and arrElement[i] < arrElement[i + 1]:
        valley += arrElement[i]

result = peak - valley
print(f"Result: {result}")