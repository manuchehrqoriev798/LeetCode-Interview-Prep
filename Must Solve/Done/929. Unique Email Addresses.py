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
            name, dom = e.split("@")
            name1 = name.split("+")
            mainName = name1[0]
            mainName = mainName.replace(".", "")
            res.add(f"{mainName}@{dom}")
        
        return len(res)