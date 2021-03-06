from mycroft import MycroftSkill, intent_file_handler
#from mycroft.util.time import now_local
import datetime as dt
import pytz
from pytz import timezone
#import time

class Whybundy(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('whybundy.intent')
    def handle_whybundy(self, message):
       #start = time.strftime("06:00:00")
       #end = time.strftime("11:00:00")
       #now = time.strftime("%H:%M:%S")
       #if now > start and now < end:
	       #self.speak_dialog('smokeo')
       #tz = pytz.timezone('Australia/Sydney')
       nw = dt.datetime.now()
       nw_arr=[nw.hour, nw.minute]
       st_arr=[2,45] #smokeo start time hour and minute
       en_arr=[3,0] #smokeo end time hour and minute
       als_arr=[2,39] #annual leave start time hour and minute
       ale_arr=[2,44] #annual leave end time hour and minute
       #st = dt.datetime(2021,6,4,6,10,0)
       #en = dt.datetime(2021,6,4,6,14,0)
       #st = time.strftime("06:00:00")
       #en = time.strftime("11:00:00")
       if nw_arr > st_arr and nw_arr < en_arr:
         self.speak_dialog('smokeo')
       elif: nw_arr > als_arr and nw_arr < ale_arr:
         self.speak_dialog('annual')
       else:
         self.speak_dialog('whybundy')

def create_skill():
    return Whybundy()

