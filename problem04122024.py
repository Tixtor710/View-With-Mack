res=[0,0]
for i in (len(a)):
        
 if a[i]>b[i]:
    res[0]+=1            
 elif a[i]<b[i]:
    res[1]+=1
    
return list(res)