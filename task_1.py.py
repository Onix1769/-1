numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим

incorrect_none = numbers[4]
correct_none = 0
numbers[4] = correct_none
numbersum = (sum(numbers) / len(numbers))
numbers[4] = numbersum
print("Измененный список:", numbers)
