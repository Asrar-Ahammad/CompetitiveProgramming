from collections import Counter

def canConstruct(ransomNote: str, magazine: str) -> bool:
        r = Counter(ransomNote)
        m = Counter(magazine)
        print(r,m)
        if r&m == r:
            return True
        return False

ransomNote = "a"
magazine = "b"

ransomNote = "aa"
magazine = "ab"

ransomNote = "aa"
magazine = "aab"

ransomNote ="fihjjjjei"
magazine = "hjibagacbhadfaefdjaeaebgi"
print(canConstruct(ransomNote, magazine))