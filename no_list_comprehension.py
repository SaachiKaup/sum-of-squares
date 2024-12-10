import sys
import math
import itertools as it

def str2ints(input_str: str) -> [int]:
    return list(map(int, input_str))

def squares(arr: [int]) -> [int]:
    def square(n: int) -> int:
        return pow(n, 2)
    return list(map(square, arr))

def read_line_input(s: str) -> str:
    def split_line(s: str) -> [str]:
        return s.split("\n")
    return split_line(s)[0]

def remove_negs(elems: [int]) -> [int]:
    def is_neg(n: int) -> bool:
        return n < 0
    return list(it.filterfalse(is_neg, elems))

def sum_of_squares(elems: [int]) -> int:
    return sum(squares(elems))

def sum_squares_of_input(s: str) -> str:
    def read_input_arr(s: str) -> [int]:
        return str2ints(s.split(" "))
    return str(sum_of_squares(read_input_arr(s)))

def format(result_strs: [str]) -> str:
    return "\n".join(result_strs)

def main():
    num_test_cases = int(input())
    input_strs = sys.stdin.readlines()
    paired_test_cases = list(map(read_line_input, input_strs))
    test_cases = paired_test_cases[1: len(paired_test_cases): 2] 

    print(format(list(map(sum_squares_of_input, test_cases))))

main()
