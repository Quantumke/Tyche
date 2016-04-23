from slackclient import SlackClient 
import time
api_token= "xoxb-37407461829-eBlHTfhJU6ZoO8vi3Y5u7hnc"
channel_name="sandbox"

class Salute():
	def run(Salute):
		slack_client_instance=SlackClient(api_token)
		if slack_client_instance.rtm_connect():
			slack_client_instance.rtm_send_message(channel_name, "Am here for your daily stand ups say 'go' !")
			while True:
				for slack_message in slack_client_instance.rtm_read():
					message=slack_message.get("text")
					user=slack_message.get("user")
					if not message or not user:
						continue
						slack_client_instance.rtm_send_message(channel_name,"<@{}> ".format(user))
						slack_client_instance.rtm_send_message(channel_name, message)
						print(message)
                				if message=="go":
							slack_client_instance.rtm_send_message(channel_name, "what did you do yesterday?")
                				else:
                    					slack_client_instance.rtm_send_message(channel_name, "I did not quite get that! Say 'go'  to continue")
                				time.sleep(0.5)

    
