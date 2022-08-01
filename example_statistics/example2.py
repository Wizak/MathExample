from statistics import *


arr = [
    66, 86, 87, 95, 77, 79, 78, 70, 63, 82,
    81, 70, 82, 77, 81, 78, 80, 69, 80, 80,
    74, 76, 82, 78, 85, 90, 75, 65, 70, 80
]


if __name__ == '__main__':
    ivs = interval_series(arr)
    freq_ivs = interval_freq_series(arr)
    relfreq_ivs = rel_interval_freq_series(arr)

    print(f'{ivs = }')
    print(f'{freq_ivs = }')
    print(f'{relfreq_ivs = }')

    plt.figure()
    plt.title('Гістограма відносних частот')
    plt.hist(arr, bins=5, density=True)
    plt.grid()
    plt.show()  