from slackclient import SlackClient
import time

class Intro():
	def run(data, fetch_data):
		data['credentials']=Intro.get_credentials(fetch_data)
		print(fetch_data, "try")

	def get_credentials (fetch_data):
		credentials ={}
		credentials['api_token']="xoxb-37407461829-eBlHTfhJU6ZoO8vi3Y5u7hnc"
		credentials['channel_name']="sandbox"
		return credentials
if __name__=='__main__':
	run()
	get_credentials()
