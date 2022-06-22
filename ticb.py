from mastodon import Mastodon


mastodon = Mastodon(
  access_token = 'token.secret',
  api_base_url = 'https://tavern.antinet.work'
)

def fetch_notifications():
	botself = mastodon.me()
	botself_id = botself["id"]
	print (botself_id)
	statuses = mastodon.notifications(limit=1)
	status_dict = statuses[0]
	status_type = status_dict['type']
	status_user = status_dict['account']
	user_id = status_user['id']
	user_name = status_user['username']
	if status_type == 'mention':
		mastodon.status_post('Hey there, thanks for reaching out, '+user_name)
	elif status_type != 'mention':
		print ('No Mention')	
		 		
	
    
fetch_notifications()
