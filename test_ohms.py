from ohms_law import calc_resistance
results = calc_resistance(10, 2)
print("Resistance =", results, "ohms")
print(calc_resistance.__doc__)
assert calc_resistance(9, 0.03) == 300
assert calc_resistance(24, 2) == 12