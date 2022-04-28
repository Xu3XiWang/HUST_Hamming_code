import numpy as np

def check_hamming_code(code_input):
    code_ham = code_input
    n = len(code_ham)
    code_ham = np.array(code_ham)
    x = 1
    while True:
        if 2 ** x - 1 >= n:
            break
        else:
            x += 1
    # 计算校验位置
    pos = np.array([2 ** i for i in range(x)])

    label = np.arange(1, n + 1, 1, int)
    error_pos = 0
    # 计算各个校正位的值
    for p in pos:
        r = np.bitwise_and(label, p)
        temp = code_ham[np.where(r)]
        for i, t in enumerate(temp):
            if i == 0:
                temp_ = t
            else:
                temp_ = np.bitwise_xor(temp_, t)
        # 判断xor是否为0，若不是0，则将对应位置反，得到校验码
        error_pos += temp_ * p
    if error_pos == 0:
        return 0
    else:
        if code_ham[error_pos - 1] == 0:
            code_ham[error_pos - 1] = 1
        else:
            code_ham[error_pos - 1] = 0
        return code_ham

def generate_hamming_code(code_raw):
    n = len(code_raw)
    code_raw = np.array(code_raw)
    x = 1
    while True:
        if 2 ** x - 1 >= n + x:
            break
        else:
            x += 1
    code_ham = np.zeros(x + n)
    pos = np.array([2 ** i for i in range(x)])
    # 将所有补充位置先设定为1，将所有原始位置先设定为0
    code_ham[pos - 1] = 1
    code_ham[code_ham == 0] = code_raw
    code_ham = code_ham.astype(int)
    label = np.arange(1, n + x + 1, 1, int)
    # 计算各个校正位的值
    for p in pos:
        r = np.bitwise_and(label, p)
        temp = code_ham[np.where(r)]
        for i, t in enumerate(temp):
            if i == 0:
                temp_ = t
            else:
                temp_ = np.bitwise_xor(temp_, t)
        # 判断xor是否为0，若不是0，则将对应位置反，得到校验码
        if temp_ == 1:
            code_ham[p - 1] = 0
    return list(code_ham)
