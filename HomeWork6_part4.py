#numbers = input('Enter numbers :')
numbers = list(map(int, input("Enter numbers :").split(" ")))
target = int(input('Enter target number :'))
result = []

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] + numbers[j] == target:
            result.append((numbers[i], numbers[j]))

print(result)
