import sys
sys.dont_write_bytecode = True

from pandac.PandaModules import ConfigVariableString
ConfigVariableString('window-type', 'none').setValue('none')
ConfigVariableString('default-model-extension', '.bam').setValue('.bam')

from direct.directbase import DirectStart
from pandac.PandaModules import *
from direct.distributed.ServerRepository import ServerRepository
from direct.distributed.ClientRepository import ClientRepository
from direct.distributed.PyDatagram import PyDatagram
from direct.distributed.PyDatagramIterator import PyDatagramIterator
from direct.distributed.MsgTypesCMU import *
from ToontownFD_Engine.npc import DistributedNPCAI
from direct.distributed.ClockDelta import globalClockDelta

class ToontownFD_ServerRepository(ServerRepository):

    notify = directNotify.newCategory('ServerRepository')

    def __init__(self):
        serverPort = base.config.GetInt('server-port', 9047)
        serverHost = base.config.GetString('server-host', '')
        dcFileNames = ['ToontownFD_Engine/etc/network.dc']
        ServerRepository.__init__(self, serverPort, serverAddress=serverHost, dcFileNames=dcFileNames)
        self.setTcpHeaderSize(4)
        base.setSleep(0.01)

__builtins__.simbase = ToontownFD_ServerRepository()

class ToontownFD_AIRepository(ClientRepository):

    notify = directNotify.newCategory('AIRepository')

    def __init__(self):
        dcFileNames = ['ToontownFD_Engine/etc/network.dc']
        ClientRepository.__init__(self, dcFileNames=dcFileNames, dcSuffix='AI')
        serverPort = base.config.GetInt('server-port', 9047)
        serverHost = base.config.GetString('server-host', '://127.0.0.1:%d')
        self.toons = {}
        self.connect([URLSpec('http%s' % (serverHost % serverPort))],
                      successCallback=self.connectSuccess,
                      failureCallback=self.connectFailure)
        self.setTcpHeaderSize(4)
        

    def connectFailure(self, statusCode, statusString):
        self.notify.warning('Couldn\'t connect to server: %d, %s' % (statusCode, statusString))

    def connectSuccess(self):
        self.acceptOnce('createReady', self.createReady)

    def createReady(self):
        self.timeManager = self.createDistributedObject(
            className='TimeManagerAI', zoneId=2
        )
        self.NPCMgr = self.createDistributedObject(
            className='DistributedNPCAI', zoneId=1000
        )
        timestamp = globalClockDelta.getFrameNetworkTime()
        animMultiplier=1.0
        self.NPCMgr.sendUpdate('setAnimStates', args=['victory', animMultiplier, timestamp])
    def handleDatagram(self, di):
        msgType = self.getMsgType()
        self.currentSenderId = None
        if msgType == SET_DOID_RANGE_CMU:
            self.handleSetDoIdrange(di)
        elif msgType == OBJECT_GENERATE_CMU:
            self.handleGenerate(di)
        elif msgType == OBJECT_UPDATE_FIELD_CMU:
            self.handleUpdateField(di)
        elif msgType == OBJECT_DISABLE_CMU:
            self.handleDisable(di)
        elif msgType == OBJECT_DELETE_CMU:
            self.handleDelete(di)
        elif msgType == REQUEST_GENERATES_CMU:
            self.handleRequestGenerates(di)
        else:
            self.handleMessageType(msgType, di)
        self.considerHeartbeat()

simbase.air = ToontownFD_AIRepository()
run()
