import sys
from itertools import combinations

l, n = map(int, sys.stdin.readline().split())
alphabets = list(map(str, sys.stdin.readline().split()))

consonants = []
vowels = []
# 자음, 모음 분리
for alphabet in alphabets:
    if alphabet in ['a','e','i','o','u']:
        vowels.append(alphabet)
    else:
        consonants.append(alphabet)

length = len(vowels) if len(vowels) < l-2 else l-2 #모음을 뽑는 최대 갯수 => 자음을 뽑는 최소 갯수 = l-length

combinationVowels = []
combinationConsonants = []
# 모음조합
for i in range(1,length+1):
    combinationVowels.append(list(combinations(vowels,i)))
# 자음조합
for i in range(l-length,l):
    combinationConsonants.append(list(combinations(consonants,i)))

results = []
# 만들기
for i in range(len(combinationConsonants)):
    for vowel in combinationVowels[i]:
        for consonant in combinationConsonants[len(combinationConsonants) - i -1]:
            result = ""
            for v in vowel:
                result = result + v
            for c in consonant:
                result = result + c

            results.append(''.join(sorted(result)))

for r in sorted(results):
    print(r)


"""
3 6
a t c i s w

4 6
a t c i s w

5 6
a t c i s w

5 7
a t c i s w e

7 15
a b c d e f g h i j k l m n o

8 15
a b c d e f g h i j k l m n o
"""
