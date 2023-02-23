def Flight_Length(F):
    result = 0
    if F<25:
        result = -100
    elif F<50:
        result = 500
    elif F<70:
        result = 650
    elif F<80:
        result = 750
    elif F<95:
        result = 850
    elif F<115:
        result = 1000
    elif F<=125:
        result = 1200
    elif F>125:
        result = -100
    return result

