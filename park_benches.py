# Author:Yi Sun(Tim) 2024-2-5

from typing import List, Tuple


def park_benches(benches: List[Tuple[int, int]], dist: int) -> int:
    if not benches or dist <= 0:
        return 0

    bench_start_list = []
    bench_end_list = []

    for bench in benches:
        bench_start, length = bench
        bench_start_list.append(bench_start)
        bench_end_list.append(bench_start + length)
    print('start 2',bench_start_list[1])
    print('end 1,',bench_end_list[0])
    for i in range(1,len(bench_start_list)-1):
        actual_dist = bench_start_list[i] - bench_end_list[i-1]

        if actual_dist <= dist and bench_end_list[i-1] - bench_start_list[i-1] < bench_end_list[i] - bench_start_list[i]:
            del bench_start_list[i-1]
            del bench_end_list[i-1]
        elif actual_dist <= dist and bench_end_list[i-1] - bench_start_list[i-1] > bench_end_list[i] - bench_start_list[i]:
            del bench_start_list[i]
            del bench_end_list[i]

    # print('actural_dist is',actual_dist)
    print(bench_start_list)
    print(bench_end_list)

    final_dist_list = []
    for j in range(0,len(bench_start_list)):
        final_dist_list.append(bench_end_list[j]-bench_start_list[j])
    print('final list is',final_dist_list)
    final_dist = max(final_dist_list)
    print('final',final_dist)
    return final_dist


if __name__ == '__main__':
    print("Example:")
    park_benches([(1, 3), (6, 5), (13, 4)], 3)

    # These "asserts" are used for self-checking and not for an auto-testing
    assert park_benches([(0, 2), (3, 3)], 2) == 3, "1 of 2 benches"
    assert park_benches([(1, 3), (6, 5), (13, 4)], 3) == 7, "2 of 3 benches "
    assert park_benches([(1, 2), (5, 6), (13, 3)], 3) == 6, "1 of 3 benches"
    assert park_benches([(0, 2), (3, 3), (8, 2), (11, 3)], 3) == 6, "2 of 4 benches"
    assert park_benches([(0, 5)], 7) == 5, "1 bench"
    assert park_benches([(0, 4), (5, 3), (10, 2), (15, 1), (17, 5)], 1) == 15, "5 benches"
    assert park_benches([(4, 2), (7, 4), (14, 5), (23, 6), (31, 5), (37, 5), (47, 6), (55, 4)], 3) == 26, "5 of 8 benches"
    assert park_benches([(2, 8), (10, 4), (14, 10), (25, 7), (33, 2), (36, 1), (38, 1), (39, 3), (44, 4), (50, 9)], 2) == 36, "6 of 10 benches"
    print("Coding complete? Click 'Check' to earn cool rewards!")
