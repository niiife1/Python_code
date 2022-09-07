from collections import deque
vowels = deque([x for x in input().split(" ")])
consonant = [x for x in input().split(" ")]

master_words = ['rose', 'tulip', 'lotus','daffodil']
real_word = []
find_words = []
while len(vowels) and len(consonant):
        vowels_word =  vowels.popleft()
        consonant_word = consonant.pop()
        for word in master_words:

                if vowels_word in word:
                        real_word.append(vowels_word)
                if consonant_word in word:
                        real_word.append(consonant_word)
                find_words =[x for x in word if x in real_word]
                combine_word = ''.join(find_words)
                if combine_word == word and len(combine_word) == len(word):
                        break
        if combine_word == word:
                break
if combine_word == word and len(combine_word) == len(word):
        print(f"Word found: {word}")
        if len(vowels) > 0:
                print(f"Vowels left: {(' '.join(map(str, vowels)))}")
        if len(consonant) > 0:
                print(f'Consonants left: {(" ".join(map(str, consonant)))}')
else:
        print('Cannot find any word!')
        if len(vowels)  > 0:
                print(f"Vowels left: {(' '.join(map(str,vowels)))}")
        if len(consonant) > 0:
                print(f'Consonants left: {(" ".join(map(str, consonant)))}')