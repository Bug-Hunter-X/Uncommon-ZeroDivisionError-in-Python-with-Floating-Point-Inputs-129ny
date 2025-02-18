def function_with_uncommon_error(x):
    try:
        if x == 0.0 or x == float('inf') or x == float('-inf'):
          print("Error: Cannot divide by zero or infinity")
          return None
        result = 1 / x
        return result
    except ZeroDivisionError:
        print("Error: Cannot divide by zero")
        return None

# Example usage:
print(function_with_uncommon_error(10))
print(function_with_uncommon_error(0))
print(function_with_uncommon_error(0.0))
print(function_with_uncommon_error(float('inf')))
print(function_with_uncommon_error(float('-inf')))