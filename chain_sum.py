def chain_sum(num=None):
    total = 0
    if num is None:
        return total
    elif isinstance(num, int):
        total += num
        return chain_sum(num)
    

if __name__ == '__main__':
    calc = chain_sum(5)()

    print(calc)
