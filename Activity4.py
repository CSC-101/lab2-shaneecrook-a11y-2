from typing import Optional             # gain access to the Optional[X] type hint


def checked_access(L:list[int], idx:int) -> Optional[int]:
    test = idx >= 0 and idx < len(L)    # What is the value of test on each call? - True if index is valid, False otherwise
    if test:                            # What is this check preventing? - It is preventing index out-of-bounds errors
        return L[idx]
    else:
        return None


first = checked_access([1, 0, 1], 9)     # What is the value of first? - None (index out of range, test = False)
second = checked_access([1, 0, 1], 2)    # What is the value of second? 1 (valid index, test = True)
print()

def length_sum(L:list[str]) -> int:
    if len(L) > 2:
        result = len(L[0]) + len(L[1]) + len(L[2])    # For which call below is this statement evaluated
    elif len(L) > 1:                                  #   and what are the values being added? - Evaluated for first call: "this"(4) + "is"(2) + "the"(3) = 9
        result = len(L[0]) + len(L[1])                # For which call below is this statement evaluated
    elif len(L) > 0:                                  #   and what are the values being added? - Evaluated for third call: "another"(7) + "call"(4) = 11
        result = len(L[0])                            # For which call below is this statement evaluated
    else:                                             # and what are the values being added? - Evaluated for second call: "second call"(11)
        result = 0
    return result


first = length_sum(["this", "is", "the", "first", "call"]) #9
second = length_sum(["second call"]) #11
third = length_sum(["another", "call"]) #11
print()
def length_sum(L:list[str]) -> int:
    def surprising(L: list[str], other: str) -> list[str]:
        L.append(other.upper())
        return L

    words = ["this", "is", "confusing", "code."]
    first = surprising(words, "Avoid")
    second = surprising(words, "such.")
    # What is the value of words at this point? - words = ['this', 'is', 'confusing', 'code.', 'AVOID', 'SUCH.']
    # What are the values of first and second at this point? - first = same list as words, second = same list as words
    # What happened? - The function modifies the original list (lists are mutable), so both calls changed the same list.

print()
print(first, second, third)
print(words)
