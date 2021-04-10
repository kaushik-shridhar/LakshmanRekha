# function to convert rssi to distance(in meters)
def convert_rssi(rssi,  measured_power):
    RSSI = int(rssi) # obtained rssi value from the device
    N = 3 # constant. depends on environment factors
    MEASURED_POWER = int(measured_power)# 1 meter rssi

    # formula to convert rssi to meters
    Y = (MEASURED_POWER - RSSI) / (10 * N)
    DISTANCE = pow(10, Y)

    # return the distance calculated
    return DISTANCE

# print('{:.2f}'.format(convert_rssi(-80)))