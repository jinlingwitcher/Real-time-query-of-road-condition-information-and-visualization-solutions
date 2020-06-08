# -*- coding: utf-8 -*- 
import urllib
import requests
from datetime import datetime
import time

f=open(r'C:\Users\newlife\Desktop\sql.txt','a+')
datatime = datetime.now().strftime("%Y-%m-%d %H_%M_%S")

try:
	while True:

		queryStr2 = 'https://restapi.amap.com/v3/weather/weatherInfo?city=320100&key=060fc55def82a6e495f4bb0d789689d1'
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



		locals=[]
		s1=118.776767 #云南路
		s2=32.048555
		for i in range(3):
			for j in range(3):
				ss1=str(s1+i*0.000972)
				ss2=str(s2+j*0.00064025)
				ss3=ss1+','+ss2
				locals.append(ss3)			
		for local in locals:
			queryStr1 = 'https://restapi.amap.com/v3/traffic/status/circle?location='+local+'&radius=50&key=060fc55def82a6e495f4bb0d789689d1'
			encodedStr1 = urllib.parse.quote(queryStr1, safe="/:=&?#+!$,;'@()*[]")
			r=requests.get(encodedStr1)
			r=r.text
			a=r.rfind("status")
			if r[a+9]==']':
				f.write('0')
			else:
				f.write(r[a+9])
			f.write(' ')
			f.write(local)
			f.write('\n')
		print('Succeed!')
		time.sleep(2)
	
except KeyboardInterrupt:
	print('finished!')
f.close()	




