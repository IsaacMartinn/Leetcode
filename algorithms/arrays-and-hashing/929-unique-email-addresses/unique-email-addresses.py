class Solution:
    def numUniqueEmails(self, emails) -> int:
        email_set = set()

        for email in emails:
            local, domain = email.split('@')
            local = local.split('+')[0]
            local = local.replace('.', '')
            email_set.add(local + "@" + domain)
                
        return len(email_set)