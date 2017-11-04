# HipChat Mute for OS X
Mute/Unmute users in HipChat channels via client-side DOM manipulation

# Usage
```bash
sudo python hipchat\ mute.py

*Note:* sudo is necessary since we're modifying a file in HipChat.app (chat.html)
```

# Comment
This was made for funsies on a whim, it's neither spectacular or pretty, but it works in my very limited testing.  

This is done via client-side DOM manipulation, so depending on how often Atlassian changes around their structure 
it could easily break between versions.

Hopefully this provides an idea on how to modify Atlassian's React clients, which I imagine could be used to add 
all sorts of neat things.
