from itertools import combinations, permutations

data = ['a', 'b', 'c']

print(list(combinations(data, r=len(data))))
print('-' * 60)
print(list(permutations(data, r=len(data))))

#   radar   
#   Go hang a salami, I'm a lasagna hog
#   otto    
#   ['a', 'b', 'c']  not a palindrome
#   ['a', 'b', 'a']  is a palindrome
