
def calc_current(voltage, resistance):
    """Calculate the electrical current using Ohm's Law.
     
      Args:
         voltage(in volts)
          resistance(in ohms) 
          
     output: current(in amperes)
     """
    if resistance == 0:
        raise ValueError("Resistance cannot be zero.")
    return voltage / resistance

def calc_power(voltage, resistance):
    """Calculate the power dissipated in a resistor.

    Args:
        voltage(in Volts)
        current(in amperes)

    Output: Power(in watts)
    """
    current = calc_current(voltage, resistance)
    power = voltage * current
    return power

print(calc_power.__doc__)