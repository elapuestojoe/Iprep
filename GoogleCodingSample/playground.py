def solution(L):
    
    emailHashMap = {}
    duplicatedEmailsGroup = 0

    for email in L:
        #StringBuffer
        formattedEmail = ""

        name = list()
        domain = list()
        #Formatting could be done using string split function in Python:
        # name, domain = email.split("@")
        # name = name.split("+")[0]
        # but I chose to do it this way to explain better my thought process

        plusFound = False
        domainFound = False
        for character in email:
            if(character == "@"):
                domainFound = True
            elif(character == "+"):
                plusFound = True
            
            else:
                if(domainFound):
                    domain.append(character)
                
                elif(not plusFound and character != "."):
                    name.append(character)
        
        strName = "".join(name)
        strDomain = "".join(domain)
        formattedEmail = strName + "@" + strDomain
        if(formattedEmail not in emailHashMap):
            emailHashMap[formattedEmail] = 1
        else:
            if(emailHashMap[formattedEmail] == 1):
                duplicatedEmailsGroup += 1
            emailHashMap[formattedEmail] += 1
    return duplicatedEmailsGroup


# l = ["a.b@example.com", "x@example.com", "ab@example.com"]
# print(solution(l))

a =  ['a.b@example.com', 'x@example.com', 'x@exa.mple.com', 'ab+1@example.com', 'y@example.com', 'y@example.com', 'y@example.com']
print(solution(a))

def splitS(s):
    name, email = s.split("@")
    name = name.split("+")[0]

    print(name,email)

for s in a:
    splitS(s)