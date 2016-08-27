class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        pattern_to_token = {}
        token_mapped = sets.Set()
        
        tokens = str.split(' ')
        if len(pattern) != len(tokens):
            return False
            
        for i in range(len(pattern)):
            if pattern[i] not in pattern_to_token:
                if tokens[i] in token_mapped: # token already been mapped
                    return False
                pattern_to_token[pattern[i]] = tokens[i] # add new mapping
                token_mapped.add(tokens[i])
            else:
                if pattern_to_token[pattern[i]] != tokens[i]: # already mapped to a different token
                    return False
        return True
