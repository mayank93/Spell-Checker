#!/usr/bin/python
import sys
import re 
a=sys.argv[1]
a=re.findall('[a-zA-Z\']',a)
#a=re.findall('[^0-9]',a)
a=''.join(a)
#print a
alphabet='abcdefghijklmnopqrstuvwxyz\''
def dic11(features):
	model = {}
	for f in features:
		model[f] = 1
	return model
dic1=dic11(open('words.txt','r').read().split())
#def dic22(features):
#	model = {}
#	for f in features:
#		model[f] = 1
#	return model
#dic2=dic22(open('words.txt','r').read().split())
k=0
def gene1(w):
	splits=[]
	deletes=[]
	transposes=[]
	replaces=[]
	inserts=[]
	splits=[(w[:i], w[i:]) for i in range(len(w) + 1) if w]
	deletes=[a + b[1:] for a, b in splits if b]
#	deletemore=[a + b[2:] for a,b in splits if len(b)>1]
	transposes=[a + b[1] + b[0] + b[2:] for a, b in splits if len(b)>1]
	replaces=[a + c + b[1:] for a, b in splits for c in alphabet if b]
	inserts=[a + c + b     for a, b in splits for c in alphabet]     
#	return set(deletes+transposes+replaces+inserts+deletemore)
	return set(deletes+transposes+replaces+inserts)
def big(s):
	if(len(s)>=1):
		s=s[0].upper()+s[1:]
		return s
#def small(s):
#	if(len(s)>=1):
#		s=s[0].lower()+s[1:]
#:
#		return s
def gene2(word):
	return set(e2 for e1 in word for e2 in gene1(e1) if e2 in dic1)
def check(word,lis):
	temp=lis
	if len(lis)>5:
		temp=filter(lambda x: abs(len(x)-len(word)) in (0,1) ,lis)
	if len(temp)>=5:
		lis=temp
	i=0
	while len(temp)>5:
		if (i>=(len(word)-2)):
			break
		else:
			temp=filter(lambda x:x[i].lower()==word[i].lower(),lis)
		if len(temp)>=5:
			lis=temp
		else: 
			break
		i=i+1
	return lis
count=0
tab1=[]
tab2=[]

if a in dic1:
	print "The word is correctly spelt."
	k=1
if k==0:
 	s1=gene1(a)
	s1=list(s1)
	r1=map(lambda x: big(x),s1)
	s1=s1+r1
	s1=set(s1)
	tab1=filter(lambda x: x in dic1,s1)
	tab1=check(a,tab1)
	if (len(tab1)<5):
	 	s2=gene2(s1)
		r2=map(lambda x: big(x),s2)
		r2=set(r2)
		s2=s2|r2
		tab2=filter(lambda x: x in dic1,s2)
	tab=set(tab1+tab2)
	
#	if(re.findall(r'[a-z]+',a[0])==[]):
#		tab=map(lambda x:x[0].upper()+x[1:],tab)
#	else:
#		tab=map(lambda x:x[0].lower()+x[1:],tab)
	tab=check(a,tab)
	kk=1
	print "The word is incorrectly spelt. The nearest options are :"

	for i in tab:
		if kk>5:
			break
		print i
		kk+=1
#	print tab
