from collections import defaultdict


class Solution:
    def groupThePeople(self, groupSizes):
        groups = defaultdict(list)

        for i, size in enumerate(groupSizes):
            groups[size].append(i)

        result = []

        for size, ids in groups.items():
            result.extend([ids[i:i + size] for i in range(0, len(ids), size)])

        return result
