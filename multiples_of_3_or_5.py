# ---------  Multiples of 3 or 5 ---------

# If we list all the natural numbers ℕ (positive integers) below 10 that are multiples of 3 or 5,
# we get 3, 5, 6, and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

import time
def main():
    start = time.perf_counter()

    sum_of_all_multiples = 0
    for i in range(1000):
        if i % 3 == 0 or i % 5 == 0:
            sum_of_all_multiples += i

    end = time.perf_counter()
    print(f"Answer: {sum_of_all_multiples}")
    print(f"Execution time: {end - start:.4f} seconds")

if __name__ == "__main__":
    main()