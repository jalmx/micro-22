def map(x, min_in, max_in, min_out,max_out): # inspirada de https://www.arduino.cc/reference/en/language/functions/math/map/
    return ( x - min_in) * (max_out - min_out) / (max_in - min_in) + min_in