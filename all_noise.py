import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
start = int(input('Start: '))
stop = int(input('Stop : '))

file = open('data.txt','w')
file.write('----------------------------------------------------------------\n')
file.write('                         Noise Ratio   \n')
file.write('----------------------------------------------------------------\n')
file.write('ObsID       OrbitID         Quadrant       DetID        PixID   \n')
file.write('----------------------------------------------------------------\n')    
url = 'https://www.iucaa.in/~astrosat/czti_dqr/index.html'
html = urlopen(url)
s = BeautifulSoup(html, 'lxml')


links = s.find_all('a',href = True, limit = stop+6)


for l in range(stop+5,start+5,-1):
	
	
	strip = links[l].get('href')
	link = 'https://www.iucaa.in/~astrosat/czti_dqr/' + strip
	html_ = urlopen(link)
	soup = BeautifulSoup(html_, 'lxml')
	
	info= soup.find_all('li')[4]
	obsid = info.text[-5:-1]
	

	orb = soup.find_all('title')[0]
	orbid = orb.text[-5:]
	print('obsid:', obsid ,	' orbid:', orbid)
	
	noise = soup.find_all('table')[5]
	pixel = soup.find_all('table')[6]

	detid = pixel.find_all('td')
	pixid = pixel.find_all('td')

	detid_a = detid[0].text
	pixid_a = pixid[1].text

	detid_b = detid[21].text
	pixid_b = pixid[22].text

	detid_c = detid[42].text
	pixid_c = pixid[43].text

	detid_d = detid[63].text
	pixid_d = pixid[64].text


	n1 = noise.find_all('td',class_='important')[0].text
	n2 = noise.find_all('td',class_='important')[1].text
	n3 = noise.find_all('td',class_='important')[2].text
	n4 = noise.find_all('td',class_='important')[3].text

	n1 = float(n1[:-1])
	n2 = float(n2[:-1])
	n3 = float(n3[:-1])
	n4 = float(n4[:-1])

	if n1 >= 5.0:
		file.write( obsid + '  	   	 ')
		file.write(orbid + '  		') 
		file.write('A = ' + str(n1) + '%')
		file.write( '		' + detid_a + '			' + pixid_a  + '\n')
		
	if n2 >= 5.0:
		file.write( obsid + '  	   	 ')
		file.write(orbid + '  		') 
		file.write('B = ' + str(n2) + '%')
		file.write( '		' + detid_b + '			' + pixid_b +'\n')
		
	if n3 >= 5.0:
		file.write( obsid + '  	   	 ')
		file.write(orbid + '  		') 
		file.write('C = ' + str(n3) + '%')
		file.write( '		' + detid_c + '			' + pixid_c +'\n')
	if n4 >= 5.0:
		file.write( obsid + '  	   	 ')
		file.write(orbid + '  		') 
		file.write('D = ' + str(n4) + '%')
		file.write( '		' + detid_d + '			' + pixid_d +'\n')

file.flush()
file.close()






