from statistics import *


arr = [
    30, 29, 24, 27, 20, 22, 21, 26, 25, 25,
    26, 24, 27, 28, 21, 28, 27, 22, 26, 28,
    24, 24, 28, 21, 25, 25, 24, 22, 27, 30
]


if __name__ == '__main__':
    rs = ranked_series(arr)
    vs = variation_series(arr)
    freqs = freq_series(arr)
    rel_freqs = rel_freq_series(arr)
    table_freqs = {v: c for v, c in zip(vs, freqs)}
    table_relfreqs = {v: r for v, r in zip(vs, rel_freqs)}
    scope = scope_series(arr)
    moda = moda_series(arr)
    median = median_series(arr)

    print(f'{rs = }')
    print(f'{vs = }')

    print(f'{table_freqs = }')
    print(f'{table_relfreqs = }')

    print(f'{scope = }')
    print(f'{moda = }')
    print(f'{median = }')

    plt.figure()
    plt.title('Полігон частот')
    plt.plot(table_freqs.keys(), table_freqs.values())
    plt.plot(table_freqs.keys(), table_freqs.values(), 'o')
    plt.grid()
    plt.show()

    plt.figure()
    plt.title('Полігон відносних частот')
    plt.plot(table_relfreqs.keys(), table_relfreqs.values())
    plt.plot(table_relfreqs.keys(), table_relfreqs.values(), 'o')
    plt.grid()
    plt.show() 