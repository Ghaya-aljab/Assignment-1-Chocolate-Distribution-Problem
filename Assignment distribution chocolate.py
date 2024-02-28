# Task 1: Distribution of chocolates
import random
from enum import Enum

# Definitions for Chocolate and ChocolateType
class ChocolateType(Enum):
    Almond = 'Almond chocolate'
    Peanut_butter = 'Peanut butter chocolate'
    Milk = 'Milk chocolate'
    Dark = 'Dark chocolate'
    White = 'White chocolate'
    Caramel = "Caramel chocolate"

class Chocolate:
    def __init__(self, id_, weight, price, type):
        self.id = id_
        self.weight = weight
        self.price = price
        self.type = type

def generate_chocolates(num_chocolates):
    # Generate a list of Chocolate objects.
    return [
        Chocolate(i, random.randint(1, 5), random.randint(10, 20), random.choice(list(ChocolateType)))
        for i in range(1, num_chocolates + 1)
    ]

def distribute_chocolates_iteratively(chocolates, num_students):
    distribution = []
    for i in range(min(num_students, len(chocolates))):
        chocolate = chocolates[i]
        student_name = f"Student {i+1}"
        distribution.append(f"{student_name} got {chocolate.type.value}, chocolate ID {chocolate.id}, Price: {chocolate.price} AED, Weight: {chocolate.weight}gm")
    return distribution

def distribute_chocolates_recursively(chocolates, num_students, index=0, distribution=None):
    if distribution is None:
        distribution = []
    if index >= num_students or index >= len(chocolates):
        return distribution
    student_name = f"Student {index+1}"
    chocolate = chocolates[index]
    distribution.append(f"{student_name} got {chocolate.type.value}, chocolate ID {chocolate.id}, Price: {chocolate.price} AED, Weight: {chocolate.weight}gm")
    return distribute_chocolates_recursively(chocolates, num_students, index + 1, distribution)

# Distribution Demonstration
num_students = 10  # Adjust this to test with different numbers of students
chocolates = generate_chocolates(num_students)

if num_students == 0:
    print("There are no students available.")
else:
    iterative_distribution = distribute_chocolates_iteratively(chocolates, num_students)
    print("Iterative Distribution:")
    for distribution in iterative_distribution:
        print(distribution)

    recursive_distribution = distribute_chocolates_recursively(chocolates, num_students)
    print("\nRecursive Distribution:")
    for distribution in recursive_distribution:
        print(distribution)

#Task 2: Merge sorting based on weight and price
    def merge_sort(chocolates, key):
        if len(chocolates) > 1:
            mid = len(chocolates) // 2
            L = chocolates[:mid]
            R = chocolates[mid:]

            merge_sort(L, key)
            merge_sort(R, key)

            i = j = k = 0

            while i < len(L) and j < len(R):
                if getattr(L[i], key) <= getattr(R[j], key):
                    chocolates[k] = L[i]
                    i += 1
                else:
                    chocolates[k] = R[j]
                    j += 1
                k += 1

            while i < len(L):
                chocolates[k] = L[i]
                i += 1
                k += 1

            while j < len(R):
                chocolates[k] = R[j]
                j += 1
                k += 1


    def sort_chocolates(chocolates):
        sorted_by_weight = chocolates[:]
        sorted_by_price = chocolates[:]

        merge_sort(sorted_by_weight, "weight")
        merge_sort(sorted_by_price, "price")

        return sorted_by_weight, sorted_by_price

    # Task 2: Sorting Demonstration
    sorted_by_weight, sorted_by_price = sort_chocolates(chocolates)
    print("\nSorted by Weight:")
    for chocolate in sorted_by_weight:
        print(f"ID: {chocolate.id}, Weight: {chocolate.weight}gm")

    print("\nSorted by Price:")
    for chocolate in sorted_by_price:
        print(f"ID: {chocolate.id}, Price: {chocolate.price} AED")

#Task 3 : Search
    def binary_search_chocolates(chocolates, target, key):
        low = 0
        high = len(chocolates) - 1

        while low <= high:
            mid = (low + high) // 2
            if key == "weight":
                mid_val = chocolates[mid].weight
            elif key == "price":
                mid_val = chocolates[mid].price
            else:
                return "Invalid key. Please use 'weight' or 'price'."

            if mid_val < target:
                low = mid + 1
            elif mid_val > target:
                high = mid - 1
            else:
                return f"\nFound chocolate with {key} {target} at position {mid} (ID {chocolates[mid].id})."
        return f"\nNo chocolate with {key} {target} found."

    # Assuming sorted_by_weight and sorted_by_price are already defined and sorted lists.
    search_result_weight = binary_search_chocolates(sorted_by_weight, 2, "weight")
    print(search_result_weight)

    search_result_price = binary_search_chocolates(sorted_by_price, 15, "price")
    print(search_result_price)

