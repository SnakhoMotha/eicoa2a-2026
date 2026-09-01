
def mm_to_inches(mm):
    """Convert millimetres to inches."""
    return mm / 25.4


def inches_to_mm(inches):
    """Convert inches to millimetres."""
    return inches * 25.4

def cm_to_inches(cm):
    """Convert centimetres to inches."""
    return cm / 2.54

def inches_to_cm(inches):
    """Convert inches to centimetres."""
    return inches * 2.54

print("--- Unit Converter Documentation ---")
print("mm_to_inches:", mm_to_inches.__doc__)
print("inches_to_mm:", inches_to_mm.__doc__)
print("cm_to_inches:", cm_to_inches.__doc__)
print("inches_to_cm:", inches_to_cm.__doc__)
print("-----------------------------------")