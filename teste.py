import math

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

def TSsin(x, decimal_cases):

    _sin = 0
    aux_sinal = 1
    aux = 1
    while True:
        aux_sin = aux_sinal * (x ** aux) / factorial(aux)
        
        if (abs(aux_sin) < 10 ** (-decimal_cases)):
            break
        
        _sin += aux_sin
        
        aux += 2
        aux_sinal *= -1
        
    return _sin

def test_sin():
    result = TSsin(math.pi, 10)
    print(result)
    assert result == math.sin(math.pi)

if __name__ == '__main__':
    test_sin()