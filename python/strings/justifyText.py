def splitWords(words, curr, L):
    if len(words) == 1:
        return words[0] + " " * (L - curr)
    to_all = (L - curr) // (len(words) - 1)
    additional = (L - curr) % (len(words) - 1)
    res = words.pop(0)

    for word in words:
        res += " " * (to_all + 1)
        if additional > 0:
            res += " "
            additional -= 1
        res += word
    return res

def fullJustify(A, B):

    result = []
    curr = 0
    tmp = []
    for word in A:
        if not word:
            continue
        if curr + len(word) <= B:
            curr += len(word) + 1
            tmp.append(word)
        else:
            result.append(splitWords(tmp, curr - 1, B))
            tmp = [word]
            curr = len(word) + 1
    if curr:
        result.append(' '.join(tmp) + ' ' * (B - curr + 1))
    return result
        

words = ["This", "is", "an", "example", "of", "text", "justification."]
print(fullJustify(words, 16))

# words = ["Two", "words."]
# print(textJustification(words, 11))

words = [ "What", "must", "be", "shall", "be." ]
r = fullJustify(words, 12)
for line in r:
    print(len(line), line)