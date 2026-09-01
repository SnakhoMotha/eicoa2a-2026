from ohms_law import calc_power

print("--- Running Power Calculation Tests ---")

result1 = calc_power(10, 5)

if result1 == 20:
    print("Test 1 Passed: calc_power(10, 5) correctly returned 20")
else:
    print(f"Test 1 Failed: Expected 20, but got {result1}")

result2 = calc_power(12, 12)

if result2 == 12:
    print("Test 2 Passed: calc_power(12, 12) correctly returned 12")
else:
    print(f"Test 2 Failed: Expected 12, but got {result2}")
