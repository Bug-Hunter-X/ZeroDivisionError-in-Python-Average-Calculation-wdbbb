def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list
    return sum(numbers) / len(numbers)

# Example usage:
my_list = [10, 20, 30, 40, 50]
average = calculate_average(my_list)
print(f"The average is: {average}")

my_empty_list = []
average_empty = calculate_average(my_empty_list)
print(f"The average of an empty list is: {average_empty}")

#Improved Solution using exception handling:
def calculate_average_improved(numbers):
    try:
        return sum(numbers) / len(numbers)
    except ZeroDivisionError:
        return 0 # or handle it in a more sophisticated way

my_list = [10, 20, 30, 40, 50]
average = calculate_average_improved(my_list)
print(f"The average is: {average}")

my_empty_list = []
average_empty = calculate_average_improved(my_empty_list)
print(f"The average of an empty list is: {average_empty}") 