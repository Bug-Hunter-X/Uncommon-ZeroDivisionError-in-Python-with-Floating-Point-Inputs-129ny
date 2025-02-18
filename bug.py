def function_with_uncommon_error(x):
    try:
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

#In this code, the error happens when you pass in 0 or 0.0, floating-point numbers as parameters, which will trigger the ZeroDivisionError exception. Similarly, a floating point infinity will also result in an error. 
# The function handles this exception gracefully, but the uncommon aspect is the specific input that causes it (0.0 or float('inf')) compared to typical integer division by zero.