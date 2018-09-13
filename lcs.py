a="ABCDGHIROOOOK"
#b="AEDFHIRK"
b="XYZ"
l1 = len(a)
l2 = len(b)

x = min(l1,l2)

print x
lcs = ""
i=0
j=0
while i<l1 and j<l2:
	if a[i] == b[j]:
		lcs +=a[i]
		i=i+1
		j=j+1
	else:
		j=j+1
	if j == l2:
		j = 0
		i=i+1
		
#for i in range(0, x):
	
print lcs
	
