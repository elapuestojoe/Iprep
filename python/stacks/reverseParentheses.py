'''
You have a string s that consists of English letters, punctuation marks, whitespace characters, and brackets. 
It is guaranteed that the parentheses in s form a regular bracket sequence.

Your task is to reverse the strings contained in each pair of matching parentheses, starting from the innermost pair. 
The results string should not contain any parentheses.

Example

For string s = "a(bc)de", the output should be
reverseParentheses(s) = "acbde".
'''

def reverseParentheses(s):
    result = []
    stringBuffers = []
    for char in s:
        if(char == '('):
            stringBuffers.append([])
        elif(char == ")"):
            
            sBuffer = stringBuffers.pop()
            
            if(len(stringBuffers) > 0):
                while(len(sBuffer) != 0):
                    stringBuffers[-1].append(sBuffer.pop())
            else:
                while(len(sBuffer) != 0):
                    result.append(sBuffer.pop())
        else:
            if(len(stringBuffers) > 0):
                stringBuffers[-1].append(char)
            else:
                result.append(char)
    return "".join(result)


print(reverseParentheses("co(de(fight)s)"))