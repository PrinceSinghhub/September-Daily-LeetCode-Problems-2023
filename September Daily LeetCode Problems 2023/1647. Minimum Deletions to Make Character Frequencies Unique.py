class Solution:
    def minDeletions(self, s: str) -> int:
        d = dict()
        for i in s:
            if(i in d):
                d[i]+=1
            else:
                d[i]=1
        arr = [0]*(len(s)+1)
        out = 0
        for key,value in d.items():
            if(arr[value]==0):
                arr[value] = key
            else:
                while(value>=0):
                    if(arr[value]!=0 and value==0):
                        break
                    value -= 1
                    out += 1
                    if(arr[value]==0):
                        arr[value] = key
                        break
        return out