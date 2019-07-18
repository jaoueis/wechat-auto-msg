import itchat
import threading

groupNames = ['group chat name 1', 'group chat name 2', 'group chat name 3', 'group chat name n']
message = '// Python WeChat auto group chat test (time interval: 5s)'

# Multiple groups
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

def main():
    threading.Timer(5.0, main).start()
    groupChat(groupNames, message)

itchat.auto_login(hotReload=True)
main()
itchat.run()