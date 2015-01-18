import cv2
import numpy as np
from matplotlib import pyplot as plt


f=[[]for i in range(0,3)] 
f[2]=open("ml14fall_test2_no_answer.dat")

f[1]=open("ml14fall_test1.dat")
f[0]=open("ml14fall_train.dat")
deal=11
out=[[]for i in range(0,3)]

out[2]=open('test2_r'+str(deal)+'.dat',"w")
out[1]=open('test1_r'+str(deal)+'.dat',"w")
out[0]=open('train_r'+str(deal)+'.dat',"w")

height=122
width=105
lastx=0
lasty=0
color=0
count=0








def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def show_image(image):
	cv2.imshow("image",image)
	cv2.waitKey(0)
	cv2.destroyAllWindows()

def set_black(image):
	image[:,:]=0

def check_line(img,i,j,k,o):
	if(o==0):
		for m in range(i,i-k):
			if(img[m,j]!=0 and m !=i):
				return True
	else:
		for m in range(j,j-k):
			if(img[i,m]!=0 and m != j):
				return True
	return False


def check(img,i,j,k):
	flag=0

	if(check_line(img,i,j,k,0)):
		flag+=1
	if(check_line(img,i,j,-k,0)):
		flag+=1


	if(check_line(img,i,j,k,1)):
		flag+=1
	if(check_line(img,i,j,-k,1)):
		flag+=1

def blur(img,m,n,k):
	global width
	global height
	for i in range(k,n-k):
		for j in range(k,m-k):
			if(img[i,j]!=0):
				for m in range(-1,2):
					for n in range(-1,2):
						if(img[i+m,j+n]!=0):
							img[i+m,j+n]=255
				#print i,j


def denoise(img,m,n,k):
	global width
	global height
	for i in range(k,m-k):
		for j in range(k,n-k):
			if(check(img,i,j,k)<2 ):
				img[i,j]=0
				#print i,j





def average(img,k):
	c=0
	global height
	global width
	blank_image=np.zeros((height,width),np.uint8)
	for i in range(1,height-1):
		for j in range(1,width-1):
			for m in range(-1,2):
				for n in range(-1,2):
					c+=img[i+m,j+n]

			c=int(c/9)
			if(c>k):
				blank_image[i,j]=255
				#print i,j,c
			else:
				blank_image[i,j]=0
			c=0
	return blank_image


def enhancment(img,k):

	tmp=0
	color=0
	for i in range(0,height-k):
		for j in range(0,width-k):
			for l in range(0,k):
				if(color<img[i,j+l]):
					color=img[i,j+l]
					tmp=l
			for l in range(0,k):
				if(img[i,j+tmp]!=0):
					img[i,j+tmp]=255
			
				else:
					img[i+tmp,j]=0
			tmp=0
			color=0

	for i in range(0,height-k):
		for j in range(0,width-k):
			for l in range(0,k):
				if(color<img[i+l,j]):
					color=img[i+l,j]
					tmp=l
			for l in range(0,k):
				if(img[i+tmp,j]!=0):
					img[i+tmp,j]=255
				else:
					img[i+tmp,j]=0
			tmp=0
			color=0


def draw(s,arr):
	global height
	global width
	test=np.zeros((height,width),np.uint8)
	originy=-1
	global lasty
	global lastx
	originx=0
	l=[0]*(width)
	m=[0]*height
	position=0


	#set_black(blank_image)
	#arr=s.split(" ")
	for i in range(0,width):
		#print l[i],i,i
		l[i]=0
	
	for tmp in arr:
		if(is_number(tmp)):
			continue
		else:
			position=int(tmp.split(":")[0])-1
			if(position<12899):
				
			
				y=int (position/width)
				if(m[y]==-1):
					m[y]=1
				if(m[y]==0):
					m[y]=-1


				x=(int((position)%width))%width
				
				l[x]=1
				
			#else:
				#print "!!!!!!!!!",x
	flag=0
	for i in range(0,height):
		if(m[i]==-1):
			m[i]=0
	
	local=0
	mark=0
	
	'''
	for i in range(0,104):
		if(l[i]==1 and flag==0):
			flag=-1
			mark=i
		if(flag == (-1) and l[i]==0):
			flag=-2
		if(flag==-2 and l[i]==0):
			local+=1
		if(flag==-2 and l[i]==1):
			
			if(local>10):
				flag = i
				break	
			else:
				local=0
				flag=-1
		#print i,flag,local,l[i]
	if(flag<0):
		flag=mark
	originx=flag
	#print originx,local
	'''
	count=0
	for i in range(0,width):
		#print l[i],i
		if(i==0):
			if(l[i]==1):
				l[i]=0
			else:
				l[i]=1
				count+=1
		else:
			if(l[i]==0):
				l[i]=l[i-1]+1
				count+=1
			else:
				if(count>0 and count<5):
					l[i]=l[i-1]-count
					count=0
				else:
					l[i]=l[i-1]
		#print l[i]
	count=0
	for i in range(0,height):
		#print l[i],i
		if(i==0):
			if(m[i]==1):
				m[i]=0
			else:
				m[i]=1
				count+=1
		else:
			if(m[i]==0):
				m[i]=m[i-1]+1
				count+=1
			else:
				if(count>0 and count<5):
					m[i]=m[i-1]-count
					count=0
				else:
					m[i]=m[i-1]
		#print l[i]
	
	scan=-2
	count=-1
	flag=0
	'''
	for i in range(0,width):
		if(scan!=l[i]):
			if(flag==1):
				count=0

				flag=0
			else:
				count+=1
			scan=l[i]
		else:
			
			if(count<5):
				if(flag==0):
					l[i-1]-=count
					l[i]-=count
				else:
					l[i]-=count
			flag=1
	'''
	lastx=width-l[width-1]
	lasty=height-m[height-1]
	yy=lasty
	if(lasty<10):
		lasty=15
	blank_image = np.zeros((lasty+1,lastx+1,1), np.uint8)
	for tmp in arr:
		if(is_number(tmp)):
			continue
		else:
			
			position=int(tmp.split(":")[0])-1
			if(position<12899):
				y=int (position/width)
				x=(int((position)%width))%width
				flag=x
				
				x-=l[x]
				y-=m[y]
				x%=width
				color=int(float(tmp.split(":")[1])*255)
				
				#if(y<121 and color>50):
				if(y<=lasty and y>=0 and x>=0 and x<=lastx and color>20):	
					blank_image[y,x]=color
				
				#print x,y,lastx,originy,lasty,position,blank_image[y,x]#,lastytmp
					#exit()
			
			#print i,color,l[x]
	#print lastx
	return blank_image,lastx,lasty

def ske(image):
	img = image
	size = np.size(img)
	skel = np.zeros(img.shape,np.uint8)
 
	ret,img = cv2.threshold(img,127,255,0)
	element = cv2.getStructuringElement(cv2.MORPH_CROSS,(3,3))
	done = False
 
	while( not done):
	    eroded = cv2.erode(img,element)
	    temp = cv2.dilate(eroded,element)
	    temp = cv2.subtract(img,temp)
	    skel = cv2.bitwise_or(skel,temp)
	    img = eroded.copy()
	 
	    zeros = size - cv2.countNonZero(img)
	    if zeros==size:
	        done = True
	 
	#output(skel)
	return skel


def resize(img,h,w):
	blank_image = np.zeros((height,width,1), np.uint8)

	dsize=(w,h)
	return cv2.resize(img, dsize, blank_image,interpolation = cv2.INTER_CUBIC)
	

def small(img,m,n):
	tmp=0
	for i in range(int (m*height*0.25),int((m+1)*height*0.25)):
		for j in range(int (n*width*0.25),int((n+1)*width*0.25)):
			if(img[i,j]!=0):
				tmp+=1
	res=float(tmp)/(height*width*0.25*0.25)
	return res


def output(out,img,tmp,add1,add3,add2,add4):
	global s
	arr=s.split(" ")
	o=""
	zi=int(arr[0])
	o+=str(zi)	
	o+=" "
	for y in range(0,width):
		for x in range(0,height):
			if(x<105 and  y < 122):
				if(img[x,y]>1):
					
					o+=(str(y*height+x+1)+":"+str(float(img[x,y])/255.0)+" ")
			else:
				print "!!!!!!!"
				#print x,y,y*104+x
	
	'''
	o+=(str(height*width+2)+":"+str(tmp/1000.0)+' ')
	o+=(str(height*width+3)+":"+str(add1)+' ')
	o+=(str(height*width+4)+":"+str(add3)+' ')
	o+=(str(height*width+5)+":"+str(float(xx)/yy)+' ')
	
	for i in range(0,16):

		o+=(str(height*width+5+i+1)+":"+str(small(img,i/4,i%4))+' ')

	
	

	for i in range(0,height):
		tmp=0
		for j in range(0,width):
			if(img[i,j]>0):
				tmp+=1
		u=tmp
		tmp/=float(width)
		tmp*=u
		o+=(str(height*width+25+i)+":"+str(tmp)+' ')
		
	for i in range(0, width):
		tmp=0
		for j in range(0,height):
			if(img[j,i]>0):
				tmp+=1
		u=tmp
		tmp/=float(height)
		tmp*=u
		o+=(str(height*width+25+height+i)+":"+str(tmp)+' ')
	#print w
	#print h
	
	o+=(str(height*width+height+width+30)+":"+str(add2)+' ')
	o+=(str(height*width+height+width+31)+":"+str(add4))
	'''
	o+='\n'
	global count
	if((count%100)==0):
		print count
	count+=1
	
	out.write(o)
	

def plain_draw(s):
	global height
	global width
	arr=s.split(" ")
	test=np.zeros((height,width),np.uint8)
	
	for tmp in arr:
		if(is_number(tmp)):
			continue
		else:
			position=int(tmp.split(":")[0])-1
			y=int (position/width)
			x=(int((position)%width))
			test[y,x]=float(tmp.split(":")[1])*255
	return test
			
			
	


'''
for s in f:
	
	#if(count>2	):
		#break
	count+=1
	img=draw(s);
	#show_image(img)

	#img=ske(img)
	#show_image(img)
	img=resize(img)
	#show_image(img)
	blur(img,width,height,1)
	#show_image(img)
	img=ske(img)
	#show_image(img)
	#denoise(img,height,width,2)
	#print img.shape
	#show_image(img)
	#average(img,10)
	#average(img,45)
	img=ske(img)
	
	output(img)
	#show_image(img)
	#img=average(img)
	#show_image(img)
	#blur(img,width,height,3)
	
	
	#enhancment(img,6)
	#show_image(img)
'''
def bluro(img):
	kernel = np.ones((5,5),np.float32)/25
	dst = cv2.filter2D(img,-1,kernel)
	global width
	global height

	'''
	for i in range(0,height):
		for j in range(0,width):
			if(dst[i,j]>200):
				dst[i,j]=255
			else:
				if(dst[i,j]>50):
					dst[i,j]+=100
	
	'''
	
	plt.subplot(121),plt.imshow(img),plt.title('Original')
	plt.xticks([]), plt.yticks([])
	plt.subplot(122),plt.imshow(dst),plt.title('Averaging')
	plt.xticks([]), plt.yticks([])
	plt.show()
	
	return dst
def sp_around(i,j,m,n,img):
	size=img.shape
	y=(i+m)%size(0)
	x=(j+n)%size(1)
def sp(img):
	size=img.shape
	res=0
	for i in range (0,size[0]):
		for j in range(0,size[1]):
			if(img[i][j]>0):
				for m in range(-1,2):
					for n in range(-1,2):
						res+=sp_around(i,j,m,n,img)
			if(res<2):
				img[i][j]=0

def en(img):
	size=img.shape
	count=0
	color=0
	for i in range(0,size[0]):
		for j in range(0,size[1]):
			if(img[i][j]!=0):
				count+=1
				
				color+=img[i][j]
	if(count!=0):
		color/=count
	else:
		color=100000
	ave=color
	color*=0.722
	for i in range(0,size[0]):
		for j in range(0,size[1]):
			if(img[i][j]!=0):
				tmp=img[i][j]
				if(tmp>30):
					img[i][j]=255
				
	return img
mmm=''

def calc(img):
	tmp=int(s.split(" ")[0])
	count=0
	for i in range(0,height):
		for j in range(0,width):
			if(img[i,j]!=0):
				count+=1
	ans[tmp][0]+=count
	ans[tmp][1]+=1

def get_count(img):
	count=0
	for i in range(0,height):
		for j in range(0,width):
			if(img[i,j]!=0):
				count+=1
	return count
def get_add1(img):
	count=0
	m=[0]*width
	for i in range(0,height):
		for j in range(0,width):
			if(img[i,j]!=0):
				m[j]+=1
	res=0.
	for k in m:
		if(k==1):
			res+=1
	return res/width
def get_add2(img):
	count=0
	m=[0]*height
	for i in range(0,width):
		for j in range(0,height):
			if(img[j,i]!=0):
				m[j]+=1
	res=0.
	for k in m:
		if(k==1):
			res+=1
	return res/height

def get_add3(img):
	count=0
	m=[0]*width
	for i in range(0,height):
		for j in range(0,width):
			if(img[i,j]!=0):
				m[j]+=1
	res=0.
	for k in m:
		if(k>=0.7*height):
			res+=1
	return res/width

def get_add4(img):
	count=0
	m=[0]*height
	for i in range(0,width):
		for j in range(0,height):
			if(img[j,i]!=0):
				m[j]+=1
	res=0.
	for k in m:
		if(k>=0.7*height):
			res+=1
	return res/height

ans=[[0.0 for x in range(2)] for x in range(32)]


for mmm in range(0,3):

	for s in f[mmm]:
		arr=s.split(' ')
		

		img,xx,yy=draw(s,arr)
		


		#show_image(img)
		
		
		height=24
		width=21
		#img=bluro(img)
		img=resize(img,height,width)
		
		
		#output(img)
		
		img=ske(img)
		
		

		#show_image(img)
		#img=bluro(img)
		#en(img)
		
		#img=ske(img)
		#show_image(img)
		
		#show_image(img)
		'''
		tmp=get_count(img)
		add1=get_add1(img)
		add3=get_add3(img)
		'''
		
		tmp=0
		add1=0
		add3=0
		
		#show_image(img)
		
		output(out[mmm],img,tmp,add1,add3,get_add2(img),get_add4(img))
		height=122
		width=105
		'''
		calc(img)
	for i in range(0,32):
		ans[i][0]/=ans[i][1]
	outans=open("skeans.dat")
	for i in range(0,32):
		o=str(i)+" "+str(ans[i][0])+" "+str(ans[i][1])+'\n'
		outans.write(o)
		'''
		
