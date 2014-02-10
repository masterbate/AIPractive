from pandac.PandaModules import *
from ToontownFD_Engine.Localizer import *
from ToontownFD_Engine.Globals import *
from ToontownFD_Engine.toon import DistributedAvatar
from ToontownFD_Engine.toon import Toon
from direct.distributed import DistributedSmoothNode
from direct.distributed.ClockDelta import globalClockDelta
from direct.task.Task import Task
from direct.directnotify import DirectNotifyGlobal
from direct.distributed import DistributedObject

class DistributedToonMgr(DistributedObject.DistributedObject):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedToonMgr')
    ActivateEvent = 'DistributedToonMgr-activate'

    def __init__(self, cr):
        print 'DistributedToonMgr (AI) is active!'