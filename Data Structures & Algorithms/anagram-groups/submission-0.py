class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        out_dict = {}

        for el in strs:
            el_sorted = "".join(sorted(el))
            if el_sorted in out_dict.keys():
                out_dict[el_sorted].append(el)
            else:
                out_dict[el_sorted] = [el]
            
        return [e for e in out_dict.values()]