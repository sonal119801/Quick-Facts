import time
from plyer import notification
#from datetime import datetime

if __name__=='__main__':
    title="TECH VOCAB"
    with open("ITJargon.txt") as vc:
        lines=vc.readlines()
        for vocab in lines:
            notification.notify(
                title=title,
                message=vocab.strip(),
                #app_icon= '\showicon.ico',
                timeout=10
            )
            time.sleep(60)