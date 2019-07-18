import itchat
import threading

groupName = 'The name of target group chat'
message = 'Message you wanna send out'

def groupChat(groupName, message):
    groups = itchat.get_chatrooms(update=True)

    global username

    groups = itchat.search_chatrooms(name=groupName)
    for group in groups: 
        if group['NickName'] == groupName:
            username = group['UserName']
            itchat.send_msg(message, username)
        else:
            print('No group found')

def main():
    threading.Timer(5.0, main).start()
    groupChat(groupName, message)

itchat.auto_login(hotReload=True)
main()
itchat.run()