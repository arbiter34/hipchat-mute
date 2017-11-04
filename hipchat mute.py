import re

hipChatFilePath = '/Applications/HipChat.app/Contents/Resources/chat.html'
muteFilePath = 'hipchat_mute.html'
origTitle = '<title>HipChat</title>'

with open(hipChatFilePath, 'r') as file:
	hipChatFileData = file.read()

with open(muteFilePath, 'r') as file:
	muteFileData = file.read()

if "macstate.webCoreStarted = true;\n\t\twindow.my_init();" not in hipChatFileData:
	hipChatFileData = hipChatFileData.replace("macstate.webCoreStarted = true;", "macstate.webCoreStarted = true;\n\t\twindow.my_init();");

if origTitle in hipChatFileData:
	hipChatFileData = hipChatFileData.replace('<title>HipChat</title>', muteFileData)
else:
	hipChatFileData = re.sub(r'<title>HackedChat</title>.*?<script>.*?</script>', muteFileData, hipChatFileData)

with open(hipChatFilePath, 'w') as file:
	file.write(hipChatFileData)