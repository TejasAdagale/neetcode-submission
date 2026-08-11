
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # if len(strs) == 0:
        #     return []

        # if len(strs) == 1:
        #     return [strs]

        # result = []
        # used = [False] * len(strs)

        # # Create sorted versions for comparison
        # sorted_strs = []

        # for word in strs:
        #     sorted_strs.append(''.join(sorted(word)))

        # # Group anagrams
        # for i in range(len(strs)):

        #     if used[i]:
        #         continue

        #     temp = [strs[i]]
        #     used[i] = True

        #     for j in range(i + 1, len(strs)):

        #         if not used[j] and sorted_strs[i] == sorted_strs[j]:
        #             temp.append(strs[j])
        #             used[j] = True

        #     result.append(temp)

        # return result


        result = {}

        for word in strs:
            count = [0] * 26

            for ch in word:
                count[ord(ch) - ord('a')] += 1

            key = tuple(count)

            if key not in result:
                result[key] = []

            result[key].append(word)

        return list(result.values())