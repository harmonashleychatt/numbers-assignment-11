# defining the list called numbers
numbers = [901, 615, 423, 404, 706, 931]
total = 0
valid_numbers = []
# empty valid number list
for num in numbers:
    if num < 0 or num > 100:
        pass
# loop to add to valid list
else:
    valid_numbers.append(num)
    total += num
print(num)
# calculating average
average = total / len(valid_numbers)
print("total:", total)
print("average:", average)
