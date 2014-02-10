from direct.distributed.DistributedSmoothNodeAI import DistributedSmoothNodeAI
from pandac.PandaModules import *
from direct.distributed.ClockDelta import globalClockDelta

class DistributedNPCAI(DistributedSmoothNodeAI):

    """ This is the AI-side implementation of DistributedSignpost. """
    
    def __init__(self, cr):
        print 'DistributedNPCAI is running'
        DistributedSmoothNodeAI.__init__(self, cr)
        self.dnaString = ''
        self.animState = ''
    
    def setAnimStates(self, animName, animMultiplier=1.0, timestamp=None, animType=None, callback=None, extraArgs=[]):
        timestamp = globalClockDelta.getFrameNetworkTime()
        #self.sendUpdate('setAnimStates', args=[str(animName), animMultiplier, timestamp])
        self.animState = animName

    def d_setAnimStates(self, animName, animMultiplier=1.0, timestamp=None, extraArgs=[]):
        timestamp = globalClockDelta.getFrameNetworkTime()
        self.sendUpdate('setAnimStates', args=['victory', 1.0, timestamp])
        
    def b_setAnimStates(self, animName, animMultiplier=1.0, callback=None, extraArgs=[]):
        self.d_setAnimStates(animName, animMultiplier, None, extraArgs)
        self.setAnimStates(animName, animMultiplier, None, None, callback, extraArgs)
        self.animStates = animName
        print 'i set an anim states'
        
    #def touched(self):
    #    print 'avatar touched the NPC'
    #    self.react()
        
    #def react(self):
    #    self.b_setAnimState('victory')
        
    def getDNAString(self):
        return self.dnaString
        
    def getAnimStates(self):
        return self.animState

