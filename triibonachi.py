# def tribonacci(signature, n):
#     for i in range(n-3):
#         num = sum(signature[-3:])
#         signature.append(num)
#     return signature[:n]


tribonacci = lambda s, n: [[s.append(sum(s[-3:])) for _ in range(n-3)], s[:n]][-1]


if __name__ == '__main__':
    sgntr, count = [1, 1, 1], 4
    result = tribonacci(sgntr, count)

    print(result)