numbers = [10,20,30,40,50]
print(numbers)

print(numbers[0])
print(numbers[2])
print(numbers[4])

#negative indexing
print(numbers[-1])

#modifing elist elements
numbers[1]= 99
print(numbers)

#adding elements list
numbers.append(60)
print(numbers)

numbers =[10,20,30,40,50]

#remove particular number
numbers.remove(99)
print(numbers)

#remove last number
numbers.pop()
print(numbers)

print(len(numbers))
for num in numbers:
    print(num)

    #slice
    numbers=[10,20,30,40,50]