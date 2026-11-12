
# ==========================================
# 06 - ITERATORS AND GENERATORS
# ==========================================


# ------------------------------------------
# 1. ITERABLES
# ------------------------------------------

# An iterable is an object we can loop over.
# Examples: list, tuple, string, dictionary, set.

numbers = [10, 20, 30]

print("ITERABLE:")
for num in numbers:
    print(num)


# ------------------------------------------
# 2. CREATING AN ITERATOR USING iter()
# ------------------------------------------

numbers = [10, 20, 30]

iterator = iter(numbers)

print("\nITERATOR:")
print(next(iterator))  # 10
print(next(iterator))  # 20
print(next(iterator))  # 30

# Calling next() again would raise StopIteration.


# ------------------------------------------
# 3. HOW A FOR LOOP WORKS INTERNALLY
# ------------------------------------------

numbers = [10, 20, 30]

iterator = iter(numbers)

print("\nMANUAL ITERATION:")

while True:
    try:
        num = next(iterator)
        print(num)
    except StopIteration:
        break


# ------------------------------------------
# 4. GENERATOR FUNCTION USING yield
# ------------------------------------------

def generate_numbers():
    print("Generating 10")
    yield 10

    print("Generating 20")
    yield 20

    print("Generating 30")
    yield 30


print("\nGENERATOR FUNCTION:")

gen = generate_numbers()

print(next(gen))
print(next(gen))
print(next(gen))


# ------------------------------------------
# 5. GENERATOR EXECUTION AND PAUSING
# ------------------------------------------

def demo():
    print("A")
    yield 1

    print("B")
    yield 2


print("\nGENERATOR EXECUTION:")

gen = demo()

x = next(gen)
y = next(gen)

print("x =", x)
print("y =", y)


# ------------------------------------------
# 6. GENERATOR EXPRESSION
# ------------------------------------------

squares = (x ** 2 for x in range(5))

print("\nGENERATOR EXPRESSION:")

for square in squares:
    print(square)


# ------------------------------------------
# 7. LIST COMPREHENSION VS GENERATOR
# ------------------------------------------

# List comprehension creates the complete list.
list_squares = [x ** 2 for x in range(5)]

# Generator expression produces values lazily.
generator_squares = (x ** 2 for x in range(5))

print("\nLIST:", list_squares)
print("GENERATOR:", generator_squares)

print("First generated value:", next(generator_squares))


# ------------------------------------------
# 8. PRACTICAL EXAMPLE: BATCH GENERATOR
# ------------------------------------------

def generate_batches(data, batch_size):
    for i in range(0, len(data), batch_size):
        yield data[i:i + batch_size]


dataset = list(range(1, 11))

print("\nDATASET BATCHES:")

for batch in generate_batches(dataset, 3):
    print(batch)
