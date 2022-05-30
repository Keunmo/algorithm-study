# https://leetcode.com/problems/unique-email-addresses/

def numUniqueEmails(emails):
    addrlist = []
    for i in emails:
        atidx = i.find('@')
        local = i[:atidx]
        domain = i[atidx:]
        local = local.replace('.','')
        if local.find('+') != -1:
            local = local[0:local.find('+')]
        addrlist.append(local+domain)
        print(addrlist)
    print(len(addrlist))
    set1 = set(addrlist)
    print(set1)
    print(len(set1))
    return len(set1)

emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]

numUniqueEmails(emails)