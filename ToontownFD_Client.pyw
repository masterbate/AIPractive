import sys
sys.dont_write_bytecode = True

from pandac.PandaModules import ConfigVariableString
ConfigVariableString('default-model-extension', '.bam').setValue('.bam')

from direct.directbase import DirectStart
from pandac.PandaModules import *
from direct.task import Task
from direct.distributed.ClientRepository import ClientRepository
from direct.showbase.InputStateGlobal import inputState
from direct.showbase.DirectObject import DirectObject
from direct.interval.IntervalGlobal import *
from direct.distributed.PyDatagram import PyDatagram
from direct.distributed.PyDatagramIterator import PyDatagramIterator
from ToontownFD_Engine.Localizer import *
from ToontownFD_Engine.Globals import *
from ToontownFD_Engine.toon import LocalToon
from ToontownFD_Engine.toon import ToonDNA
from ToontownFD_Engine.npc import DistributedNPC
from direct.distributed.ClockDelta import globalClockDelta
from direct.distributed import DistributedSmoothNode

execfile('CogNation.py')
#execfile('ttsrc/toontown/toonbase/ToontownStart.py')
#execfile('yolo.txt')

class ToontownFD_ClientRepository(ClientRepository):

    notify = directNotify.newCategory('ClientRepository')

    def __init__(self):
        dcFileNames = ['ToontownFD_Engine/etc/network.dc']
        ClientRepository.__init__(self, dcFileNames=dcFileNames)
        self.setTcpHeaderSize(4)
        self.parentMgr.registerParent(SPRender, base.render)
        self.parentMgr.registerParent(SPHidden, NodePath())

class ToontownFD_Client(DirectObject):

    notify = directNotify.newCategory('ToontownFDClient')

    def __init__(self):
        globalClock.setMode(ClockObject.MLimited)
        globalClock.setFrameRate(30)
        self.url = URLSpec('http://127.0.0.1:9047')
        self.cr = ToontownFD_ClientRepository()
        self.cr.connect([self.url],
                        successCallback=self.connectSuccess,
                        failureCallback=self.connectFailure)
        base.camLens.setFov(DefaultCameraFov)
        base.camLens.setNearFar(DefaultCameraNear, DefaultCameraFar)
        base.setBackgroundColor(DefaultBackgroundColor)
        globalClock.setMaxDt(0.2)

    def connectFailure(self, statusCode, statusString):
        self.notify.warning('Couldn\'t connect to server: %d, %s' % (statusCode, statusString))

    def connectSuccess(self):
        self.acceptOnce('gotTimeSync', self.gotTimeSync)
        self.cr.setInterestZones([2])

    def gotTimeSync(self):
        DistributedSmoothNode.globalActivateSmoothing(1, 0)
        self.cr.setInterestZones([2, 1000])
        if self.cr.haveCreateAuthority():
            self.createReady()
        else:
            self.acceptOnce('createReady', self.createReady)

    def createReady(self):
        #localAvatar = LocalToon.LocalToon(self.cr)
        #localAvatar.dclass = self.cr.dclassesByName['DistributedToon']
        #base.localAvatar = localAvatar
        #__builtins__.localAvatar = base.localAvatar
        #style = ToonDNA.ToonDNA()
        #style.newToonRandom()
        #localAvatar.setDNA(style)
        #base.localAvatar = self.cr.createDistributedObject(
        #    className='DistributedToon', distObj=base.localAvatar, zoneId=1000
        #)
        #base.localAvatar.d_setDNAString(style.makeNetString())
        #base.localAvatar.startPosHprBroadcast()
        #base.localAvatar.attachCamera()
        #base.localAvatar.initCameraPositions()
        #base.localAvatar.startUpdateSmartCamera(1)
        #base.localAvatar.collisionsOn()
        #base.localAvatar.enableAvatarControls()
        #base.localAvatar.startTrackAnimToSpeed()
        #base.localAvatar.setName('test1')
        base.oobe()
        base.accept('f2', enterCommand)
        
def enterCommand():
    lol = raw_input('Command?/n')
    exec(lol)

base.game = ToontownFD_Client()
base.cr = base.game.cr

run()
