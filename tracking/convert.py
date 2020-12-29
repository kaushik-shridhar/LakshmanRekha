from math import log10

# function to convert rssi to meters
def convert_rssi(measured_power, rssi, n):
    MEASURED_POWER = measured_power
    RSSI = rssi
    N = n

    exp = (((MEASURED_POWER) - (RSSI)) / (10 * N))
    DISTANCE = 10**exp

    return DISTANCE

def convert_rssi2(dBm):
    MHz = 2417
    FSPL = 27.55
    dist = 10 ** ((FSPL - (20 * log10(MHz)) + abs(dBm)) / 20)
    dist = round(dist, 2)

    return dist