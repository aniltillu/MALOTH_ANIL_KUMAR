def generate_series(n):
    result = []
    for i in range(n):
        result.append(2 * i + 1)
    return result

# Example usage
a = int(input("Enter a number: "))
output = generate_series(a)
print("Output:", ", ".join(map(str, output)))
