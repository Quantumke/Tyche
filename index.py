from slackclient import SlackClient
import time

api_token= ""
channel_name=""



def main():
	slack_client_instance=SlackClient(api_token)
	if slack_client_instance.rtm_connect():
		slack_client_instance.rtm_send_message(channel_name, "Am here to find you a  tech date  !")
		while True:
			for slack_message in slack_client_instance.rtm_read():
				message=slack_message.get("text")
				user=slack_message.get("user")
				if message=="go":
					message="please tell me your gender"
					slack_client_instance.rtm_send_message(channel_name, message)
					gender=slack_message.get("text`")
				if not message or not user:
					continue
					slack_client_instance.rtm_send_message(channel_name,"<@{}> ".format(user))
					slack_client_instance.rtm_send_message(channel_name, message)
					time.sleep(0.5)


if __name__=='__main__':
	main()
