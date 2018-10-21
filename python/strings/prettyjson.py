'''


Pretty print a json object using proper indentation.

    Every inner brace should increase one indentation to the following lines.
    Every close brace should decrease one indentation to the same line and the following lines.
    The indents can be increased with an additional ‘\t’

Example 1:

Input : {A:"B",C:{D:"E",F:{G:"H",I:"J"}}}
Output : 
{ 
    A:"B",
    C: 
    { 
        D:"E",
        F: 
        { 
            G:"H",
            I:"J"
        } 
    }     
}

Example 2:

Input : ["foo", {"bar":["baz",null,1.0,2]}]
Output : 
[
    "foo", 
    {
        "bar":
        [
            "baz", 
            null, 
            1.0, 
            2
        ]
    }
]

[] and {} are only acceptable braces in this case.

Assume for this problem that space characters can be done away with.

Your solution should return a list of strings, where each entry corresponds to a single line. The strings should not have “\n” character in them.

'''

def prettyJSON(A):
    solutions = []
    buffer = []
    tabs = 0
    for char in A:
        if(char in ["[", "{"]):
            if(len(buffer) > 0):
                solutions.append("".join(buffer))
            buffer = []
            for i in range(tabs):
                buffer.append("\t")
            buffer.append(char)
            solutions.append("".join(buffer))
            buffer = []
            tabs+=1

        elif(char in ["]", "}"]):
            if(len(buffer) > 0):
                solutions.append("".join(buffer))
            buffer = []
            tabs-=1
            for i in range(tabs):
                buffer.append("\t")
            buffer.append(char)
            solutions.append("".join(buffer))
            buffer = []
        elif(char == ","):
            if(len(buffer)==0):
                solutions[-1] += ","
            else:
                buffer.append(char)
                solutions.append("".join(buffer))
                buffer = []
        elif(char != " "):
            if(len(buffer)==0):
                for i in range(tabs):
                    buffer.append("\t")
            buffer.append(char)
    return solutions
a = '["foo",  {"bar":["baz",null,1.0,2],[1,2]}]'
aAnswer = prettyJSON(a)
for i in aAnswer:
    print(i)

b = '{A:"B",C:{D:"E",F:{G:"H",I:"J"}}}'
bAnswer = prettyJSON(b)
for i in bAnswer:
    print(i)