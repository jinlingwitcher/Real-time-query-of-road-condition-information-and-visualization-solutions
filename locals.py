# -*- coding: utf-8 -*- 
import urllib
import requests
from datetime import datetime
import time

nums=0
try:
	while True:
		f=open(r'C:\Users\newlife\Desktop\c.txt','a+')
		datatime = datetime.now().strftime("%Y-%m-%d %H_%M_%S")
		queryStr2 = 'https://restapi.amap.com/v3/weather/weatherInfo?city=320100&key=yourkey'
		encodedStr2 = urllib.parse.quote(queryStr2, safe="/:=&?#+!$,;'@()*[]")
		w=requests.get(encodedStr2)
		w=w.text
		f.write('\n')
		f.write('\n')
		f.write(datatime)
		f.write('\n')
		b1=w.rfind("weather")
		b2=w.rfind("temperature")
		b3=w.rfind("winddirection")
		b4=w.rfind("windpower")
		if w[b1+11] != '\"':
			f.write(w[b1+10])
			f.write(w[b1+11])
		else:
			f.write(w[b1+10])
		f.write(' ')
		f.write(w[b2+14])
		f.write(w[b2+15])
		f.write(' ')
		f.write(w[b3+16])
		f.write(w[b3+17])
		f.write(' ')
		f.write(w[b4+12])
		f.write(w[b4+13])
		f.write(' ')
		f.write('\n')
		print('weather done!')


		locals=[]
		s1=118.773164 #南京医科大学左上角 
		s2=32.045922
		n=0
		for i in range(30):
			for j in range(30):
				ss2=str(s2-i*0.001190)
				ss1=str(s1+j*0.001190)
				ss3=ss1+','+ss2
				locals.append(ss3)		#118.823181	
		print('locals are ready')
		for local in locals:
			queryStr1 = 'https://restapi.amap.com/v3/traffic/status/circle?location='+local+'&radius=40&key=yourkey'
			encodedStr1 = urllib.parse.quote(queryStr1, safe="/:=&?#+!$,;'@()*[]")
			r=requests.get(encodedStr1)
			r=r.text
			a=r.rfind("status")
			if r[a+9]==']':
				f.write('0')
			else:
				f.write(r[a+9])
			n=n+1
			print(n)
			if n==30:
				f.write('\n')
				n=0
				continue
			f.write(',')
		f.close()
		print (time.strftime('%H:%M:%S',time.localtime(time.time())))
		print('Succeed!')
		nums=nums+1
		if nums==33:#每20min查一次，一共33次，连续11h
			break
		time.sleep(1200)
except KeyboardInterrupt:
	print('finished!')
