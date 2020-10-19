# https://leetcode.com/explore/challenge/card/october-leetcoding-challenge/561/week-3-october-15th-october-21st/3498/

# All DNA is composed of a series of nucleotides abbreviated as 'A', 'C', 'G', and 'T', for example: "ACGAATTCCG". When studying DNA, it is sometimes useful to identify repeated sequences within the DNA.

# Write a function to find all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.

import collections

def findRepeatedDnaSequences(s):
    if len(s) <= 10: return []

    d = collections.Counter()
    i = 10
    while i <= len(s):
        substr = s[i - 10: i]
        d[substr] += 1
        i += 1

    res = [substr for substr, count in d.items() if count > 1]
    return res


print(findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT")) # ["AAAAACCCCC","CCCCCAAAAA"]
print(findRepeatedDnaSequences("AAAAAAAAAAA")) # ["AAAAAAAAAA"]
