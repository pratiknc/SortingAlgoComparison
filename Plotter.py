from matplotlib import pyplot as plt

import itertools



def plot_group(timings_avg, algos,title):
    for algo in algos:
        plt.plot(timings_avg.index, timings_avg[algo], marker='o')
    plt.xscale('log')
    plt.xlabel('Input Sizes', fontsize=14)
    plt.ylabel('Time in seconds', fontsize=14)
    plt.title(title)
    plt.legend(algos)
    plt.show()


def plot_group_save(timings_avg, algos, input_size_array, array_type):
    for algo in algos:
        plt.plot(timings_avg.index, timings_avg[algo], marker='o')
        plt.xlabel('Input Sizes', fontsize=14)
        plt.ylabel('Time in sec', fontsize=14)
        # plt.xscale('log')
        plt.xticks(input_size_array)
        plt.legend(algo)
        file_path = algo + '.png'
        plt.savefig(file_path)
        plt.close()

    algos_permut = []

    for i in range(2, len(algos) + 1):
        algos_permut.append(itertools.combinations(algos, i))

    for algos_permut_elem in algos_permut:
        for algo_group in algos_permut_elem:
            for algo in algo_group:
                plt.plot(timings_avg.index, timings_avg[algo], marker='o')
            # plt.xscale('log')
            # plt.xtick
            plt.xticks(input_size_array)
            plt.xlabel('Input Sizes', fontsize=14)
            plt.ylabel('Time in ms', fontsize=14)
            plt.legend(algo_group)
            file_path = ''.join(algo_group) + '_' + array_type + '.png'
            plt.savefig(file_path)
            plt.close()
