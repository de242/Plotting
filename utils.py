import csv
import itertools
import numpy

def window_indices(data, window):
    lower_bound, upper_bound = window
    start, end = 0, 0
    for index, element in enumerate(data):
        if element < lower_bound:
            start = index + 1
        if element < upper_bound:
            end = index
    return start, end


def load_datafile(path):
    """
    Load csv data file with temperatures as col headers and frequency values as first column
    :param path: File to load
    :return: Temps, Freqs, Amps arrays
    """
    amps = []
    freqs = []
    with open(path, 'r') as f:
        raw = csv.reader(f)
        temps = [float(i) for i in raw.next()[1:]]
        for row in raw:
            freqs.append(float(row[0]))
            amps.append([float(i) for i in row[1:]])
    amp_data = numpy.asarray(amps)
    temp_data = numpy.ndarray(shape=amp_data.shape)
    freq_data = numpy.ndarray(shape=amp_data.shape)
    for x, y in itertools.product(range(len(temps)), range(len(freqs))):
        temp_data[y, x] = temps[x]
        freq_data[y, x] = freqs[y]
    return temp_data, freq_data, amp_data