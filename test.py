def LCS(a, b):
    if a == '' or b == '':
        return ''
    elif a[-1] == b[-1]:
        return LCS(a[:-1], b[:-1]) + a[-1]
    else:
        sol_a = LCS(a[:-1], b)
        sol_b = LCS(a, b[:-1])
        if len(sol_a) > len(sol_b):
            return sol_a
        return sol_b


if __name__ == "__main__":
    a = 'abc'
    print(a[::-1])
    print(LCS(a, a[::-1]))