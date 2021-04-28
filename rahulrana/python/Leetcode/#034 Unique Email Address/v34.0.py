# https://leetcode.com/problems/unique-email-addresses/

# to filter "." and "+" before @ to find out uniques
def numUniqueEmails(emails):
    email_list = []
    for email in emails:
        e_split = email.split('@')
        left = ''
        skip = False
        for char in e_split[0]:
            if not skip:     
                if char == '.':
                    True
                elif char == '+':
                    skip = True
                else:
                    left += char
        email_list.append(left + "@" + e_split[1])
    print(set(email_list))
    return len(set(email_list))

emails = ["test.emailalex@leetcode.com","test.e.mailbob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
print(numUniqueEmails(emails))

# 68ms; Faster than 17%
# 14.2MB; Less than 65%