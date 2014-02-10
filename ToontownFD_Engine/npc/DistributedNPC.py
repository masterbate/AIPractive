from pandac.PandaModules import *
from ToontownFD_Engine.Localizer import *
from ToontownFD_Engine.Globals import *
from ToontownFD_Engine.toon import DistributedAvatar
from ToontownFD_Engine.toon import Toon
from direct.distributed import DistributedSmoothNode
from direct.distributed.ClockDelta import globalClockDelta
from direct.task.Task import Task

class DistributedNPC(DistributedAvatar.DistributedAvatar, Toon.Toon, DistributedSmoothNode.DistributedSmoothNode):

    def __init__(self, cr):
        DistributedAvatar.DistributedAvatar.__init__(self, cr)
        Toon.Toon.__init__(self)
        DistributedSmoothNode.DistributedSmoothNode.__init__(self, cr)

    def disable(self):
        self.stopBlink()
        self.stopSmooth()
        self.stopLookAroundNow()
        DistributedAvatar.DistributedAvatar.disable(self)

    def delete(self):
        try:
            self.DistributedToon_deleted
        except:
            self.DistributedToon_deleted = 1
            DistributedAvatar.DistributedAvatar.delete(self)
            Toon.Toon.delete(self)
            DistributedSmoothNode.DistributedSmoothNode.delete(self)

    def generate(self):
        DistributedAvatar.DistributedAvatar.generate(self)
        DistributedSmoothNode.DistributedSmoothNode.generate(self)

    def announceGenerate(self):
        print 'lets not'
        #DistributedAvatar.DistributedAvatar.announceGenerate(self)

    def setDNAString(self, dnaString):
        Toon.Toon.setDNAString(self, dnaString)

    def d_setDNAString(self, dnaString):
        self.sendUpdate('setDNAString', [dnaString])

    def b_setDNAString(self, dnaString):
        self.setDNAString(dnaString)
        self.d_setDNAString(dnaString)

    def setDNA(self, dna):
        Toon.Toon.setDNA(self, dna)

    def getDNAString(self):
        return self.style.makeNetString()

    def getAnimStates(self):
        return (self.playingAnim, self.animMultiplier, 0)

    def wrtReparentTo(self, parent):
        DistributedSmoothNode.DistributedSmoothNode.wrtReparentTo(self, parent)

    def b_setAnimStates(self, animName, animMultiplier=1.0, callback=None, extraArgs=[]):
        if self.animFSM.getCurrentState().getName() == animName:
            return None
        self.d_setAnimStates(animName, animMultiplier, None, extraArgs)
        self.setAnimStates(animName, animMultiplier, None, None, callback, extraArgs)

    def d_setAnimStates(self, animName, animMultiplier=1.0, timestamp=None, extraArgs=[]):
        if self.animFSM.getCurrentState().getName() == animName:
            return None
        timestamp = globalClockDelta.getFrameNetworkTime()
        print 'here'
        self.sendUpdate('setAnimStates', [animName, animMultiplier, timestamp])

    def setAnimStates(self, animName, animMultiplier=1.0, timestamp=None, animType=None, callback=None, extraArgs=[]):
        if self.animFSM.getCurrentState().getName() == animName:
            return None
        if not animName or animName == 'None':
            return None
        if timestamp == None:
            ts = 0.0
        else:
            ts = globalClockDelta.localElapsedTime(timestamp)
        self.animMultiplier = animMultiplier
        if self.animFSM.getStateNamed(animName):
            self.animFSM.request(animName, [animMultiplier, ts, callback, extraArgs])
