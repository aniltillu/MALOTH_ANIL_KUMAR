def generate_odd_series(a):
    # If a is even, reduce it by 1
    if a % 2 == 0:
        a -= 1

    # Create list of first 'a' odd numbers
    result = []
    for i in range(1, a * 2, 2):
        result.append(i)
    
    return result

# Example usage
a = int(input("Enter a number: "))
output = generate_odd_series(a)

# Print result
print("Output:", ", ".join(map(str, output)))