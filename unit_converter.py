def  mm_to_inches(mm):
    """Convert millimetres to inches.
    
    Args:
        Length in millimetres.

    Returns:
           float: Length in inches (1 inche = 25.4 mm)
    """
    return mm / 25.4

def inches_to_mm(inches):
    """Convert inches to millimetres.
    Args:
        inches(float): length in millimetres.
    
    Returns:
           float: length in millimetres (inches * 25.4)
    """
    return inches * 25.4