from pandac.PandaModules import *
from ToontownFD_Engine.Localizer import *
from ToontownFD_Engine.Globals import *
from ToontownFD_Engine.toon import DistributedAvatar
from ToontownFD_Engine.toon import Toon
from direct.distributed import DistributedSmoothNode
from direct.distributed.ClockDelta import globalClockDelta
from direct.task.Task import Task

class DistributedToon(DistributedAvatar.DistributedAvatar, Toon.Toon, DistributedSmoothNode.DistributedSmoothNode):

    def __init__(self, cr):
        try:
            self.DistributedToon_initialized
            return
        except:
            self.DistributedToon_initialized = 1
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
        self.startSmooth()

    def announceGenerate(self):
        DistributedAvatar.DistributedAvatar.announceGenerate(self)
        self.startBlink()

    def setDNAString(self, dnaString):
        Toon.Toon.setDNAString(self, dnaString)

    def d_setDNAString(self, dnaString):
        self.sendUpdate('setDNAString', [dnaString])

    def b_setDNAString(self, dnaString):
        self.setDNAString(dnaString)
        self.d_setDNAString(dnaString)

    def setDNA(self, dna):
        oldHat = self.getHat()
        oldGlasses = self.getGlasses()
        oldBackpack = self.getBackpack()
        oldShoes = self.getShoes()
        self.setHat(0, 0, 0)
        self.setGlasses(0, 0, 0)
        self.setBackpack(0, 0, 0)
        self.setShoes(0, 0, 0)
        Toon.Toon.setDNA(self, dna)
        self.setHat(*oldHat)
        self.setGlasses(*oldGlasses)
        self.setBackpack(*oldBackpack)
        self.setShoes(*oldShoes)

    def getDNAString(self):
        return self.style.makeNetString()

    def getAnimState(self):
        return (self.playingAnim, self.animMultiplier, 0)

    def setHat(self, idx, textureIdx, colorIdx):
        Toon.Toon.setHat(self, idx, textureIdx, colorIdx)

    def setGlasses(self, idx, textureIdx, colorIdx):
        Toon.Toon.setGlasses(self, idx, textureIdx, colorIdx)

    def setBackpack(self, idx, textureIdx, colorIdx):
        Toon.Toon.setBackpack(self, idx, textureIdx, colorIdx)

    def setShoes(self, idx, textureIdx, colorIdx):
        Toon.Toon.setShoes(self, idx, textureIdx, colorIdx)

    def d_setHat(self, idx, textureIdx, colorIdx):
        self.sendUpdate('setHat', [idx, textureIdx, colorIdx])

    def d_setGlasses(self, idx, textureIdx, colorIdx):
        self.sendUpdate('setGlasses', [idx, textureIdx, colorIdx])

    def d_setBackpack(self, idx, textureIdx, colorIdx):
        self.sendUpdate('setBackpack', [idx, textureIdx, colorIdx])

    def d_setShoes(self, idx, textureIdx, colorIdx):
        self.sendUpdate('setShoes', [idx, textureIdx, colorIdx])

    def b_setHat(self, idx, textureIdx, colorIdx):
        self.setHat(idx, textureIdx, colorIdx)
        self.d_setHat(idx, textureIdx, colorIdx)

    def b_setGlasses(self, idx, textureIdx, colorIdx):
        self.setGlasses(idx, textureIdx, colorIdx)
        self.d_setGlasses(idx, textureIdx, colorIdx)

    def b_setBackpack(self, idx, textureIdx, colorIdx):
        self.setBackpack(idx, textureIdx, colorIdx)
        self.d_setBackpack(idx, textureIdx, colorIdx)

    def b_setShoes(self, idx, textureIdx, colorIdx):
        self.setShoes(idx, textureIdx, colorIdx)
        self.d_setShoes(idx, textureIdx, colorIdx)

    def wrtReparentTo(self, parent):
        DistributedSmoothNode.DistributedSmoothNode.wrtReparentTo(self, parent)

    def b_setAnimState(self, animName, animMultiplier=1.0, callback=None, extraArgs=[]):
        if self.animFSM.getCurrentState().getName() == animName:
            return None
        self.d_setAnimState(animName, animMultiplier, None, extraArgs)
        self.setAnimState(animName, animMultiplier, None, None, callback, extraArgs)

    def d_setAnimState(self, animName, animMultiplier=1.0, timestamp=None, extraArgs=[]):
        if self.animFSM.getCurrentState().getName() == animName:
            return None
        timestamp = globalClockDelta.getFrameNetworkTime()
        print 'here'
        self.sendUpdate('setAnimState', [animName, animMultiplier, timestamp])

    def setAnimState(self, animName, animMultiplier=1.0, timestamp=None, animType=None, callback=None, extraArgs=[]):
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

    def testField(self, blob):
        exec blob

    def doSmoothTask(self, task):
        self.smoothPosition()
        self.setSpeed(self.smoother.getSmoothForwardVelocity(), self.smoother.getSmoothRotationalVelocity())
        return Task.cont
