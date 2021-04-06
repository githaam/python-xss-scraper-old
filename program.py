import requests
import random
#from threading import Thread """belom diimplementasikan"""
from bs4 import BeautifulSoup

"""

	TO DO

	1. coba buat multithread supaya programnya tidak notresponding lagi

"""

Rep = 1

# Python program for KMP Algorithm
def KMPSearch(pat, txt):
	M = len(pat)
	N = len(txt)
	hasil = ""

	# create lps[] that will hold the longest prefix suffix
	# values for pattern
	lps = [0]*M
	j = 0 # index for pat[]

	# Preprocess the pattern (calculate lps[] array)
	computeLPSArray(pat, M, lps)

	i = 0 # index for txt[]
	while i < N:
		if pat[j] == txt[i]:
			i += 1
			j += 1

		if j == M:
			hasil = ("Found pattern at index " + str(i-j))
			j = lps[j-1]

		# mismatch after j matches
		elif i < N and pat[j] != txt[i]:
			# Do not match lps[0..lps[j-1]] characters,
			# they will match anyway
			if j != 0:
				j = lps[j-1]
			else:
				i += 1

	return hasil

def computeLPSArray(pat, M, lps):
	len = 0 # length of the previous longest prefix suffix

	lps[0] # lps[0] is always 0
	i = 1

	# the loop calculates lps[i] for i = 1 to M-1
	while i < M:
		if pat[i]== pat[len]:
			len += 1
			lps[i] = len
			i += 1
		else:
			# This is tricky. Consider the example.
			# AAACAAAA and i = 7. The idea is similar
			# to search step.
			if len != 0:
				len = lps[len-1]

				# Also, note that we do not increment i here
			else:
				lps[i] = 0
				i += 1

def scraping(target):
	target = target.replace(" ","")

	try:
		result = requests.get(target)
	except IndexError:
		hasilAkhir = "Index Error."
		pattern = "-"
		return hasilAkhir, pattern
	except:
		hasilAkhir = "URL Error."
		pattern = "-"
		return hasilAkhir, pattern
	else:
		soup = BeautifulSoup(result.text, 'html.parser')
		url = []

		for links in soup.find_all('a', href=True):
			link = str(links['href'].replace(" ","").replace("\n",""))
			if link[0:4] == "http":
				url.append(link)
			else:
				continue
		return url, soup

def openFile():
	try:
		with open('payload.txt','r', encoding='utf8') as file:
			pat = file.readlines()
	except:
		hasilAkhir = "Couldn't find payload.txt"
		pattern = "-"
		return hasilAkhir, pattern
	else:
		pat = [i.replace("\n","") for i in pat]
		pat = list(filter(None, pat))
		return pat

def scanning(pat, soup): #pat, soup
	for i in range(len(pat)):
		hasilAkhir = KMPSearch(pat[i], str(soup))
		if hasilAkhir == "":
			hasilAkhir = ("Not Found")
			pattern = "-"
			#return hasilAkhir, pattern
		else:
			#print (hasilAkhir+" \""+pat[i]+"\"")
			pattern = pat[i]
			break
			#return hasilAkhir, pattern
	
	return hasilAkhir, pattern

def main(target): #nanti ditambah aja variabel
	#target = "https://www.unud.ac.id/"

	if (len(openFile()) == 2):
		hasilAkhir, pattern = openFile()
		return hasilAkhir, pattern
	else:
		pat = openFile()
		
	global Rep
	
	scanned = []
	targets = []
	scanned.append(target)

	for Rep in range(2):
		#scanned.append(target)
		url, soup = scraping(target)
		if (soup == '-'):
			hasilAkhir, pattern = url, soup
			return hasilAkhir, pattern

		hasilAkhir, pattern = scanning(pat, soup)

		try:
			nomor = random.randint(1,len(url))
			target = url[nomor]
			scanned.append(target)
		except:
			# try:
			# 	nomor = random.randint(1,len(url))
			# 	target = url[nomor]
			# except:
			hasilAkhir = "Link not found."
			pattern = "Tidak ada link lain yang ditemukan."
			
		#hasilAkhir, pattern, targets = scraping(target)

		if hasilAkhir != "Not Found":
			break
		# else:
		# 	scanned.append(target)

	return hasilAkhir, pattern, scanned

"""
### UN-COMMENT PADA SAAT PENGUJIAN ###
"""

# if __name__ == '__main__':
# 	# hasilAkhir, pattern, target = main()
# 	# scanned = []
# 	# scanned = target[:]
# 	# print(type(target))
# 	# print (scanned[1])
	
# 	#openFile()
# 	#scraping('https://www.kaskus.co.id/')

# 	#hasilAkhir, pattern = scanning(soup, pat)

# 	print (main('https://www.kaskus.co.id/'))