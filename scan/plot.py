import matplotlib.pyplot as plt

if __name__ == '__main__':
    
    filepath = './scan/scan.out'
    names = ["Serial", "OpenMP T4", "MPI T4"]
    x = list(range(1000, 50001, 1000))  # this is the range of input sizes tested
    with open(filepath, 'r') as file:
        for i, line in enumerate(file):
            y = list(map(float, line.split(',')))
            plt.plot(x, y, label=names[i])

    plt.xlabel('Input size')
    plt.ylabel('Time taken (ms)')
    plt.title('Prefix Sum operation comparisons')
    plt.legend()
    plt.savefig('./scan/scan_comparison.png')
    plt.show()