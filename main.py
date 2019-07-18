import itchat
import threading

groupNames = ['group chat 1', 'group chat 2', 'group chat 3', 'group chat n']
message = '// Python WeChat auto chat test (time interval: 10s)'

# group chat
def groupChat(groupNames, message):
    groups = itchat.get_chatrooms(update=True)

    global username

    for groupName in groupNames:
        groups = itchat.search_chatrooms(name=groupName)
        for group in groups:
            if group['NickName'] == groupName:
                username = group['UserName']
                itchat.send_msg(message, username)
            else:
                print('No group found')

nickNames = ['user 1', 'user 2', 'user 3', 'user n']

# individual chat
def individualChat(userNames, message): 
    for nickName in nickNames:
        friends = itchat.search_friends(nickName=nickName)
        for friend in friends:
            itchat.send_msg(message, friend['UserName'])

def main():
    threading.Timer(10.0, main).start()
    # groupChat(groupNames, message)
    #individualChat(nickNames, message)

itchat.auto_login(hotReload=True)
main()
itchat.run()