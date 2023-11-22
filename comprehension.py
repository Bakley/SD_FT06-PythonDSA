# List comprehension
import time

def measure_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"The function call {func.__name__}(), executed in {execution_time:.7f} seconds")
        return result
    return wrapper

@measure_time
def even_digits(x) -> list[int]:
    new_Arry = []
    for item in range(len(x)):
        if x[item] % 2 == 0:
            new_Arry.append(x[item])
            
    return new_Arry

@measure_time
def list_comprehension_in_python()-> list[int]:
    even_numbers = [ints for ints in numbers if ints % 2 == 0]
    return even_numbers

@measure_time
def generators_in_python():
    even_numbers = (ints for ints in numbers if ints % 2 == 0)
    return even_numbers



if __name__ == "__main__":
    
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # Measure execution time of the normal for loop approach
    even_numbers_indices = even_digits(numbers)
    print(f"Using a normal for loop: {even_numbers_indices}")
    print('*' * 50)

    # Measure execution time of the list comprehension approach
    even_numbers_list = list_comprehension_in_python()
    print(f"Using list comprehension: {even_numbers_list}")
    print('*' * 50)

    # Measure execution time of the generator expression approach
    even_numbers_generator = generators_in_python()
    print(f"Using a generator expression: {even_numbers_generator}")  # Prints the iterator object itself

    # Consume the generator's contents to print the even numbers
    for even_num in even_numbers_generator:
        print(even_num)

    