from mastodon import Mastodon
from time import time, sleep


mastodon = Mastodon(
  access_token = 'token.secret',
  api_base_url = 'https://tavern.antinet.work'
)

#verify own credentials to get user id

botself = mastodon.me()

botself_id = botself["id"]

def fetch():
    Mastodon.notifications(id = None account_id = botself_id)
