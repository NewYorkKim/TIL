# class Solution:
#     def hIndex(self, citations: List[int]) -> int:
#         citations.sort()
#         h = 0

#         while True:
#             tmp = 0
#             for citation in citations:
#                 if citation > h:
#                     tmp += 1
            
#             if tmp <= h:
#                 break
#             else:
#                 h += 1
        
#         return h

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        h = 0

        for i in range(len(citations)):
            if citations[i] >= i + 1:
                h += 1
        
        return h