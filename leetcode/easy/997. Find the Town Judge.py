'''
# It's getting to complicated for an easy problem.
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        untrusting = set(range(1, n + 1))
        untrusted = set(range(1, n + 1))

        for trust_relationship in trust:
            if trust_relationship[0] in untrusting: 
                untrusting.remove(trust_relationship[0])
            
            if trust_relationship[1] in untrusted:
                untrusted.remove(trust_relationship[1])
        
        satisfying_criteria = set()
        
        for untrust in untrusting:
            if untrust not in untrusted:
                satisfying_criteria.add(untrust)

        return -1 if len(satisfying_criteria) != 1 else satisfying_criteria.pop()
        
'''

from collections import defaultdict
from typing import List


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trust_map = defaultdict(int)
        untrusting = set(range(1, n+1))

        for trust_item in trust:
            trust_map[trust_item[1]] += 1
            
            if trust_item[0] in untrusting:
                untrusting.remove(trust_item[0])
        
        possible_answers = []
        
        for untrust in untrusting:
            if trust_map[untrust] == n - 1:
                possible_answers.append(untrust)
        
        return -1 if len(possible_answers) != 1 else possible_answers.pop()
