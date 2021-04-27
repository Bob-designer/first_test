import numpy as np
def get_all_channels_from_load(load):
    left_4 = load[0:4]
    serial_number = np.frombuffer(left_4, '>I')[0]
    now = datetime.now()
    # print(serial_number, end=' ')
    signed_channels_all: np.ndarray = np.frombuffer(load[0:4], '>I') % (2 ** 24)
    signed_channels_all = signed_channels_all << 8
    signed_channels_all = signed_channels_all.astype('>i')
    signed_channels_all = signed_channels_all // 2 ** 8
    signed_channels_all = signed_channels_all.reshape((32, 8)).transpose()
    signed_channels_all = signed_channels_all * UNIT

    return signed_channels_all