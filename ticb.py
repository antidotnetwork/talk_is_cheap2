from mastodon import Mastodon
from bs4 import BeautifulSoup
import re

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

def fetch_notifications():
	print (botself_id)
	statuses = mastodon.notifications(limit=1)
	status_dict = statuses[0]
	status_type = status_dict['type']
	status_id = status_dict['id']
	status_user = status_dict['account']
	user_id = status_user['id']
	user_name = status_user['username']
	status_msg_dict = status_dict['status']
	status_msg = status_msg_dict['content']
	#if status_type == 'mention':
		#print (status_msg)
	#elif status_type != 'mention':
		#print ('No Mention')	
	for x in statuses:
		if status_type == 'mention':
			print (status_msg)
			plaintext = h2t(status_msg)
			print (plaintext)
		elif status_type != 'mention':
			print ("No Content at post id:", status_id)
			mastodon.notifications_dismiss(status_id)

		
fetch_notifications()
