import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

file = open('tele_data.txt','w')
url = "https://www.iucaa.in/~astrosat/czti_dqr/20220228_C07_001T01_9000004982_level2_34726/index.html"
html = urlopen(url)
soup = BeautifulSoup(html, 'lxml')


def mode (value):
		
	cleanv= []
	j = 1
	while ( j < len(value)):
		for i in range(len(value)):
			
			if i == j :
				j +=4
				continue
			else :
				cleanv.append(value[i].text)

	t = 0		
	val = 0
	
	for i in range( 2,len(cleanv),3):
		file.write(cleanv[i - 2] +'           ')
		p = float(cleanv[i])
		pp = float(cleanv[i-1])
		error = p*1.0 / pp*1.0
		error = error*100.0
		error = round(error,6)
		file.write( str(error) +  ' \n')
		

table1= soup.find_all('table')[1]
row = table1.find_all('th')

info= soup.find_all('li')[4]
obsid = info.text

orb = soup.find_all('title')[0]
orbid = orb.text[-5:]
file.write(' The Telemetry error of ' + obsid + ', orbit ' + orbid + ' is : \n\n')
file.write(  row[0].text + '\n')
file.write('------------------------------------\n')

file.write(row[1].text + '  ')

#file.write(row[3].text + '  ')
#file.write(row[4].text + '  ')
file. write( ' Telemetry Error ( % )\n\n')
value1 = table1.find_all('td')
in1 = mode(value1)

file.write('\n')


table2= soup.find_all('table')[2]
row = table2.find_all('th')
file.write(row[0].text + '\n')
file.write('------------------------------------\n')

file.write(row[1].text + '  ')
#file.write(row[3].text + '  ')
#file.write(row[4].text + '  ')
file. write( ' Telemetry Error ( % )\n\n')
value2 = table2.find_all('td')
in2 = mode(value2)
file.write('\n')


table3= soup.find_all('table')[3]
row = table3.find_all('th')
file.write( row[0].text + '\n')
file.write('------------------------------------\n')

file.write(row[1].text + '  ')
#file.write(row[3].text + '  ')
#file.write(row[4].text + '  ')
file. write( ' Telemetry Error ( % )\n\n')
value3 = table3.find_all('td')
in3 = mode(value3)
file.write('\n')	


file.flush()
file.close()






