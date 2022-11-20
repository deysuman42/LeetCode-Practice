class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        
        h = set()
       
        
        for e in emails:
            local, domain = e.split('@')
            local = local.split("+")[0]
            local = local.replace(".","")
            email = local + '@' + domain
            h.add(email)
        
        return len(h)
        
