#!/usr/bin/env python3
def solve(senators):
    removals = []
    while not (senators[0] == 0 and len(set(senators)) == 1):
        largest_party_size = max(senators)
        # Two parties are equally largest
        if senators.count(largest_party_size) > 1:
            largest_party_index_1 = senators.index(largest_party_size)
            largest_party_index_2 = largest_party_index_1 + senators[largest_party_index_1+1:].index(largest_party_size) + 1
            if set(senators) in [set([1]), set([0,1])] and senators.count(1) == 3:
                senators[largest_party_index_1] -= 1
                removals.append(chr(65+largest_party_index_1))
            else:
                senators[largest_party_index_1] -= 1
                senators[largest_party_index_2] -= 1
                removals.append("{}{}".format(chr(65+largest_party_index_1), chr(65+largest_party_index_2)))
        else:
            num_parties_remaining = len([x for x in senators if x])
            if num_parties_remaining == 2:
                largest_party_index = senators.index(largest_party_size)
                senators[largest_party_index] -= 1
                removals.append(chr(65+largest_party_index))
            else:
                largest_party_index = senators.index(largest_party_size)
                senators[largest_party_index] -= 2
                removals.append(chr(65+largest_party_index)*2)
    return " ".join(removals)


num_tests = int(input())
for n in range(num_tests):
    input()
    answer = solve([int(x) for x in input().split()])
    print("Case #{}: {}".format(n+1, answer))