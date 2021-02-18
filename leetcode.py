#Created By Dawn
class Solution:
    def maxDiff(self, num: int) -> int:
        num=str(num)
        a=len(num)
        def checkmax(num):
            if num[0]=="9":
                if len(num)==1:
                    return "9"
                return "9"+checkmax(num[1:])
            else:
                return num.replace(num[0],"9")
        def checkmin(num):
            if len(num)==1:
                if len(num)==a:
                    return "1"
                return num
            if num[0]=="1" or num[0]=="0":
                return num[0]+checkmin(num[1:])
            else:
                if len(num)==a:
                    return num.replace(num[0],"1")
                else:
                    return num.replace(num[0],"0")
        return int(checkmax(str(num)))-int(checkmin(str(num)))
