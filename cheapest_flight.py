# Author:Yi Sun(Tim) 2023-5-10

'''
As the input you get the flight schedule as an list, each element of which is the price of a direct flight between 2 cities (list of 3 elements - 2 city names as a string, and a flight price).
Planes fly in both directions and the price in both directions is the same. There is a possibility that there are no direct flights between cities.
Find the price of the cheapest flight between cities that are given as the 2nd and 3rd arguments. In case the flight can not be performed, return 0.
Input: 3 arguments: the flight schedule as a list of lists, city of departure and destination city as strings.
Output: The best price as integer.
'''

from collections import defaultdict
import heapq


def cheapest_flight(flight, start, goal):
    flight_dic = defaultdict(lambda: defaultdict(int))
    for dep, arr, cost in flight:
        flight_dic[dep][arr] = cost
        flight_dic[arr][dep] = cost
    que = [(0, start)]
    cost_dic = defaultdict(int)
    done = set()
    while True:
        if not que:
            return 0
        dep = heapq.heappop(que)[1]
        if dep == goal:
            return cost_dic[goal]
        if dep in done:
            continue
        for arr in flight_dic[dep]:
            new_cost = flight_dic[dep][arr] + cost_dic[dep]
            cost_dic[arr] = min(cost_dic[arr] or new_cost, new_cost)
            heapq.heappush(que, (cost_dic[arr], arr))
        done.add(dep)

if __name__ == '__main__':
    print("Example:")
    print(cheapest_flight([['A', 'C', 100],
  ['A', 'B', 20],
  ['B', 'C', 50]],
 'A',
 'C'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert cheapest_flight([['A', 'C', 100],
  ['A', 'B', 20],
  ['B', 'C', 50]],
 'A',
 'C') == 70
    assert cheapest_flight([['A', 'C', 100],
  ['A', 'B', 20],
  ['B', 'C', 50]],
 'C',
 'A') == 70
    assert cheapest_flight([['A', 'C', 40],
  ['A', 'B', 20],
  ['A', 'D', 20],
  ['B', 'C', 50],
  ['D', 'C', 70]],
 'D',
 'C') == 60
    assert cheapest_flight([['A', 'C', 100],
  ['A', 'B', 20],
  ['D', 'F', 900]],
 'A',
 'F') == 0
    assert cheapest_flight([['A', 'B', 10],
  ['A', 'C', 15],
  ['B', 'D', 15],
  ['C', 'D', 10]],
 'A',
 'D') == 25
    print("Coding complete? Click 'Check' to earn cool rewards!")