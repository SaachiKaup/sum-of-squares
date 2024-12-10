import math

def read_input(input_str: str) -> [int]:
    return list(map(int, input_str))

def squares(arr: [int]) -> [int]:
    return list(map(lambda x: pow(x, 2), arr))

print(read_input(input().split(" ")))
