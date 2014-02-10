from pandac.PandaModules import *
from ToontownFD_Engine.Localizer import *
from ToontownFD_Engine.Globals import *
from direct.interval.IntervalGlobal import *
from ToonHead import *
from direct.directnotify import DirectNotifyGlobal
from direct.task.Task import Task
from ToontownFD_Engine.toon import Avatar
from ToontownFD_Engine.toon import ToonDNA
import AccessoryGlobals

DogDialogueArray = []
CatDialogueArray = []
HorseDialogueArray = []
RabbitDialogueArray = []
MouseDialogueArray = []
DuckDialogueArray = []
MonkeyDialogueArray = []
BearDialogueArray = []
PigDialogueArray = []
LegsAnimDict = {}
TorsoAnimDict = {}
HeadAnimDict = {}
Preloaded = []

Phase3AnimList = (
    ('neutral', 'neutral'),
    ('run', 'run')
)
Phase3_5AnimList = (
    ('walk', 'walk'),
    ('teleport', 'teleport'),
    ('book', 'book'),
    ('jump', 'jump'),
    ('running-jump', 'running-jump'),
    ('jump-squat', 'jump-zstart'),
    ('jump-idle', 'jump-zhang'),
    ('jump-land', 'jump-zend'),
    ('running-jump-squat', 'leap_zstart'),
    ('running-jump-idle', 'leap_zhang'),
    ('running-jump-land', 'leap_zend'),
    ('pushbutton', 'press-button'),
    ('throw', 'pie-throw'),
    ('victory', 'victory-dance'),
    ('sidestep-left', 'sidestep-left'),
    ('conked', 'conked'),
    ('cringe', 'cringe'),
    ('wave', 'wave'),
    ('shrug', 'shrug'),
    ('angry', 'angry'),
    ('tutorial-neutral', 'tutorial-neutral'),
    ('left-point', 'left-point'),
    ('right-point', 'right-point'),
    ('right-point-start', 'right-point-start'),
    ('give-props', 'give-props'),
    ('give-props-start', 'give-props-start'),
    ('right-hand', 'right-hand'),
    ('right-hand-start', 'right-hand-start'),
    ('duck', 'duck'),
    ('sidestep-right', 'jump-back-right'),
    ('periscope', 'periscope')
)
Phase4AnimList = (
    ('sit', 'sit'),
    ('sit-start', 'intoSit'),
    ('swim', 'swim'),
    ('tug-o-war', 'tug-o-war'),
    ('sad-walk', 'losewalk'),
    ('sad-neutral', 'sad-neutral'),
    ('up', 'up'),
    ('down', 'down'),
    ('left', 'left'),
    ('right', 'right'),
    ('applause', 'applause'),
    ('confused', 'confused'),
    ('bow', 'bow'),
    ('curtsy', 'curtsy'),
    ('bored', 'bored'),
    ('think', 'think'),
    ('battlecast', 'fish'),
    ('cast', 'cast'),
    ('castlong', 'castlong'),
    ('fish-end', 'fishEND'),
    ('fish-neutral', 'fishneutral'),
    ('fish-again', 'fishAGAIN'),
    ('reel', 'reel'),
    ('reel-H', 'reelH'),
    ('reel-neutral', 'reelneutral'),
    ('pole', 'pole'),
    ('pole-neutral', 'poleneutral'),
    ('slip-forward', 'slip-forward'),
    ('slip-backward', 'slip-backward'),
    ('catch-neutral', 'gameneutral'),
    ('catch-run', 'gamerun'),
    ('catch-eatneutral', 'eat_neutral'),
    ('catch-eatnrun', 'eatnrun'),
    ('catch-intro-throw', 'gameThrow'),
    ('swing', 'swing'),
    ('pet-start', 'petin'),
    ('pet-loop', 'petloop'),
    ('pet-end', 'petend'),
    ('scientistJealous', 'scientistJealous'),
    ('scientistEmcee', 'scientistEmcee'),
    ('scientistWork', 'scientistWork'),
    ('scientistGame', 'scientistGame')
)
Phase5AnimList = (
    ('water-gun', 'water-gun'),
    ('hold-bottle', 'hold-bottle'),
    ('firehose', 'firehose'),
    ('spit', 'spit'),
    ('tickle', 'tickle'),
    ('smooch', 'smooch'),
    ('happy-dance', 'happy-dance'),
    ('sprinkle-dust', 'sprinkle-dust'),
    ('juggle', 'juggle'),
    ('climb', 'climb'),
    ('sound', 'shout'),
    ('toss', 'toss'),
    ('hold-magnet', 'hold-magnet'),
    ('hypnotize', 'hypnotize'),
    ('struggle', 'struggle'),
    ('lose', 'lose'),
    ('melt', 'melt')
)
Phase5_5AnimList = (
    ('takePhone', 'takePhone'),
    ('phoneNeutral', 'phoneNeutral'),
    ('phoneBack', 'phoneBack'),
    ('bank', 'jellybeanJar'),
    ('callPet', 'callPet'),
    ('feedPet', 'feedPet'),
    ('start-dig', 'into_dig'),
    ('loop-dig', 'loop_dig'),
    ('water', 'water')
)
Phase6AnimList = (
    ('headdown-putt', 'headdown-putt'),
    ('into-putt', 'into-putt'),
    ('loop-putt', 'loop-putt'),
    ('rotateL-putt', 'rotateL-putt'),
    ('rotateR-putt', 'rotateR-putt'),
    ('swing-putt', 'swing-putt'),
    ('look-putt', 'look-putt'),
    ('lookloop-putt', 'lookloop-putt'),
    ('bad-putt', 'bad-putt'),
    ('badloop-putt', 'badloop-putt'),
    ('good-putt', 'good-putt')
)
Phase9AnimList = (
    ('push', 'push'),
)
Phase10AnimList = (
    ('leverReach', 'leverReach'),
    ('leverPull', 'leverPull'),
    ('leverNeutral', 'leverNeutral')
)
Phase12AnimList = (
)
LegDict = {
     's':'/models/char/tt_a_chr_dgs_shorts_legs_',
     'm':'/models/char/tt_a_chr_dgm_shorts_legs_',
     'l':'/models/char/tt_a_chr_dgl_shorts_legs_'
}
TorsoDict = {
     's':'/models/char/dogSS_Naked-torso-',
     'm':'/models/char/dogMM_Naked-torso-',
     'l':'/models/char/dogLL_Naked-torso-',
     'ss':'/models/char/tt_a_chr_dgs_shorts_torso_',
     'ms':'/models/char/tt_a_chr_dgm_shorts_torso_',
     'ls':'/models/char/tt_a_chr_dgl_shorts_torso_',
     'sd':'/models/char/tt_a_chr_dgs_skirt_torso_',
     'md':'/models/char/tt_a_chr_dgm_skirt_torso_',
     'ld':'/models/char/tt_a_chr_dgl_skirt_torso_'
}

def loadModels():
    global Preloaded
    preloadAvatars = 0
    if preloadAvatars:
        def loadTex(path):
            tex = loader.loadTexture(path)
            tex.setMinfilter(Texture.FTLinearMipmapLinear)
            tex.setMagfilter(Texture.FTLinear)
            Preloaded.append(tex)

        for shirt in ToonDNA.Shirts:
            loadTex(shirt)
        for sleeve in ToonDNA.Sleeves:
            loadTex(sleeve)
        for short in ToonDNA.BoyShorts:
            loadTex(short)
        for bottom in ToonDNA.GirlBottoms:
            loadTex(bottom[0])
        for key in LegDict.keys():
            fileRoot = LegDict[key]
            model = loader.loadModelNode('phase_3' + fileRoot + '1000')
            Preloaded.append(model)
            model = loader.loadModelNode('phase_3' + fileRoot + '500')
            Preloaded.append(model)
            model = loader.loadModelNode('phase_3' + fileRoot + '250')
            Preloaded.append(model)
        for key in TorsoDict.keys():
            fileRoot = TorsoDict[key]
            model = loader.loadModelNode('phase_3' + fileRoot + '1000')
            Preloaded.append(model)
            if len(key) > 1:
                model = loader.loadModelNode('phase_3' + fileRoot + '500')
                Preloaded.append(model)
                model = loader.loadModelNode('phase_3' + fileRoot + '250')
                Preloaded.append(model)
        for key in HeadDict.keys():
            fileRoot = HeadDict[key]
            model = loader.loadModelNode('phase_3' + fileRoot + '1000')
            Preloaded.append(model)
            model = loader.loadModelNode('phase_3' + fileRoot + '500')
            Preloaded.append(model)
            model = loader.loadModelNode('phase_3' + fileRoot + '250')
            Preloaded.append(model)

def loadBasicAnims():
    loadPhaseAnims()

def unloadBasicAnims():
    loadPhaseAnims(0)

def loadTutorialBattleAnims():
    loadPhaseAnims('phase_3.5')

def unloadTutorialBattleAnims():
    loadPhaseAnims('phase_3.5', 0)

def loadMinigameAnims():
    loadPhaseAnims('phase_4')

def unloadMinigameAnims():
    loadPhaseAnims('phase_4', 0)

def loadBattleAnims():
    loadPhaseAnims('phase_5')

def unloadBattleAnims():
    loadPhaseAnims('phase_5', 0)

def loadSellbotHQAnims():
    loadPhaseAnims('phase_9')

def unloadSellbotHQAnims():
    loadPhaseAnims('phase_9', 0)

def loadCashbotHQAnims():
    loadPhaseAnims('phase_10')

def unloadCashbotHQAnims():
    loadPhaseAnims('phase_10', 0)

def loadBossbotHQAnims():
    loadPhaseAnims('phase_12')

def unloadBossbotHQAnims():
    loadPhaseAnims('phase_12', 0)

def loadPhaseAnims(phaseStr = 'phase_3', loadFlag = 1):
    if phaseStr == 'phase_3':
        animList = Phase3AnimList
    elif phaseStr == 'phase_3.5':
        animList = Phase3_5AnimList
    elif phaseStr == 'phase_4':
        animList = Phase4AnimList
    elif phaseStr == 'phase_5':
        animList = Phase5AnimList
    elif phaseStr == 'phase_5.5':
        animList = Phase5_5AnimList
    elif phaseStr == 'phase_6':
        animList = Phase6AnimList
    elif phaseStr == 'phase_9':
        animList = Phase9AnimList
    elif phaseStr == 'phase_10':
        animList = Phase10AnimList
    elif phaseStr == 'phase_12':
        animList = Phase12AnimList
    else:
        self.notify.error('Unknown phase string %s' % phaseStr)
    for key in LegDict.keys():
        for anim in animList:
            if loadFlag:
                pass
            elif LegsAnimDict[key].has_key(anim[0]):
                if base.localAvatar.style.legs == key:
                    base.localAvatar.unloadAnims([anim[0]], 'legs', None)
    for key in TorsoDict.keys():
        for anim in animList:
            if loadFlag:
                pass
            elif TorsoAnimDict[key].has_key(anim[0]):
                if base.localAvatar.style.torso == key:
                    base.localAvatar.unloadAnims([anim[0]], 'torso', None)
    for key in HeadDict.keys():
        if string.find(key, 'd') >= 0:
            for anim in animList:
                if loadFlag:
                    pass
                elif HeadAnimDict[key].has_key(anim[0]):
                    if base.localAvatar.style.head == key:
                        base.localAvatar.unloadAnims([anim[0]], 'head', None)

def compileGlobalAnimList():
    phaseList = [
     Phase3AnimList,
     Phase3_5AnimList,
     Phase4AnimList,
     Phase5AnimList,
     Phase5_5AnimList,
     Phase6AnimList,
     Phase9AnimList,
     Phase10AnimList,
     Phase12AnimList
    ]
    phaseStrList = [
     'phase_3',
     'phase_3.5',
     'phase_4',
     'phase_5',
     'phase_5.5',
     'phase_6',
     'phase_9',
     'phase_10',
     'phase_12'
    ]
    for animList in phaseList:
        phaseStr = phaseStrList[phaseList.index(animList)]
        for key in LegDict.keys():
            LegsAnimDict.setdefault(key, {})
            for anim in animList:
                file = phaseStr + LegDict[key] + anim[1]
                LegsAnimDict[key][anim[0]] = file
        for key in TorsoDict.keys():
            TorsoAnimDict.setdefault(key, {})
            for anim in animList:
                file = phaseStr + TorsoDict[key] + anim[1]
                TorsoAnimDict[key][anim[0]] = file
        for key in HeadDict.keys():
            if string.find(key, 'd') >= 0:
                HeadAnimDict.setdefault(key, {})
                for anim in animList:
                    file = phaseStr + HeadDict[key] + anim[1]
                    HeadAnimDict[key][anim[0]] = file

def loadDialog():
    global CatDialogueArray
    global PigDialogueArray
    global BearDialogueArray
    global DuckDialogueArray
    global RabbitDialogueArray
    global MouseDialogueArray
    global DogDialogueArray
    global HorseDialogueArray
    global MonkeyDialogueArray
    loadPath = 'phase_3.5/audio/dial/'
    DogDialogueFiles = (
     'AV_dog_short', 'AV_dog_med', 'AV_dog_long', 'AV_dog_question', 'AV_dog_exclaim', 'AV_dog_howl'
    )
    for file in DogDialogueFiles:
        DogDialogueArray.append(base.loadSfx(loadPath + file + '.mp3'))
    catDialogueFiles = (
     'AV_cat_short', 'AV_cat_med', 'AV_cat_long', 'AV_cat_question', 'AV_cat_exclaim', 'AV_cat_howl'
    )
    for file in catDialogueFiles:
        CatDialogueArray.append(base.loadSfx(loadPath + file + '.mp3'))
    horseDialogueFiles = (
     'AV_horse_short', 'AV_horse_med', 'AV_horse_long', 'AV_horse_question', 'AV_horse_exclaim', 'AV_horse_howl'
    )
    for file in horseDialogueFiles:
        HorseDialogueArray.append(base.loadSfx(loadPath + file + '.mp3'))
    rabbitDialogueFiles = (
     'AV_rabbit_short', 'AV_rabbit_med', 'AV_rabbit_long', 'AV_rabbit_question', 'AV_rabbit_exclaim', 'AV_rabbit_howl'
    )
    for file in rabbitDialogueFiles:
        RabbitDialogueArray.append(base.loadSfx(loadPath + file + '.mp3'))
    mouseDialogueFiles = (
     'AV_mouse_short', 'AV_mouse_med', 'AV_mouse_long', 'AV_mouse_question', 'AV_mouse_exclaim', 'AV_mouse_howl'
    )
    for file in mouseDialogueFiles:
        MouseDialogueArray.append(base.loadSfx(loadPath + file + '.mp3'))
    duckDialogueFiles = (
     'AV_duck_short', 'AV_duck_med', 'AV_duck_long', 'AV_duck_question', 'AV_duck_exclaim', 'AV_duck_howl'
    )
    for file in duckDialogueFiles:
        DuckDialogueArray.append(base.loadSfx(loadPath + file + '.mp3'))
    monkeyDialogueFiles = (
     'AV_monkey_short', 'AV_monkey_med', 'AV_monkey_long', 'AV_monkey_question', 'AV_monkey_exclaim', 'AV_monkey_howl'
    )
    for file in monkeyDialogueFiles:
        MonkeyDialogueArray.append(base.loadSfx(loadPath + file + '.mp3'))
    bearDialogueFiles = (
     'AV_bear_short', 'AV_bear_med', 'AV_bear_long', 'AV_bear_question', 'AV_bear_exclaim', 'AV_bear_howl'
    )
    for file in bearDialogueFiles:
        BearDialogueArray.append(base.loadSfx(loadPath + file + '.mp3'))
    pigDialogueFiles = (
     'AV_pig_short', 'AV_pig_med', 'AV_pig_long', 'AV_pig_question', 'AV_pig_exclaim', 'AV_pig_howl'
    )
    for file in pigDialogueFiles:
        PigDialogueArray.append(base.loadSfx(loadPath + file + '.mp3'))

def unloadDialog():
    global CatDialogueArray
    global PigDialogueArray
    global BearDialogueArray
    global DuckDialogueArray
    global RabbitDialogueArray
    global MouseDialogueArray
    global DogDialogueArray
    global HorseDialogueArray
    global MonkeyDialogueArray
    DogDialogueArray = []
    CatDialogueArray = []
    HorseDialogueArray = []
    RabbitDialogueArray = []
    MouseDialogueArray = []
    DuckDialogueArray = []
    MonkeyDialogueArray = []
    BearDialogueArray = []
    PigDialogueArray = []

class Toon(Avatar.Avatar, ToonHead):

    notify = DirectNotifyGlobal.directNotify.newCategory('Toon')

    def __swapToonClothes(self, dna):
        self.setStyle(dna)
        self.generateToonClothes(fromNet=1)

    def __returnToLastAnim(self, task):
        if self.playingAnim:
            self.loop(self.playingAnim)
        elif self.hp > 0:
            self.loop('neutral')
        else:
            self.loop('sad-neutral')
        return Task.done

    def __init__(self):
        try:
            self.Toon_initialized
            return None
        except:
            self.Toon_initialized = 1
        Avatar.Avatar.__init__(self)
        ToonHead.__init__(self)
        self.forwardSpeed = 0.0
        self.rotateSpeed = 0.0
        self.avatarType = 'toon'
        self.standWalkRunReverse = (
            ('neutral', 1.0), ('walk', 1.0), ('run', 1.0), ('walk', -1.0)
        )
        self.playingAnim = None
        self.playingRate = None
        self.forceJumpIdle = False
        self.hatNodes = []
        self.glassesNodes = []
        self.backpackNodes = []
        self.hat = (0, 0, 0)
        self.glasses = (0, 0, 0)
        self.backpack = (0, 0, 0)
        self.shoes = (0, 0, 0)
        self.defaultColorScale = None
        self.setFont(getToonFont())
        self.soundChatBubble = base.loadSfx('phase_3/audio/sfx/GUI_balloon_popup.mp3')
        self.animFSM = ClassicFSM('Toon', [
         State('off', self.enterOff, self.exitOff),
         State('neutral', self.enterNeutral, self.exitNeutral),
         State('victory', self.enterVictory, self.exitVictory),
         State('Happy', self.enterHappy, self.exitHappy),
         State('Sad', self.enterSad, self.exitSad),
         State('Catching', self.enterCatching, self.exitCatching),
         State('CatchEating', self.enterCatchEating, self.exitCatchEating),
         State('walk', self.enterWalk, self.exitWalk),
         State('jumpSquat', self.enterJumpSquat, self.exitJumpSquat),
         State('jump', self.enterJump, self.exitJump),
         State('jumpAirborne', self.enterJumpAirborne, self.exitJumpAirborne),
         State('jumpLand', self.enterJumpLand, self.exitJumpLand),
         State('run', self.enterRun, self.exitRun),
         State('swim', self.enterSwim, self.exitSwim),
         State('swimhold', self.enterSwimHold, self.exitSwimHold),
         State('dive', self.enterDive, self.exitDive),
         State('cringe', self.enterCringe, self.exitCringe),
         State('Died', self.enterDied, self.exitDied),
         State('TeleportedOut', self.enterTeleportedOut, self.exitTeleportedOut),
         State('SitStart', self.enterSitStart, self.exitSitStart),
         State('Sit', self.enterSit, self.exitSit),
         State('Push', self.enterPush, self.exitPush),
         State('jump-idle', self.enterJumpIdle, self.exitRunningJumpIdle),
         State('running-jump-idle', self.enterRunningJumpIdle, self.exitRunningJumpIdle)
        ], 'off', 'off')
        animStateList = self.animFSM.getStates()
        self.animFSM.enterInitialState()

    def delete(self):
        try:
            self.Toon_deleted
        except:
            self.Toon_deleted = 1
            self.rightHands = None
            self.rightHand = None
            self.leftHands = None
            self.leftHand = None
            self.headParts = None
            self.torsoParts = None
            self.hipsParts = None
            self.legsParts = None
            del self.animFSM
            ToonHead.delete(self)

    def updateToonDNA(self, newDNA, fForce=0):
        self.style.gender = newDNA.getGender()
        oldDNA = self.style
        if fForce or (newDNA.head != oldDNA.head):
            self.swapToonHead(newDNA.head)
        if fForce or (newDNA.torso != oldDNA.torso):
            self.swapToonTorso(newDNA.torso, genClothes=0)
            self.loop('neutral')
        if fForce or (newDNA.legs != oldDNA.legs):
            self.swapToonLegs(newDNA.legs)
        self.swapToonColor(newDNA)
        self.__swapToonClothes(newDNA)

    def setDNAString(self, dnaString):
        newDNA = ToonDNA.ToonDNA()
        newDNA.makeFromNetString(dnaString)
        if len(newDNA.torso) < 2:
            newDNA.torso = newDNA.torso + 's'
        self.setDNA(newDNA)

    def setDNA(self, dna):
        if self.style:
            self.updateToonDNA(dna)
        else:
            self.style = dna
            self.generateToon()

    def parentToonParts(self):
        if self.hasLOD():
            for lodName in self.getLODNames():
                if not self.getPart('torso', lodName).find('**/def_head').isEmpty():
                    self.attach('head', 'torso', 'def_head', lodName)
                else:
                    self.attach('head', 'torso', 'joint_head', lodName)
                self.attach('torso', 'legs', 'joint_hips', lodName)
        else:
            self.attach('head', 'torso', 'joint_head')
            self.attach('torso', 'legs', 'joint_hips')

    def unparentToonParts(self):
        if self.hasLOD():
            for lodName in self.getLODNames():
                self.getPart('head', lodName).reparentTo(self.getLOD(lodName))
                self.getPart('torso', lodName).reparentTo(self.getLOD(lodName))
                self.getPart('legs', lodName).reparentTo(self.getLOD(lodName))
        else:
            self.getPart('head').reparentTo(self.getGeomNode())
            self.getPart('torso').reparentTo(self.getGeomNode())
            self.getPart('legs').reparentTo(self.getGeomNode())

    def setSpeed(self, forwardSpeed, rotateSpeed):
        self.forwardSpeed = forwardSpeed
        self.rotateSpeed = rotateSpeed
        action = None
        if self.standWalkRunReverse:
            if forwardSpeed >= RunCutOff:
                action = RUN_INDEX
            elif forwardSpeed > WalkCutOff:
                action = WALK_INDEX
            elif forwardSpeed < -WalkCutOff:
                action = REVERSE_INDEX
            elif rotateSpeed != 0.0:
                action = WALK_INDEX
            else:
                action = STAND_INDEX
            anim, rate = self.standWalkRunReverse[action]
            if anim != self.playingAnim:
                self.playingAnim = anim
                self.playingRate = rate
                self.stop()
                self.loop(anim)
                self.setPlayRate(rate, anim)
            elif rate != self.playingRate:
                self.playingRate = rate
                self.setPlayRate(rate, anim)
        return action

    def setLODs(self):
        self.setLODNode()
        levelOneIn = 20
        levelOneOut = 0
        levelTwoIn = 80
        levelTwoOut = 20
        levelThreeIn = 280
        levelThreeOut = 80
        self.addLOD(1000, levelOneIn, levelOneOut)
        self.addLOD(500, levelTwoIn, levelTwoOut)
        self.addLOD(250, levelThreeIn, levelThreeOut)

    def generateToon(self):
        self.setLODs()
        self.generateToonLegs()
        self.generateToonHead()
        self.generateToonTorso()
        self.generateToonColor()
        self.parentToonParts()
        self.rescaleToon()
        self.resetHeight()
        self.setupToonNodes()

    def setupToonNodes(self):
        rightHand = NodePath('rightHand')
        self.rightHand = None
        self.rightHands = []
        leftHand = NodePath('leftHand')
        self.leftHands = []
        self.leftHand = None
        for lodName in self.getLODNames():
            hand = self.getPart('torso', lodName).find('**/joint_Rhold')
            if not self.getPart('torso', lodName).find('**/def_joint_right_hold').isEmpty():
                hand = self.getPart('torso', lodName).find('**/def_joint_right_hold')
            self.rightHands.append(hand)
            rightHand = rightHand.instanceTo(hand)
            if not self.getPart('torso', lodName).find('**/def_joint_left_hold').isEmpty():
                hand = self.getPart('torso', lodName).find('**/def_joint_left_hold')
            self.leftHands.append(hand)
            leftHand = leftHand.instanceTo(hand)
            if self.rightHand == None:
                self.rightHand = rightHand
            if self.leftHand == None:
                self.leftHand = leftHand
        self.headParts = self.findAllMatches('**/__Actor_head')
        self.legsParts = self.findAllMatches('**/__Actor_legs')
        self.hipsParts = self.legsParts.findAllMatches('**/joint_hips')
        self.torsoParts = self.hipsParts.findAllMatches('**/__Actor_torso')

    def rescaleToon(self):
        animalStyle = self.style.getAnimal()
        bodyScale = toonBodyScales[animalStyle]
        headScale = toonHeadScales[animalStyle]
        self.setAvatarScale(bodyScale)
        for lod in self.getLODNames():
            self.getPart('head', lod).setScale(headScale)

    def getBodyScale(self):
        animalStyle = self.style.getAnimal()
        bodyScale = toonBodyScales[animalStyle]
        return bodyScale

    def resetHeight(self):
        if hasattr(self, 'style') and self.style:
            animal = self.style.getAnimal()
            bodyScale = toonBodyScales[animal]
            headScale = toonHeadScales[animal][2]
            shoulderHeight = legHeightDict[self.style.legs] * bodyScale + torsoHeightDict[self.style.torso] * bodyScale
            height = shoulderHeight + headHeightDict[self.style.head] * headScale
            self.shoulderHeight = shoulderHeight
            self.setHeight(height)

    def generateToonLegs(self, copy=1):
        legStyle = self.style.legs
        filePrefix = LegDict.get(legStyle)
        if filePrefix is None:
            self.notify.error('unknown leg style:%s' % legStyle)
        self.loadModel('phase_3' + filePrefix + '1000', 'legs', '1000', copy)
        self.loadModel('phase_3' + filePrefix + '500', 'legs', '500', copy)
        self.loadModel('phase_3' + filePrefix + '250', 'legs', '250', copy)
        if not copy:
            self.showPart('legs', '1000')
            self.showPart('legs', '500')
            self.showPart('legs', '250')
        self.loadAnims(LegsAnimDict[legStyle], 'legs', '1000')
        self.loadAnims(LegsAnimDict[legStyle], 'legs', '500')
        self.loadAnims(LegsAnimDict[legStyle], 'legs', '250')
        self.findAllMatches('**/boots_short').stash()
        self.findAllMatches('**/boots_long').stash()
        self.findAllMatches('**/shoes').stash()

    def swapToonLegs(self, legStyle, copy=1):
        self.unparentToonParts()
        self.removePart('legs', '1000')
        self.removePart('legs', '500')
        self.removePart('legs', '250')
        self.style.legs = legStyle
        self.generateToonLegs(copy)
        self.generateToonColor()
        self.parentToonParts()
        self.rescaleToon()
        self.resetHeight()

    def generateToonTorso(self, copy=1, genClothes=1):
        torsoStyle = self.style.torso
        filePrefix = TorsoDict.get(torsoStyle)
        if filePrefix is None:
            self.notify.error('unknown torso style:%s' % torsoStyle)
        self.loadModel('phase_3' + filePrefix + '1000', 'torso', '1000', copy)
        if len(torsoStyle) == 1:
            self.loadModel('phase_3' + filePrefix + '1000', 'torso', '500', copy)
            self.loadModel('phase_3' + filePrefix + '1000', 'torso', '250', copy)
        else:
            self.loadModel('phase_3' + filePrefix + '500', 'torso', '500', copy)
            self.loadModel('phase_3' + filePrefix + '250', 'torso', '250', copy)
        if not copy:
            self.showPart('torso', '1000')
            self.showPart('torso', '500')
            self.showPart('torso', '250')
        self.loadAnims(TorsoAnimDict[torsoStyle], 'torso', '1000')
        self.loadAnims(TorsoAnimDict[torsoStyle], 'torso', '500')
        self.loadAnims(TorsoAnimDict[torsoStyle], 'torso', '250')
        if genClothes == 1 and not len(torsoStyle) == 1:
            self.generateToonClothes()

    def swapToonTorso(self, torsoStyle, copy=1, genClothes=1):
        self.unparentToonParts()
        self.removePart('torso', '1000')
        self.removePart('torso', '500')
        self.removePart('torso', '250')
        self.style.torso = torsoStyle
        self.generateToonTorso(copy, genClothes)
        self.generateToonColor()
        self.parentToonParts()
        self.rescaleToon()
        self.resetHeight()
        self.setupToonNodes()
        self.generateBackpack()

    def generateToonHead(self, copy=1):
        headHeight = ToonHead.generateToonHead(self, copy, self.style, ('1000', '500', '250'))
        if self.style.getAnimal() == 'dog':
            self.loadAnims(HeadAnimDict[self.style.head], 'head', '1000')
            self.loadAnims(HeadAnimDict[self.style.head], 'head', '500')
            self.loadAnims(HeadAnimDict[self.style.head], 'head', '250')

    def swapToonHead(self, headStyle, copy=1):
        self.stopLookAroundNow()
        self.eyelids.request('open')
        self.unparentToonParts()
        self.removePart('head', '1000')
        self.removePart('head', '500')
        self.removePart('head', '250')
        self.style.head = headStyle
        self.generateToonHead(copy)
        self.generateToonColor()
        self.parentToonParts()
        self.rescaleToon()
        self.resetHeight()
        self.eyelids.request('open')
        self.startLookAround()

    def generateToonColor(self):
        ToonHead.generateToonColor(self, self.style)
        armColor = self.style.getArmColor()
        gloveColor = self.style.getGloveColor()
        legColor = self.style.getLegColor()
        for lodName in self.getLODNames():
            torso = self.getPart('torso', lodName)
            if len(self.style.torso) == 1:
                parts = torso.findAllMatches('**/torso*')
                parts.setColor(armColor)
            for pieceName in ('arms', 'neck'):
                piece = torso.find('**/' + pieceName)
                piece.setColor(armColor)
            hands = torso.find('**/hands')
            hands.setColor(gloveColor)
            legs = self.getPart('legs', lodName)
            for pieceName in ('legs', 'feet'):
                piece = legs.find('**/%s;+s' % pieceName)
                piece.setColor(legColor)

    def swapToonColor(self, dna):
        self.setStyle(dna)
        self.generateToonColor()

    def generateToonClothes(self, fromNet=0):
        swappedTorso = 0
        if self.hasLOD():
            if self.style.getGender() == 'f' and fromNet == 0:
                try:
                    bottomPair = ToonDNA.GirlBottoms[self.style.botTex]
                except:
                    bottomPair = ToonDNA.GirlBottoms[0]
                if len(self.style.torso) < 2:
                    return 0
                elif self.style.torso[1] == 's' and bottomPair[1] == ToonDNA.SKIRT:
                    self.swapToonTorso(self.style.torso[0] + 'd', genClothes=0)
                    swappedTorso = 1
                elif self.style.torso[1] == 'd' and bottomPair[1] == ToonDNA.SHORTS:
                    self.swapToonTorso(self.style.torso[0] + 's', genClothes=0)
                    swappedTorso = 1
            try:
                texName = ToonDNA.Shirts[self.style.topTex]
            except:
                texName = ToonDNA.Shirts[0]
            shirtTex = loader.loadTexture(texName, okMissing=True)
            if shirtTex is None:
                shirtTex = loader.loadTexture(ToonDNA.Shirts[0])
            shirtTex.setMinfilter(Texture.FTLinearMipmapLinear)
            shirtTex.setMagfilter(Texture.FTLinear)
            try:
                shirtColor = ToonDNA.ClothesColors[self.style.topTexColor]
            except:
                shirtColor = ToonDNA.ClothesColors[0]
            try:
                texName = ToonDNA.Sleeves[self.style.sleeveTex]
            except:
                texName = ToonDNA.Sleeves[0]
            sleeveTex = loader.loadTexture(texName, okMissing=True)
            if sleeveTex is None:
                sleeveTex = loader.loadTexture(ToonDNA.Sleeves[0])
            sleeveTex.setMinfilter(Texture.FTLinearMipmapLinear)
            sleeveTex.setMagfilter(Texture.FTLinear)
            try:
                sleeveColor = ToonDNA.ClothesColors[self.style.sleeveTexColor]
            except:
                sleeveColor = ToonDNA.ClothesColors[0]
            if self.style.getGender() == 'm':
                try:
                    texName = ToonDNA.BoyShorts[self.style.botTex]
                except:
                    texName = ToonDNA.BoyShorts[0]
            else:
                try:
                    texName = ToonDNA.GirlBottoms[self.style.botTex][0]
                except:
                    texName = ToonDNA.GirlBottoms[0][0]
            bottomTex = loader.loadTexture(texName, okMissing=True)
            if bottomTex is None:
                if self.style.getGender() == 'm':
                    bottomTex = loader.loadTexture(ToonDNA.BoyShorts[0])
                else:
                    bottomTex = loader.loadTexture(ToonDNA.GirlBottoms[0][0])
            bottomTex.setMinfilter(Texture.FTLinearMipmapLinear)
            bottomTex.setMagfilter(Texture.FTLinear)
            try:
                bottomColor = ToonDNA.ClothesColors[self.style.botTexColor]
            except:
                bottomColor = ToonDNA.ClothesColors[0]
            darkBottomColor = bottomColor * 0.5
            darkBottomColor.setW(1.0)
            for lodName in self.getLODNames():
                thisPart = self.getPart('torso', lodName)
                top = thisPart.find('**/torso-top')
                top.setTexture(shirtTex, 1)
                top.setColor(shirtColor)
                sleeves = thisPart.find('**/sleeves')
                sleeves.setTexture(sleeveTex, 1)
                sleeves.setColor(sleeveColor)
                bottoms = thisPart.findAllMatches('**/torso-bot')
                for bottomNum in range(0, bottoms.getNumPaths()):
                    bottom = bottoms.getPath(bottomNum)
                    bottom.setTexture(bottomTex, 1)
                    bottom.setColor(bottomColor)
                caps = thisPart.findAllMatches('**/torso-bot-cap')
                caps.setColor(darkBottomColor)
        return swappedTorso

    def generateHat(self, fromRTM=False):
        hat = self.getHat()
        if hat[0] >= len(ToonDNA.HatModels):
            return None
        if len(self.hatNodes) > 0:
            for hatNode in self.hatNodes:
                hatNode.removeNode()
            self.hatNodes = []
        self.showEars()
        if hat[0] != 0:
            hatGeom = loader.loadModel(ToonDNA.HatModels[hat[0]], okMissing=True)
            if hatGeom:
                if hat[0] == 54:
                    self.hideEars()
                if hat[1] != 0:
                    texName = ToonDNA.HatTextures[hat[1]]
                    tex = loader.loadTexture(texName, okMissing=True)
                    if tex is None:
                        pass
                    else:
                        tex.setMinfilter(Texture.FTLinearMipmapLinear)
                        tex.setMagfilter(Texture.FTLinear)
                        hatGeom.setTexture(tex, 1)
                if fromRTM:
                    reload(AccessoryGlobals)
                transOffset = None
                if AccessoryGlobals.ExtendedHatTransTable.get(hat[0]):
                    transOffset = AccessoryGlobals.ExtendedHatTransTable[hat[0]].get(self.style.head[:2])
                if transOffset is None:
                    transOffset = AccessoryGlobals.HatTransTable.get(self.style.head[:2])
                    if transOffset is None:
                        return None
                hatGeom.setPos(transOffset[0][0], transOffset[0][1], transOffset[0][2])
                hatGeom.setHpr(transOffset[1][0], transOffset[1][1], transOffset[1][2])
                hatGeom.setScale(transOffset[2][0], transOffset[2][1], transOffset[2][2])
                headNodes = self.findAllMatches('**/__Actor_head')
                for headNode in headNodes:
                    hatNode = headNode.attachNewNode('hatNode')
                    self.hatNodes.append(hatNode)
                    hatGeom.instanceTo(hatNode)

    def generateGlasses(self, fromRTM=False):
        glasses = self.getGlasses()
        if glasses[0] >= len(ToonDNA.GlassesModels):
            return None
        if len(self.glassesNodes) > 0:
            for glassesNode in self.glassesNodes:
                glassesNode.removeNode()
            self.glassesNodes = []
        self.showEyelashes()
        if glasses[0] != 0:
            glassesGeom = loader.loadModel(ToonDNA.GlassesModels[glasses[0]], okMissing=True)
            if glassesGeom:
                if glasses[0] in [15, 16]:
                    self.hideEyelashes()
                if glasses[1] != 0:
                    texName = ToonDNA.GlassesTextures[glasses[1]]
                    tex = loader.loadTexture(texName, okMissing=True)
                    if tex is None:
                        pass
                    else:
                        tex.setMinfilter(Texture.FTLinearMipmapLinear)
                        tex.setMagfilter(Texture.FTLinear)
                        glassesGeom.setTexture(tex, 1)
                if fromRTM:
                    reload(AccessoryGlobals)
                transOffset = None
                if AccessoryGlobals.ExtendedGlassesTransTable.get(glasses[0]):
                    transOffset = AccessoryGlobals.ExtendedGlassesTransTable[glasses[0]].get(self.style.head[:2])
                if transOffset is None:
                    transOffset = AccessoryGlobals.GlassesTransTable.get(self.style.head[:2])
                    if transOffset is None:
                        return None
                glassesGeom.setPos(transOffset[0][0], transOffset[0][1], transOffset[0][2])
                glassesGeom.setHpr(transOffset[1][0], transOffset[1][1], transOffset[1][2])
                glassesGeom.setScale(transOffset[2][0], transOffset[2][1], transOffset[2][2])
                headNodes = self.findAllMatches('**/__Actor_head')
                for headNode in headNodes:
                    glassesNode = headNode.attachNewNode('glassesNode')
                    self.glassesNodes.append(glassesNode)
                    glassesGeom.instanceTo(glassesNode)

    def generateBackpack(self, fromRTM=False):
        backpack = self.getBackpack()
        if backpack[0] >= len(ToonDNA.BackpackModels):
            return None
        if len(self.backpackNodes) > 0:
            for backpackNode in self.backpackNodes:
                backpackNode.removeNode()
            self.backpackNodes = []
        if backpack[0] != 0:
            geom = loader.loadModel(ToonDNA.BackpackModels[backpack[0]], okMissing=True)
            if geom:
                if backpack[1] != 0:
                    texName = ToonDNA.BackpackTextures[backpack[1]]
                    tex = loader.loadTexture(texName, okMissing=True)
                    if tex is None:
                        pass
                    else:
                        tex.setMinfilter(Texture.FTLinearMipmapLinear)
                        tex.setMagfilter(Texture.FTLinear)
                        geom.setTexture(tex, 1)
                if fromRTM:
                    reload(AccessoryGlobals)
                transOffset = None
                if AccessoryGlobals.ExtendedBackpackTransTable.get(backpack[0]):
                    transOffset = AccessoryGlobals.ExtendedBackpackTransTable[backpack[0]].get(self.style.torso[:1])
                if transOffset is None:
                    transOffset = AccessoryGlobals.BackpackTransTable.get(self.style.torso[:1])
                    if transOffset is None:
                        return None
                geom.setPos(transOffset[0][0], transOffset[0][1], transOffset[0][2])
                geom.setHpr(transOffset[1][0], transOffset[1][1], transOffset[1][2])
                geom.setScale(transOffset[2][0], transOffset[2][1], transOffset[2][2])
                nodes = self.findAllMatches('**/def_joint_attachFlower')
                for node in nodes:
                    theNode = node.attachNewNode('backpackNode')
                    self.backpackNodes.append(theNode)
                    geom.instanceTo(theNode)

    def generateShoes(self):
        shoes = self.getShoes()
        if shoes[0] >= len(ToonDNA.ShoesModels):
            return None
        self.findAllMatches('**/feet;+s').stash()
        self.findAllMatches('**/boots_short;+s').stash()
        self.findAllMatches('**/boots_long;+s').stash()
        self.findAllMatches('**/shoes;+s').stash()
        geoms = self.findAllMatches('**/%s;+s' % ToonDNA.ShoesModels[shoes[0]])
        for geom in geoms:
            geom.unstash()
        if shoes[0] != 0:
            for geom in geoms:
                texName = ToonDNA.ShoesTextures[shoes[1]]
                if self.style.legs == 'l' and shoes[0] == 3:
                    texName = texName[:-4] + 'LL.jpg'
                tex = loader.loadTexture(texName, okMissing=True)
                if tex is None:
                    pass
                else:
                    tex.setMinfilter(Texture.FTLinearMipmapLinear)
                    tex.setMagfilter(Texture.FTLinear)
                    geom.setTexture(tex, 1)

    def generateToonAccessories(self):
        self.generateHat()
        self.generateGlasses()
        self.generateBackpack()
        self.generateShoes()

    def setHat(self, hatIdx, textureIdx, colorIdx, fromRTM=False):
        self.hat = (hatIdx, textureIdx, colorIdx)
        self.generateHat(fromRTM=fromRTM)

    def getHat(self):
        return self.hat

    def setGlasses(self, glassesIdx, textureIdx, colorIdx, fromRTM=False):
        self.glasses = (glassesIdx, textureIdx, colorIdx)
        self.generateGlasses(fromRTM=fromRTM)

    def getGlasses(self):
        return self.glasses

    def setBackpack(self, backpackIdx, textureIdx, colorIdx, fromRTM=False):
        self.backpack = (backpackIdx, textureIdx, colorIdx)
        self.generateBackpack(fromRTM=fromRTM)

    def getBackpack(self):
        return self.backpack

    def setShoes(self, shoesIdx, textureIdx, colorIdx):
        self.shoes = (shoesIdx, textureIdx, colorIdx)
        self.generateShoes()

    def getShoes(self):
        return self.shoes

    def getRightHands(self):
        return self.rightHands

    def getLeftHands(self):
        return self.leftHands

    def getHeadParts(self):
        return self.headParts

    def getHipsParts(self):
        return self.hipsParts

    def getTorsoParts(self):
        return self.torsoParts

    def getLegsParts(self):
        return self.legsParts

    def setForceJumpIdle(self, value):
        self.forceJumpIdle = value

    def enterOff(self, animMultiplier=1, ts=0, callback=None, extraArgs=[]):
        self.playingAnim = None

    def exitOff(self):
        return None

    def enterNeutral(self, animMultiplier=1, ts=0, callback=None, extraArgs=[]):
        anim = 'neutral'
        self.pose(anim, int(self.getNumFrames(anim) * self.randGen.random()))
        self.loop(anim, restart=0)
        self.setPlayRate(animMultiplier, anim)
        self.playingAnim = anim

    def exitNeutral(self):
        self.stop()

    def enterVictory(self, animMultiplier=1, ts=0, callback=None, extraArgs=[]):
        anim = 'victory'
        frame = int(ts * self.getFrameRate(anim) * animMultiplier)
        self.pose(anim, frame)
        self.loop('victory', restart=0)
        self.setPlayRate(animMultiplier, 'victory')
        self.playingAnim = anim

    def exitVictory(self):
        self.stop()

    def enterHappy(self, animMultiplier=1, ts=0, callback=None, extraArgs=[]):
        self.playingAnim = None
        self.playingRate = None
        self.standWalkRunReverse = (
            ('neutral', 1.0), ('walk', 1.0), ('run', 1.0), ('walk', -1.0)
        )
        self.setSpeed(self.forwardSpeed, self.rotateSpeed)

    def exitHappy(self):
        self.standWalkRunReverse = None
        self.stop()

    def enterSad(self, animMultiplier=1, ts=0, callback=None, extraArgs=[]):
        self.playingAnim = 'sad'
        self.playingRate = None
        self.standWalkRunReverse = (
            ('sad-neutral', 1.0), ('sad-walk', 1.2), ('sad-walk', 1.2), ('sad-walk', -1.0)
        )
        self.setSpeed(0, 0)
        if self.isLocal():
            self.controlManager.disableAvatarJump()

    def exitSad(self):
        self.standWalkRunReverse = None
        self.stop()
        if self.isLocal():
            self.controlManager.enableAvatarJump()

    def enterCatching(self, animMultiplier=1, ts=0, callback=None, extraArgs=[]):
        self.playingAnim = None
        self.playingRate = None
        self.standWalkRunReverse = (
            ('catch-neutral', 1.0), ('catch-run', 1.0), ('catch-run', 1.0), ('catch-run', -1.0)
        )
        self.setSpeed(self.forwardSpeed, self.rotateSpeed)

    def exitCatching(self):
        self.standWalkRunReverse = None
        self.stop()

    def enterCatchEating(self, animMultiplier=1, ts=0, callback=None, extraArgs=[]):
        self.playingAnim = None
        self.playingRate = None
        self.standWalkRunReverse = (
            ('catch-eatneutral', 1.0), ('catch-eatnrun', 1.0), ('catch-eatnrun', 1.0), ('catch-eatnrun', -1.0)
        )
        self.setSpeed(self.forwardSpeed, self.rotateSpeed)

    def exitCatchEating(self):
        self.standWalkRunReverse = None
        self.stop()

    def enterWalk(self, animMultiplier=1, ts=0, callback=None, extraArgs=[]):
        self.loop('walk')
        self.setPlayRate(animMultiplier, 'walk')

    def exitWalk(self):
        self.stop()

    def getJumpDuration(self):
        if self.playingAnim == 'neutral':
            return self.getDuration('jump', 'legs')
        else:
            return self.getDuration('running-jump', 'legs')

    def enterJump(self, animMultiplier=1, ts=0, callback=None, extraArgs=[]):
        if self.playingAnim == 'neutral':
            anim = 'jump'
        else:
            anim = 'running-jump'
        self.playingAnim = anim
        self.setPlayRate(animMultiplier, anim)
        self.play(anim)

    def exitJump(self):
        self.stop()
        self.playingAnim = 'neutral'

    def enterJumpSquat(self, animMultiplier=1, ts=0, callback=None, extraArgs=[]):
        if self.playingAnim == 'neutral':
            anim = 'jump-squat'
        else:
            anim = 'running-jump-squat'
        self.playingAnim = anim
        self.setPlayRate(animMultiplier, anim)
        self.play(anim)

    def exitJumpSquat(self):
        self.stop()
        self.playingAnim = 'neutral'

    def enterJumpAirborne(self, animMultiplier=1, ts=0, callback=None, extraArgs=[]):
        if (self.playingAnim == 'neutral') or self.forceJumpIdle:
            anim = 'jump-idle'
        else:
            anim = 'running-jump-idle'
        self.playingAnim = anim
        self.setPlayRate(animMultiplier, anim)
        self.loop(anim)

    def exitJumpAirborne(self):
        self.stop()
        self.playingAnim = 'neutral'

    def enterJumpLand(self, animMultiplier=1, ts=0, callback=None, extraArgs=[]):
        if self.playingAnim == 'running-jump-idle':
            anim = 'running-jump-land'
            skipStart = 0.2
        else:
            anim = 'jump-land'
            skipStart = 0.0
        self.playingAnim = anim
        self.setPlayRate(animMultiplier, anim)
        self.play(anim)

    def exitJumpLand(self):
        self.stop()
        self.playingAnim = 'neutral'

    def enterRun(self, animMultiplier=1, ts=0, callback=None, extraArgs=[]):
        self.loop('run')
        self.setPlayRate(animMultiplier, 'run')

    def exitRun(self):
        self.stop()

    def enterCringe(self, animMultiplier=1, ts=0, callback=None, extraArgs=[]):
        self.loop('cringe')
        self.getGeomNode().setPos(0, 0, -2)
        self.setPlayRate(animMultiplier, 'cringe')

    def exitCringe(self, animMultiplier=1, ts=0, callback=None, extraArgs=[]):
        self.stop()
        self.getGeomNode().setPos(0, 0, 0)
        self.playingAnim = 'neutral'
        self.setPlayRate(animMultiplier, 'cringe')

    def enterDive(self, animMultiplier=1, ts=0, callback=None, extraArgs=[]):
        self.loop('swim')
        if hasattr(self.getGeomNode(), 'setPos'):
            self.getGeomNode().setPos(0, 0, -2)
            self.setPlayRate(animMultiplier, 'swim')

    def exitDive(self):
        self.stop()
        self.getGeomNode().setPos(0, 0, 0)
        self.playingAnim = 'neutral'

    def enterSwimHold(self, animMultiplier=1, ts=0, callback=None, extraArgs=[]):
        self.getGeomNode().setPos(0, 0, -2)
        self.pose('swim', 55)

    def exitSwimHold(self):
        self.stop()
        self.getGeomNode().setPos(0, 0, 0)
        self.playingAnim = 'neutral'

    def enterSwim(self, animMultiplier=1, ts=0, callback=None, extraArgs=[]):
        self.playingAnim = 'swim'
        self.loop('swim')
        self.setPlayRate(animMultiplier, 'swim')
        self.getGeomNode().setP(-89.0)
        if self.isLocal():
            self.useSwimControls()
        self.startBobSwimTask()

    def exitSwim(self):
        self.stop()
        self.playingAnim = 'neutral'
        self.stopBobSwimTask()
        self.getGeomNode().setPosHpr(0, 0, 0, 0, 0, 0)
        if self.isLocal():
            self.useWalkControls()

    def startBobSwimTask(self):
        swimTaskName = self.taskName('swimBobTask')
        taskMgr.remove('swimTask')
        taskMgr.remove(swimTaskName)
        self.getGeomNode().setZ(4.0)
        newTask = Task.loop(
            self.getGeomNode().lerpPosXYZ(0, -3, 3, 1, blendType='easeInOut'),
            self.getGeomNode().lerpPosXYZ(0, -3, 4, 1, blendType='easeInOut')
        )
        taskMgr.add(newTask, swimTaskName)

    def stopBobSwimTask(self):
        swimTaskName = self.taskName('swimBobTask')
        taskMgr.remove(swimTaskName)
        self.getGeomNode().setPos(0, 0, 0)

    def enterTeleportedOut(self, animMultiplier=1, ts=0, callback=None, extraArgs=[]):
        return None

    def exitTeleportedOut(self):
        return None

    def getDiedInterval(self, autoFinishTrack=1):
        sound = loader.loadSfx('phase_5/audio/sfx/ENC_Lose.mp3')
        if hasattr(self, 'uniqueName'):
            trackName = self.uniqueName('died')
        else:
            trackName = 'died'
        ival = Sequence(
            Func(self.sadEyes),
            Func(self.blinkEyes),
            Track(
                (0, ActorInterval(self, 'lose')),
                (2, SoundInterval(sound, node=self)),
                (5.333, self.scaleInterval(1.5, VBase3(0.01, 0.01, 0.01), blendType='easeInOut'))
            ),
            Func(self.detachNode),
            Func(self.setScale, 1, 1, 1),
            Func(self.normalEyes),
            Func(self.blinkEyes),
            name=trackName, autoFinish=autoFinishTrack
        )
        return ival

    def enterDied(self, animMultiplier=1, ts=0, callback=None, extraArgs=[]):
        self.playingAnim = 'lose'
        if self.isLocal():
            autoFinishTrack = 0
        else:
            autoFinishTrack = 1
        if hasattr(self, 'jumpLandAnimFixTask') and self.jumpLandAnimFixTask:
            self.jumpLandAnimFixTask.remove()
            self.jumpLandAnimFixTask = None
        self.track = self.getDiedInterval(autoFinishTrack)
        if callback:
            self.track = Sequence(self.track, Func(callback, *extraArgs), autoFinish=autoFinishTrack)
        self.track.start(ts)

    def exitDied(self):
        if self.track != None:
            self.ignore(self.track.getName())
            self.track.finish()
            self.track = None
        self.show()

    def finishDied(self, callback=None, extraArgs=[]):
        if self.track != None:
            self.ignore(self.track.getName())
            self.track.finish()
            self.track = None
        if hasattr(self, 'animFSM'):
            self.animFSM.request('TeleportedOut')
        if callback:
            callback(*extraArgs)

    def enterSitStart(self, animMultiplier=1, ts=0, callback=None, extraArgs=[]):
        self.playingAnim = 'sit-start'
        if self.isLocal():
            self.track = Sequence(ActorInterval(self, 'sit-start'), Func(self.b_setAnimState, 'Sit', animMultiplier))
        else:
            self.track = Sequence(ActorInterval(self, 'sit-start'))
        self.track.start(ts)

    def exitSitStart(self):
        self.playingAnim = 'neutral'
        if self.track != None:
            self.track.finish()
            self.track = None

    def enterSit(self, animMultiplier=1, ts=0, callback=None, extraArgs=[]):
        self.playingAnim = 'sit'
        self.loop('sit')

    def exitSit(self):
        self.playingAnim = 'neutral'

    def enterJumpIdle(self, animMultiplier=1, ts=0, callback=None, extraArgs=[]):
        self.playingAnim = 'jump-idle'
        self.loop('jump-idle')

    def exitJumpIdle(self):
        self.playingAnim = 'neutral'

    def enterRunningJumpIdle(self, animMultiplier=1, ts=0, callback=None, extraArgs=[]):
        self.playingAnim = 'running-jump-idle'
        self.loop('running-jump-idle')

    def exitRunningJumpIdle(self):
        self.playingAnim = 'neutral'

    def enterPush(self, animMultiplier=1, ts=0, callback=None, extraArgs=[]):
        self.playingAnim = 'push'
        self.track = Sequence(ActorInterval(self, 'push'))
        self.track.loop()

    def exitPush(self):
        self.playingAnim = 'neutral'
        if self.track != None:
            self.track.finish()
            self.track = None

    def getPieces(self, *pieces):
        results = []
        for lodName in self.getLODNames():
            for partName, pieceNames in pieces:
                part = self.getPart(partName, lodName)
                if part:
                    if type(pieceNames) == types.StringType:
                        pieceNames = (pieceNames,)
                    for pieceName in pieceNames:
                        npc = part.findAllMatches('**/%s;+s' % pieceName)
                        for i in range(npc.getNumPaths()):
                            results.append(npc[i])
        return results

    def setPartsAdd(self, parts):
        actorCollection = parts
        for thingIndex in range(0, actorCollection.getNumPaths()):
            thing = actorCollection[thingIndex]
            if thing.getName() not in ('joint_attachMeter', 'joint_nameTag'):
                thing.setAttrib(ColorBlendAttrib.make(ColorBlendAttrib.MAdd))
                thing.setDepthWrite(False)
                self.setBin('fixed', 1)

    def setPartsNormal(self, parts, alpha=0):
        actorCollection = parts
        for thingIndex in range(0, actorCollection.getNumPaths()):
            thing = actorCollection[thingIndex]
            if thing.getName() not in ('joint_attachMeter', 'joint_nameTag'):
                thing.setAttrib(ColorBlendAttrib.make(ColorBlendAttrib.MNone))
                thing.setDepthWrite(True)
                self.setBin('default', 0)
                if alpha:
                    thing.setTransparency(1)
                    thing.setBin('transparent', 0)

loadModels()
compileGlobalAnimList()