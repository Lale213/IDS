import numpy as np


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def normaliz_DOS(array):
    x_min = [0,     0,    1,   1,   0, 0,   1,   1, 0, 0]
    x_max = [54540, 8315, 511, 511, 1, 1, 255, 255, 1, 1]
    array_1 = []
    for i in range(0, len(array)):
        y = (array[i] - x_min[i]) / (x_max[i] - x_min[i])
        array_1.append(y)
    return array_1


def normaliz_Probe(array):
    x_min = [0,   0,   0, 0, 0, 0, 1,   1,   0, 0]
    x_max = [511, 150, 1, 1, 1, 1, 255, 255, 1, 1]
    array_1 = []
    for i in range(0, len(array)):
        y = (array[i] - x_min[i]) / (x_max[i] - x_min[i])
        array_1.append(y)
    return array_1


def normaliz_R2L(array):
    x_min = [0,     0, 0, 0, 1, 1,   1,   0, 0, 0,    0]
    x_max = [2453, 28, 1, 1, 3, 255, 144, 1, 1, 0.67, 0.96]
    array_1 = []
    for i in range(0, len(array)):
        y = (array[i] - x_min[i]) / (x_max[i] - x_min[i])
        array_1.append(y)
    return array_1


def DOS(synaptic_weights, line):
    line_spis = line.strip('\n').split(',')
    input_layer = [line_spis[4], line_spis[5], line_spis[22], line_spis[23], line_spis[24], line_spis[25],
                   line_spis[31], line_spis[32], line_spis[37], line_spis[38]]
    for j in range(0, len(input_layer)):
        try:
            input_layer[j] = int(input_layer[j])
        except ValueError:
            input_layer[j] = float(input_layer[j])
    new_inputs = normaliz_DOS(input_layer)
    output = sigmoid(np.dot(new_inputs, synaptic_weights))
    # print('rez: ', output)
    if output > 0.5:
        return 1
    else:
        return 0


def Probe(synaptic_weights, line):
    line_spis = line.strip('\n').split(',')
    input_layer = [line_spis[22], line_spis[23], line_spis[26], line_spis[27], line_spis[28], line_spis[29],
                   line_spis[31], line_spis[32], line_spis[39], line_spis[40]]
    for j in range(0, len(input_layer)):
        try:
            input_layer[j] = int(input_layer[j])
        except ValueError:
            input_layer[j] = float(input_layer[j])
    new_inputs = normaliz_Probe(input_layer)
    output = sigmoid(np.dot(new_inputs, synaptic_weights))
    # print('rez: ', output)
    if output > 0.5:
        return 1
    else:
        return 0


def R2L(synaptic_weights, line):
    line_spis = line.strip('\n').split(',')
    input_layer = [line_spis[5], line_spis[9], line_spis[11], line_spis[21], line_spis[22], line_spis[31],
                   line_spis[32], line_spis[33], line_spis[35], line_spis[36], line_spis[39]]
    for j in range(0, len(input_layer)):
        try:
            input_layer[j] = int(input_layer[j])
        except ValueError:
            input_layer[j] = float(input_layer[j])
    new_inputs = normaliz_R2L(input_layer)
    output = sigmoid(np.dot(new_inputs, synaptic_weights))
    # print('rez: ', output)
    if output > 0.5:
        return 1
    else:
        return 0
