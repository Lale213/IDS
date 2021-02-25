import numpy as np
import time


def testing(synaptic_weights):
    Rez = []
    right = 0
    number_line = 1
    f = open('normal.txt')
    # print(synaptic_weights)
    for line in f:
        if 5000 < number_line < 7000:
            line_spis = line.strip('\n').split(',')
            input_layer = [line_spis[4], line_spis[5], line_spis[22], line_spis[23], line_spis[24], line_spis[25],
                           line_spis[31], line_spis[32], line_spis[37], line_spis[38]]
            for j in range(0, len(input_layer)):
                try:
                    input_layer[j] = int(input_layer[j])
                except ValueError:
                    input_layer[j] = float(input_layer[j])
            new_inputs = normaliz(input_layer)
            output = sigmoid(np.dot(new_inputs, synaptic_weights))
            # print('rez: ', output)
            if output > 0.5:
                Rez.append(1)
                right += 1
            else:
                Rez.append(0)
        number_line += 1

    if right > len(Rez) / 2:
        return 0
    else:
        return 1


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def normaliz(array):
    x_min = [0,     0,    1,   1,   0, 0,   1,   1, 0, 0]
    x_max = [54540, 8315, 511, 511, 1, 1, 255, 255, 1, 1]
    array_1 = []
    for i in range(0, len(array)):
        y = (array[i] - x_min[i]) / (x_max[i] - x_min[i])
        array_1.append(y)
    return array_1


def training():
    start_time = time.time()
    f1 = open('DOS/smurf.txt', 'r')
    f2 = open('normal.txt', 'r')
    F = [f1, f2]
    N = [4000, 1000]
    temp = 1
    m = 1
    training_outputs_1 = np.ones((4001, 1))
    training_outputs_2 = np.zeros((1000, 1))
    training_outputs = np.vstack([training_outputs_1, training_outputs_2])
    synaptic_weights = (2 * np.random.random((10, 1)) - 1) * 0.2
    traiging_inputs_fin = [[-0.29246376811594205, 0.0, 0.0, 0.0, 0.0, 0.0, 0.5708661417322834, 0.0, 0.0, 0.0]]
    for i in range(0, 2):
        for line in F[i]:
            line_spis = line.strip('\n').split(',')
            input_layer = [line_spis[4], line_spis[5], line_spis[22], line_spis[23], line_spis[24], line_spis[25],
                           line_spis[31], line_spis[32], line_spis[37], line_spis[38]]
            for j in range(0, len(input_layer)):
                try:
                    input_layer[j] = int(input_layer[j])
                except ValueError:
                    input_layer[j] = float(input_layer[j])
            input_layer = normaliz(input_layer)
            traiging_inputs = np.array(input_layer)
            traiging_inputs_fin = np.vstack([traiging_inputs_fin, traiging_inputs])
            temp += 1
            if temp > N[i]:
                temp = 1
                break

    # print(traiging_inputs_fin)
    for i in range(0, 10000):
        input_layer = traiging_inputs_fin
        outputs = sigmoid(np.dot(input_layer, synaptic_weights))
        err = training_outputs - outputs
        adjustments = np.dot(input_layer.T, err * (outputs * (1 - outputs)))
        synaptic_weights += adjustments
    return synaptic_weights


def Training():
    start_time = time.time()
    synaptic_weights = training()
    while testing(synaptic_weights) == 0:
        synaptic_weights = training()
    print(time.time() - start_time)
    return synaptic_weights


if __name__ == '__main__':
    Training()