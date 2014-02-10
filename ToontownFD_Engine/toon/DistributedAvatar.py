from pandac.PandaModules import *
from direct.distributed import DistributedNode
from direct.actor.DistributedActor import DistributedActor
from ToontownFD_Engine.toon.Avatar import Avatar
from ToontownFD_Engine.Globals import *

class DistributedAvatar(DistributedActor):

    def __init__(self, cr):
        try:
            self.DistributedAvatar_initialized
            return None
        except:
            self.DistributedAvatar_initialized = 1
        DistributedActor.__init__(self, cr)

    def disable(self):
        try:
            del self.DistributedAvatar_announced
        except:
            return None
        self.reparentTo(hidden)
        self.disableBodyCollisions()
        DistributedActor.disable(self)

    def delete(self):
        try:
            self.DistributedAvatar_deleted
        except:
            self.DistributedAvatar_deleted = 1
            DistributedActor.delete(self)

    def generate(self):
        DistributedActor.generate(self)
        self.setParent(SPRender)

    def announceGenerate(self):
        try:
            self.DistributedAvatar_announced
            return
        except:
            self.DistributedAvatar_announced = 1
        if not self.isLocal():
            self.initializeBodyCollisions('distAvatarCollNode-' + str(self.doId))
        DistributedActor.announceGenerate(self)

    def do_setParent(self, parentToken):
        if not self.isDisabled():
            DistributedActor.do_setParent(self, parentToken)

    def getName(self):
        return Avatar.getName(self)

    def setName(self, name):
        try:
            print 'i set my name to %s' % name
            self.node().setName('%s-%d' % (name, self.doId))
            self.gotName = 1
        except:
            pass
        return Avatar.setName(self, name)

    def getStareAtNodeAndOffset(self):
        return (self, Point3(0, 0, self.height))

    def getAvIdName(self):
        return '%s\n%s' % (self.getName(), self.doId)