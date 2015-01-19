c=3

f=[[]for i in range(0,c)]
for i in range(0,c):
	f[i]=open(str(i)+".res")
a=[[[]for i in range(0,8000) ] for j in range(0,c)]
ans=[0]*8000
count=0
lll=0
for i in range(0,c):
	for s in f[i]:
		a[i][count]=int(s)
		count+=1
	lll=count
	count=0

def get_ans(table):
	tmp=0
	count=0
	for i in range(0,33):
		if(table[i]>tmp):
			tmp=table[i]
			count=i
	return count

def fill_ans(count):
	table=[0]*33
	for i in range(0,count):
		for j in range(0,c):
			#print i,j
			table[a[j][i]]+=1
		ans[i]=get_ans(table)
		for j in range(0,c):
			table[a[j][i]]=0
		count+=1
def fill_ans_track1(count):
	b=4
	table=[0]*33
	for i in range(0,count):
		for j in range(0,c):
			tmp=a[j][i]
			table[tmp]+=1
			if(tmp<12):
				b+=1
			
			if(tmp>=12):
				if(tmp<=21):
					table[tmp+10]+=0.9
				else:
					table[tmp-10]+=0.9
			'''
			
			print j,tmp
			if(tmp==1):
				table[21]+=0.9
			if(tmp==21):
				table[1]+=0.9
			'''

		if(b<2):
			for i in range(0,12):
				table[i]=0
		ans[i]=get_ans(table)
		for j in range(0,33):
			table[j]=0
		count+=1


'''
f4=open("../test1.small.dat")
count=0
for s in f4:
	ans[count]=int(s.split(" ")[0])
	count+=1
res=0
for i in range(0,count):
	if(ans[i]!=d[i]):
		res+=1
print float(res)/count
'''
def output(ans,count):
	o=''
	for j in range(0,count):
		o+=(str(ans[j])+'\n')
	out=open("aggregation_ans.res",'w')
	out.write(o)

fill_ans_track1(lll)
output(ans,lll)