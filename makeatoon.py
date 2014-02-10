from direct.directbase import DirectStart
from pandac.PandaModules import *
from toontown.toonbase import ToontownGlobals
from direct.showbase import DirectObject
from ToontownFD_Engine.toon import Toon
from ToontownFD_Engine.toon import ToonDNA
from toontown.toontowngui import TTDialog
from direct.gui.DirectGui import *
from toontown.toonbase import TTLocalizer
from direct.directnotify import DirectNotifyGlobal
from toontown.toontowngui import TeaserPanel
from toontown.toonbase import UserFunnel
base.disableMouse()

ConfigVariableString('default-model-extension', '.bam').setValue('.bam')

def endGame():
    base.destroy()

background = loader.loadModel('phase_3/models/gui/create_a_toon.bam')
background.reparentTo(render)
background.find('**/sewing_machine*').removeNode()
background.find('**/easel*').removeNode()
background.find('**/drafting_table*').removeNode()
background.find('**/wall_floor*').setColorScale(0,0.5,0.5,1)

buttonGeom = loader.loadModel('phase_3/models/gui/pick_a_toon_gui.bam')
arrowGeom = loader.loadModel('phase_3/models/gui/create_a_toon_gui.bam')

timeMachine = loader.loadModel('phase_14/models/props/TT_TimeMachine.bam')
timeMachine.reparentTo(render)
timeMachine.setPos(0,0,0)
timeMachine.setHpr(-7,0,0)
timeMachine.setScale(0.8)


localAvatar = Toon.Toon()
localAvatar.reparentTo(render)
style = ToonDNA.ToonDNA()
style.makeFromNetString('t\x05\x01\x00\x01\x97\x1b\x8a\x1b\x3a\x1b\x06\x00\x06\x06')
localAvatar.setDNA(style)
localAvatar.setHpr(200,0,0)
localAvatar.enterSitStart()
localAvatar.setPos(-2.5,-4.2,-0.3)

base.camera.setPos(-1.3,-12.5,2)

mickey = loader.loadFont('phase_3/models/fonts/MickeyFont.bam')
impress = loader.loadFont('phase_3/models/fonts/ImpressBT.ttf')  

text = OnscreenText(text = "Pick A Toon To Play", font = mickey,
                    scale = .15, pos = (0,.8,0), shadow = (255,255,255,1),
                    fg = (255,255,0,1))

next = DirectButton(text = 'Quit', geom = (buttonGeom.find('**/QuitBtn_UP'),
                                           buttonGeom.find('**/QuitBtn_RLVR'),
                                           buttonGeom.find('**/QuitBtn_DN')),
                                           frameVisibleScale = (0,0), text_scale= .1,
                                           text_font = impress, text_pos = (0,-.025,0),
                                           pos = (1,0,-0.9), command = endGame)

run()