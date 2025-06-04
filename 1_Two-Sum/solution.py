import sys
from typing import List, Tuple, Dict, Set 

input = sys.stdin.readline 

def get_string() -> str:
    return input().strip()

def get_int() -> int:
    return int(input())

def get_ints() -> List[int]:
    return list(map(int, input().split()))

def get_floats() -> List[float]:
    return list(map(float, input().split()))

def get_list_strings() -> List[str]:
    return input().strip().split()

def get_list_ints_matrix(rows: int) -> List[List[int]]:
    matrix = []
    for _ in range(rows):
        matrix.append(get_ints())
    return matrix

def solve(nums, target):
   num_map = {} 
   for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            print(num_map[complement], i) 
            return [num_map[complement], i]
        num_map[num] = i

if __name__ == "__main__":
    nums = get_ints()
    target = get_int()
    solve(nums, target)