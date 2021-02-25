import time
import training_DOS_back
import training_DOS_neptune
import training_DOS_smurf
import training_DOS_teardrop
import training_Probe_ipsweep
import training_Probe_nmap
import training_Probe_portsweep
import training_Probe_satan
import training_R2L_warezclient
import training_R2L_guess_passwd
import testing


def control(synaptic_weights):
    type_attack = ['back_DOS', 'neptune_DOS', 'smurf_DOS', 'teardrop_DOS', 'ipsweep_Probe', 'nmap_Probe',
                   'portsweep_Probe', 'satan_Probe', 'guess_passwd_R2L', 'warezclient_R2L']
    control_array = []
    attack = 0
    file_name = 'TEST_NN/' + input('Ведите имя файла: ') + '.txt'
    number_line = 0
    f = open(file_name, 'r')
    for line in f:
        for i in range(0, 4):
            control_array.append(testing.DOS(synaptic_weights[i], line))
        for i in range(4, 8):
            control_array.append(testing.Probe(synaptic_weights[i], line))
        for i in range(8, 10):
            control_array.append(testing.R2L(synaptic_weights[i], line))
        flag = 0
        attack_name = ''
        for i in range(0, len(control_array)):
            if control_array[i] == 1:
                attack_name += type_attack[i] + '   '
                flag = 1
        if flag == 1:
            print('!!!ATTACK!!!' + attack_name)
            attack += 1
        else:
            print('NOT attack')
        number_line += 1
        control_array = []
    print('traf: ', number_line)
    print('attack: ', attack)
    print('% attack: ', attack / (number_line))


def main():
    synaptic_weights = []
    start_time = time.time()
    synaptic_weights.append(training_DOS_back.Training())
    print('Training DOS_back completed')
    synaptic_weights.append(training_DOS_neptune.Training())
    print('Training DOS_neptune completed')
    synaptic_weights.append(training_DOS_smurf.Training())
    print('Training DOS_smurf completed')
    synaptic_weights.append(training_DOS_teardrop.Training())
    print('Training DOS_teardrop completed')
    synaptic_weights.append(training_Probe_ipsweep.Training())
    print('Training Probe_ipsweep completed')
    synaptic_weights.append(training_Probe_nmap.Training())
    print('Training Probe_nmap completed')
    synaptic_weights.append(training_Probe_portsweep.Training())
    print('Training Probe_portsweep completed')
    synaptic_weights.append(training_Probe_satan.Training())
    print('Training Probe_satan completed')
    synaptic_weights.append(training_R2L_guess_passwd.Training())
    print('Training R2L_warezclient completed')
    synaptic_weights.append(training_R2L_warezclient.Training())
    print('Training R2L_guess_passwd completed')

    print('--- NN is done ---')
    print('all time: ', time.time() - start_time)
    print(synaptic_weights)
    control(synaptic_weights)


if __name__ == '__main__':
    main()
