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
  
botself = mastodon.me()
botself_id = botself["id"]
print (botself_id)
statuses = mastodon.timeline_local(limit=1)
status_dict = statuses[0]
# status_type = status_dict['type']
status_id = status_dict['id']
status_user = status_dict['account']
#user_id = status_user['id']	
user_name = status_user['username']
#status_msg_dict = status_dict['status']
status_msg = status_dict['content']
plaintext = h2t(status_msg)
xml_file = {'id' : status_id, 'username' : user_name, 'content' : plaintext}
print (xml_file)
xml_file = dicttoxml.dicttoxml(xml_file)
print (xml_file)
if 
fetch_mostrecent()



	
	
	
	
	
	
	
	
	
	
	
	
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

		
