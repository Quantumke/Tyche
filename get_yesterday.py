from slackclient import SlackClient
import time


class GetYesterday():
	def run(getyesterday):
		if slack_client_instance.rtm_connect():
			while  True:
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



