def smallest(n: float, m: float) -> float:
   if n < m:
      return n             # For which calls below is this statement evaluated? - Evaluated when n < m
   else:
      return m


first = smallest(3, 2)     # What is the value of first? the value of first is 2
second = smallest(2, 2)    # What is the value of second? Is this a reasonable result? Why or why not? The value of second is 2. This is reasonable because when n and m are equal, the condition n < m is false, so the function returns m, which is still the same value.
print()

def function2(a:int, b:int, c:int) -> int:
    if a > b and a > c:
        return a - b             # In general, when will a call to this function evaluate this statement?
    elif b > c:                               # - It will evauluate the statement when a is the largest
        return b + c             # In general, when will a call to this function evaluate this statement?
    else:                                     # - It will evaluate the statement when b > c and a is not largest
        return 2 * c             # In general, when will a call to this function evaluate this statement?
                                              # - It will evaluate the statement when c is largest OR ties

answer1 = function2(3, 2, 1)     # What is the value of answer1?  # 1
answer2 = function2(2, 3, 1)     # What is the value of answer2?  # 4
answer3 = function2(2, 1, 3)     # What is the value of answer3?  # 6
print()
print(first)
print(second)
print(answer1, answer2, answer3)