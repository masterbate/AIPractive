from ToontownFD_Engine.Localizer import *
from direct.showbase.PythonUtil import Enum, invertDict
from pandac.PandaModules import BitMask32, Vec4
from pandac.PandaModules import *

WallBitmask = BitMask32(1)
FloorBitmask = BitMask32(2)
CameraBitmask = BitMask32(4)
CameraTransparentBitmask = BitMask32(8)
SafetyNetBitmask = BitMask32(512)
SafetyGateBitmask = BitMask32(1024)
GhostBitmask = BitMask32(2048)
PathFindingBitmask = BitMask32.bit(29)
CeilingBitmask = BitMask32(256)
FloorEventBitmask = BitMask32(16)
OriginalCameraFov = 52.0
DefaultCameraFov = 52.0
DefaultCameraFar = 400.0
DefaultCameraNear = 1.0
AICollisionPriority = 10
AICollMovePriority = 8
SPInvalid = 0
SPHidden = 1
SPRender = 2
SPDynamic = 5
WalkCutOff = 0.5
RunCutOff = 8.0
FloorOffset = 0.025
AvatarDefaultRadius = 1
InterfaceFont = 'phase_3/models/fonts/ImpressBT.ttf'
InterfaceFontPath = None

def getInterfaceFont():
    global InterfaceFontPath
    global InterfaceFont
    if InterfaceFont == None:
        if InterfaceFontPath == None:
            InterfaceFont = TextNode.getDefaultFont()
        else:
            InterfaceFont = loader.loadFont(InterfaceFontPath, lineHeight=1.0)
    return InterfaceFont

def setInterfaceFont(path):
    global InterfaceFontPath
    global InterfaceFont
    InterfaceFontPath = path
    InterfaceFont = None

NetworkLatency = 1.0
STAND_INDEX = 0
WALK_INDEX = 1
RUN_INDEX = 2
REVERSE_INDEX = 3
STRAFE_LEFT_INDEX = 4
STRAFE_RIGHT_INDEX = 5
ToonStandableGround = 0.707
ToonSpeedFactor = 1.25
ToonForwardSpeed = 16.0 * ToonSpeedFactor
ToonJumpForce = 24.0
ToonReverseSpeed = 8.0 * ToonSpeedFactor
ToonRotateSpeed = 80.0 * ToonSpeedFactor
ToonForwardSlowSpeed = 6.0
ToonJumpSlowForce = 4.0
ToonReverseSlowSpeed = 2.5
ToonRotateSlowSpeed = 33.0
DefaultBackgroundColor = (0.3, 0.3, 0.3, 1)
toonBodyScales = {
    'mouse': 0.6,
    'cat': 0.73,
    'duck': 0.66,
    'rabbit': 0.74,
    'horse': 0.85,
    'dog': 0.85,
    'monkey': 0.68,
    'bear': 0.85,
    'pig': 0.77
}
toonHeadScales = {
    'mouse': Point3(1.0),
    'cat': Point3(1.0),
    'duck': Point3(1.0),
    'rabbit': Point3(1.0),
    'horse': Point3(1.0),
    'dog': Point3(1.0),
    'monkey': Point3(1.0),
    'bear': Point3(1.0),
    'pig': Point3(1.0)
}
legHeightDict = {
    's': 1.5,
    'm': 2.0,
    'l': 2.75
}
torsoHeightDict = {
    's': 1.5,
    'm': 1.75,
    'l': 2.25,
    'ss': 1.5,
    'ms': 1.75,
    'ls': 2.25,
    'sd': 1.5,
    'md': 1.75,
    'ld': 2.25
}
headHeightDict = {
    'dls': 0.75,
    'dss': 0.5,
    'dsl': 0.5,
    'dll': 0.75,
    'cls': 0.75,
    'css': 0.5,
    'csl': 0.5,
    'cll': 0.75,
    'hls': 0.75,
    'hss': 0.5,
    'hsl': 0.5,
    'hll': 0.75,
    'mls': 0.75,
    'mss': 0.5,
    'rls': 0.75,
    'rss': 0.5,
    'rsl': 0.5,
    'rll': 0.75,
    'fls': 0.75,
    'fss': 0.5,
    'fsl': 0.5,
    'fll': 0.75,
    'pls': 0.75,
    'pss': 0.5,
    'psl': 0.5,
    'pll': 0.75,
    'bls': 0.75,
    'bss': 0.5,
    'bsl': 0.5,
    'bll': 0.75,
    'sls': 0.75,
    'sss': 0.5,
    'ssl': 0.5,
    'sll': 0.75
}
setInterfaceFont(InterfaceFont)
ToonFont = 'phase_3/models/fonts/ImpressBT.ttf'

def getToonFont():
    global ToonFont
    if ToonFont == None:
        ToonFont = loader.loadFont(ToonFont, lineHeight=1.0)
    return ToonFont

ToonAnimStates = set([
    'off',
    'neutral',
    'victory',
    'Happy',
    'Sad',
    'Catching',
    'CatchEating',
    'Sleep',
    'walk',
    'jumpSquat',
    'jump',
    'jumpAirborne',
    'jumpLand',
    'run',
    'swim',
    'swimhold',
    'dive',
    'cringe',
    'OpenBook',
    'ReadBook',
    'CloseBook',
    'TeleportOut',
    'Died',
    'TeleportedOut',
    'TeleportIn',
    'Emote',
    'SitStart',
    'Sit',
    'Push',
    'Squish',
    'FallDown',
    'GolfPuttLoop',
    'GolfRotateLeft',
    'GolfRotateRight',
    'GolfPuttSwing',
    'GolfGoodPutt',
    'GolfBadPutt',
    'Flattened',
    'CogThiefRunning',
    'ScientistJealous',
    'ScientistEmcee',
    'ScientistWork',
    'ScientistLessWork',
    'ScientistPlay'
])