from mastodon import Mastodon
import re
import dicttoxml
import os

mastodon = Mastodon(
  access_token = 'token.secret',
  api_base_url = 'https://tavern.antinet.work'
)
CLEANR = re.compile('<.*?>') 

def h2t(raw_html):
  cleantext = re.sub(CLEANR, '', raw_html)
  return cleantext


def get_toot():  
	botself = mastodon.me()
	botself_id = botself["id"]
	statuses = mastodon.timeline_local(limit=1)
	status_dict = statuses[0]
	status_id = status_dict['id']
	status_user = status_dict['account']
	user_name = status_user['username']
	status_msg = status_dict['content']
	plaintext = h2t(status_msg)
	xml_file = {'id' : status_id, 'username' : user_name, 'content' : plaintext}
	xml_file = dicttoxml.dicttoxml(xml_file)
	return xml_file, status_id

def check_toot():
	XML, ID = get_toot()
	print (XML)
	with open("IDS.txt", 'r') as f:
		w = f.read()
		if ID == int(w):
			toot_ok = False
		else:
			toot_ok = True
	with open("IDS.txt",'w') as f:
		f.write(str(ID)+'\n')
		f.close()
	return XML, toot_ok
		

def write_xml(xxx):
	
	print (XML)
	with open("IDS.txt", 'r') as f:
		w = f.read()
		if ID == int(w):
			toot_ok = False
		else:
			toot_ok = True
	with open("IDS.txt",'w') as f:
		f.write(str(ID)+'\n')
		f.close()
	return XML, toot_ok
XML_File = check_toot()



	
	
	
	
	
	
	
	
	
	
	
	
	#	if status_type == 'mention':
	#		plaintext = h2t(status_msg)
	#		print (plaintext)
	#		tokens = nltk.word_tokenize(plaintext)
	#		print (tokens)
	#		for x in tokens:
	#			print (x)
	#			if x == 'Hello':
	#				print ('Hi...')
	#			elif x == '?':
	#				print ('whats the question again?')
	#	elif status_type != 'mention':
	#		print ("No Content at post id:", status_id)
	#		mastodon.notifications_dismiss(status_id)
