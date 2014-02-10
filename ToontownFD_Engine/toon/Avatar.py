from ToontownFD_Engine.Localizer import *
from ToontownFD_Engine.Globals import *
from direct.actor.Actor import Actor

class Avatar(Actor):

    notify = directNotify.newCategory('Avatar')

    def __init__(self, other=None):
        self.name = ''
        try:
            self.Avatar_initialized
            return
        except:
            self.Avatar_initialized = 1
        Actor.__init__(self, None, None, other, flattenable=0, setFinal=1)
        self.__font = getInterfaceFont()
        self.avatarType = ''
        self.collTube = None
        self.scale = 1.0
        self.height = 0.0
        self.style = None

    def delete(self):
        try:
            self.Avatar_deleted
        except:
            Actor.cleanup(self)
            self.Avatar_deleted = 1
            del self.__font
            del self.style
            Actor.delete(self)

    def isLocal(self):
        return 0

    def isPet(self):
        return False

    def isProxy(self):
        return False

    def setPlayerType(self, playerType):
        self.playerType = playerType

    def getAvatarScale(self):
        return self.scale

    def setAvatarScale(self, scale):
        if self.scale != scale:
            self.scale = scale
            self.getGeomNode().setScale(scale)
            self.setHeight(self.height)

    def getHeight(self):
        return self.height

    def setHeight(self, height):
        self.height = height
        if self.collTube:
            self.collTube.setPointB(0, 0, height - self.getRadius())
            if self.collNodePath:
                self.collNodePath.forceRecomputeBounds()

    def getRadius(self):
        return AvatarDefaultRadius

    def getName(self):
        return self.name

    def getType(self):
        return self.avatarType

    def setName(self, name):
        self.name = name

    def getFont(self):
        return self.__font

    def setFont(self, font):
        self.__font = font

    def getStyle(self):
        return self.style

    def setStyle(self, style):
        self.style = style

    def isInView(self):
        pos = self.getPos(camera)
        eyePos = Point3(pos[0], pos[1], pos[2] + self.getHeight())
        return base.camNode.isInView(eyePos)

    def getAirborneHeight(self):
        height = self.getPos()
        return height.getZ() + 0.025


    def initializeBodyCollisions(self, collIdStr):
        self.collTube = CollisionTube(
            0, 0, 0.5, 0, 0, self.height - self.getRadius(), self.getRadius()
        )
        self.collNode = CollisionNode(collIdStr)
        self.collNode.addSolid(self.collTube)
        self.collNodePath = self.attachNewNode(self.collNode)
        self.collNode.setCollideMask(WallBitmask)

    def stashBodyCollisions(self):
        if hasattr(self, 'collNodePath'):
            self.collNodePath.stash()

    def unstashBodyCollisions(self):
        if hasattr(self, 'collNodePath'):
            self.collNodePath.unstash()

    def disableBodyCollisions(self):
        if hasattr(self, 'collNodePath'):
            self.collNodePath.removeNode()
            del self.collNodePath
        self.collTube = None

    def loop(self, animName, restart=1, partName=None, fromFrame=None, toFrame=None):
        return Actor.loop(self, animName, restart, partName, fromFrame, toFrame)