class Solution(object):
    def groupAnagrams(self, strs):
        output = {}
        for i in strs:
            word = "".join(sorted(i))
            if word in output:
                output[word].append(i)
            else:
                output[word] = [i]
            
        return list(output.values())

        
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        