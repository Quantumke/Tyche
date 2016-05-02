from slackclient import SlackClient
import time

class Intro():
	def run(data, fetch_data):
		data['credentials']=Intro.get_credentials(fetch_data)
		print(fetch_data, "try")

	def get_credentials (fetch_data):
		credentials ={}
		credentials['api_token']=""
		credentials['channel_name']=""
		return credentials
if __name__=='__main__':
	run()
	get_credentials()
