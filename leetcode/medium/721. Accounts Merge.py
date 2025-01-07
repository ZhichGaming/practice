from collections import defaultdict
from typing import List


# I didn't figure this out by myself, I got the idea from Neetcode. I implemented it myself though.
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        email_map: dict[str, int] = {}

        rank: dict[str, int] = {}
        parent: dict[str, str] = {}

        def find(node: str) -> str:
            if parent[node] != node:
                return find(parent[node])
            
            return node

        for i, account in enumerate(accounts):
            root_email = None

            for email in account[1:]:
                if root_email is None:
                    root_email = email
                    
                    if email not in parent:
                        parent[email] = root_email
                        rank[root_email] = 1
                    else:
                        root_email = find(email)

                if email not in email_map:
                    email_map[email] = i
                    parent[email] = root_email

                    if rank[root_email] < 2:
                        rank[root_email] += 1
                else:
                    root1 = find(email)
                    root2 = find(root_email)

                    if parent[root1] != parent[root2]:
                        if rank[root1] > rank[root2]:
                            parent[root2] = root1
                        elif rank[root1] < rank[root2]:
                            parent[root1] = root2
                        else:
                            parent[root2] = root1
                            rank[root2] += 1

        email_groups = defaultdict(list)

        for email in email_map:
            root_email_index = email_map[find(email)]
            email_groups[root_email_index].append(email)
        
        res = []

        for i, emails in email_groups.items():
            res.append([accounts[i][0]] + sorted(emails))
        
        return res
    