import sys
import requests
import os
import optparse
import re
import hashlib
from colorama import Fore, Back, Style
import string
import itertools

Tversion = 'VERSION 0.1'
#CPath = os.path.dirname(os.path.realpath(__file__))         # current path
alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9','0','_']

################################

def suf(suser):
	try:
		response = requests.get('https://t.me/'+suser, timeout=5)
		DescS = re.search('''([Mm][Ee][Tt][Aa] [Pp][Rr][Oo][Pp][Ee][Rr][Tt][Yy])\s*=("[Oo][Gg]:[Dd][Ee][Ss][Cc][Rr][Ii][Pp][Tt][Ii][Oo][Nn]" [Cc][Oo][Nn][Tt][Ee][Nn][Tt]=.*)''',response.text).group(2)
		exDEC = re.search('''([Cc][Oo][Nn][Tt][Ee][Nn][Tt])\s*=(.*)\s*''',DescS).group(2)
		if exDEC != '''"">''':
			print (Fore.GREEN + 'Your Requested Username Existed')
		else:
			print (Fore.GREEN + 'Your Requested Username Does not Existed')
	except Exception as e:
		print (Fore.RED + 'Failed, Try Again\n'+str(e))
	print(Style.RESET_ALL)

################################

def uf(ulen,stw,lstwi):
	if stw == None:
		try:
			searchkeywords = [''.join(i) for i in itertools.product(alphabets, repeat = ulen)]
			for count in range(len(searchkeywords)):
				response = requests.get('https://t.me/'+searchkeywords[count], timeout=5)
				DescS = re.search('''([Mm][Ee][Tt][Aa] [Pp][Rr][Oo][Pp][Ee][Rr][Tt][Yy])\s*=("[Oo][Gg]:[Dd][Ee][Ss][Cc][Rr][Ii][Pp][Tt][Ii][Oo][Nn]" [Cc][Oo][Nn][Tt][Ee][Nn][Tt]=.*)''',response.text).group(2)
				exDEC = re.search('''([Cc][Oo][Nn][Tt][Ee][Nn][Tt])\s*=(.*)\s*''',DescS).group(2)
				if exDEC != '''"">''':
					print (Fore.GREEN + searchkeywords[count]+' - - - YES')
				else:
					print (Fore.YELLOW + searchkeywords[count]+' - - - NO')
		except Exception as e:
			print (Fore.RED + 'Failed, Try Again\n'+str(e))
	else:
		if lstwi > ulen:
			print (Fore.GREEN + 'Please choose right username lenght')
		elif lstwi == ulen:
			print (Fore.GREEN + 'Your provided username lenght (--ul) should be at least %s'%(ulen+1))
		else:
			sufflen = ulen - lstwi
			try:
				for sufcount in range(sufflen+1):
					searchkeywords = [''.join(j) for j in itertools.product(alphabets, repeat = sufcount)]
					for lokount in range(len(searchkeywords)):
						response = requests.get('https://t.me/'+stw+searchkeywords[lokount], timeout=5)
						DescS = re.search('''([Mm][Ee][Tt][Aa] [Pp][Rr][Oo][Pp][Ee][Rr][Tt][Yy])\s*=("[Oo][Gg]:[Dd][Ee][Ss][Cc][Rr][Ii][Pp][Tt][Ii][Oo][Nn]" [Cc][Oo][Nn][Tt][Ee][Nn][Tt]=.*)''',response.text).group(2)
						exDEC = re.search('''([Cc][Oo][Nn][Tt][Ee][Nn][Tt])\s*=(.*)\s*''',DescS).group(2)
						if exDEC != '''"">''':
							print (Fore.GREEN + stw+searchkeywords[lokount]+' - - - YES')
						else:
							print (Fore.YELLOW + stw+searchkeywords[lokount]+' - - - NO')
			except Exception as e:
				print (Fore.RED + 'Failed, Try Again\n'+str(e))
	print(Style.RESET_ALL)

################################

if __name__=='__main__':
	print (Fore.YELLOW + '\nSIMPLE Telegram Username Checker/Finder\n')
	print (Fore.CYAN + '''
		_______________ ___      ___________
		\__    ___/    |   \ ____\_   _____/
		  |    |  |    |   // __ \|    __)  
		  |    |  |    |  /\  ___/|     \   
		  |____|  |______/  \___  >___  /   
		                        \/    \/    
		                        coded by Z3r0\n\n''')
	print(Fore.YELLOW)
	parser = optparse.OptionParser( version = Tversion )
	parser.add_option('--ul', action='store', dest='ulenght' , help='Usernames Lenght, It  shoulde be at least 5')
	parser.add_option('--st', action='store', dest='stwi' , help='Usernames will start with what you specified here, if you do not specify this, it will check all possible usernames with the provided lenght')
	parser.add_option('--suser', action='store', dest='siguser' , help='If you want to search for single username')
	print(Style.RESET_ALL)
	options,_ = parser.parse_args()
	if ( options.siguser ):
		if( options.ulenght or options.stwi or (options.stwi and options.ulenght)):
			print (Fore.RED + 'Sorry, In this mode you can just search for SINGLE USER (DO NOT USE --ul and --st COMMANDS)\n')
		else:
			suf(options.siguser)
	else:
		if ( options.ulenght and int(options.ulenght) > 4 ):
			iulenght = int(options.ulenght)
			if (options.stwi):
				lstwi = len(options.stwi)
				uf(iulenght,options.stwi,lstwi)
			else:
				uf(iulenght,None,0)
		else:
			print (Fore.RED + 'You Should Specify The Lenght Of Usernames That You Want To Find(Maybe Your Specified Lenght is Less Than 5)\n')
		print(Style.RESET_ALL)
	print(Style.RESET_ALL)
