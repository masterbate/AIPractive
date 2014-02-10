from direct.directnotify import DirectNotifyGlobal
from direct.distributed import DistributedObject
from direct.interval.IntervalGlobal import *

class DistributedChatMgr(DistributedObject.DistributedObject):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedChatMgr')
    ActivateEvent = 'DistributedChatMgr-activate'

    def __init__(self):
        print 'ChatManager online'
        self.chat = ' '

    def setChat(self, chat):
        self.chat = chat

    def getChat(self):
        return self.chat

DistributedChatMgr = DistributedChatMgr()