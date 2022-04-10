def current(volt=0.0,resistance=0.0 )-> float:
    """The function calculate the current from ohm law

    Args:
        volt (float, optional): Value of volts. Defaults to 0.0.
        resistance (float, optional): Value of resistance. Defaults to 0.0.

    Returns:
        float: the value of current
    """    
    return volt / resistance

def resistance(volt=0.0, current=0.0)-> float:
    """The function calculate the resistance from ohm law

    Args:
        volt (float, optional): Value of resistance. Defaults to 0.0.
        current (float, optional): Value of current. Defaults to 0.0.

    Returns:
        float: _description_
    """    
    return volt/current

def volt(resistance=0.0, current=0.0) -> float:
    """The function calculate the value of volts from ohm law

    Args:
        resistance (float, optional): Value of resistance. Defaults to 0.0.
        current (float, optional): Value of currente. Defaults to 0.0.

    Returns:
        float: _description_
    """    
    return resistance * current

def ohm_law()-> None:
    """Retrun a dict with all functions from ohm law

    Returns:
        dict: Functions of ohm law
    """    
    return {
        "volt":volt,
        "resistance": resistance,
        "current": current
    }