class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        res = set()
        
        for e in emails:
            name, dom = e.split("@")
            name = name.split("+")[0]
            mainName = name.replace(".", "")
            res.add(f"{mainName}@{dom}")

        return len(res)



class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        res = set()
        for e in emails:
            name, dom = map(str, e.split("@"))
            name = name.split("+")[0]
            # name = name.split("+")
            # mainName = name[0]
            mainName = name.replace(".", "")
            res.add(f'{mainName}@{dom}')
        
        return len(res)