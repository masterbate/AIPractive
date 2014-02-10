from sys import argv
from direct.directbase import DirectStart
from direct.task import Task
from direct.actor.Actor import Actor
from direct.gui.DirectGui import *
from pandac.PandaModules import *
from direct.interval.IntervalGlobal import *
from direct.showbase.InputStateGlobal import inputState
from direct.controls.GravityWalker import GravityWalker
base.disableMouse()
 
legsAnimDict = {'right-hand-start': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_legs_right-hand-start.bam', 'firehose': 'phase_5/models/char/tt_a_chr_dgs_shorts_legs_firehose.bam', 'rotateL-putt': 'phase_6/models/char/tt_a_chr_dgs_shorts_legs_rotateL-putt.bam', 'slip-forward': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_slip-forward.bam', 'catch-eatnrun': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_eatnrun.bam', 'tickle': 'phase_5/models/char/tt_a_chr_dgs_shorts_legs_tickle.bam', 'water-gun': 'phase_5/models/char/tt_a_chr_dgs_shorts_legs_water-gun.bam', 'leverNeutral': 'phase_10/models/char/tt_a_chr_dgs_shorts_legs_leverNeutral.bam', 'swim': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_swim.bam', 'catch-run': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_gamerun.bam', 'sad-neutral': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_sad-neutral.bam', 'pet-loop': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_petloop.bam', 'jump-squat': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_legs_jump-zstart.bam', 'wave': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_legs_wave.bam', 'reel-neutral': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_reelneutral.bam', 'pole-neutral': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_poleneutral.bam', 'bank': 'phase_5.5/models/char/tt_a_chr_dgs_shorts_legs_jellybeanJar.bam', 'scientistGame': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_scientistGame.bam', 'right-hand': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_legs_right-hand.bam', 'lookloop-putt': 'phase_6/models/char/tt_a_chr_dgs_shorts_legs_lookloop-putt.bam', 'victory': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_legs_victory-dance.bam', 'lose': 'phase_5/models/char/tt_a_chr_dgs_shorts_legs_lose.bam', 'cringe': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_legs_cringe.bam', 'right': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_right.bam', 'headdown-putt': 'phase_6/models/char/tt_a_chr_dgs_shorts_legs_headdown-putt.bam', 'conked': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_legs_conked.bam', 'jump': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_legs_jump.bam', 'into-putt': 'phase_6/models/char/tt_a_chr_dgs_shorts_legs_into-putt.bam', 'fish-end': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_fishEND.bam', 'running-jump-land': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_legs_leap_zend.bam', 'shrug': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_legs_shrug.bam', 'sprinkle-dust': 'phase_5/models/char/tt_a_chr_dgs_shorts_legs_sprinkle-dust.bam', 'hold-bottle': 'phase_5/models/char/tt_a_chr_dgs_shorts_legs_hold-bottle.bam', 'takePhone': 'phase_5.5/models/char/tt_a_chr_dgs_shorts_legs_takePhone.bam', 'melt': 'phase_5/models/char/tt_a_chr_dgs_shorts_legs_melt.bam', 'pet-start': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_petin.bam', 'look-putt': 'phase_6/models/char/tt_a_chr_dgs_shorts_legs_look-putt.bam', 'loop-putt': 'phase_6/models/char/tt_a_chr_dgs_shorts_legs_loop-putt.bam', 'good-putt': 'phase_6/models/char/tt_a_chr_dgs_shorts_legs_good-putt.bam', 'juggle': 'phase_5/models/char/tt_a_chr_dgs_shorts_legs_juggle.bam', 'run': 'phase_3/models/char/tt_a_chr_dgs_shorts_legs_run.bam', 'pushbutton': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_legs_press-button.bam', 'sidestep-right': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_legs_jump-back-right.bam', 'water': 'phase_5.5/models/char/tt_a_chr_dgs_shorts_legs_water.bam', 'right-point-start': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_legs_right-point-start.bam', 'bad-putt': 'phase_6/models/char/tt_a_chr_dgs_shorts_legs_bad-putt.bam', 'struggle': 'phase_5/models/char/tt_a_chr_dgs_shorts_legs_struggle.bam', 'running-jump': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_legs_running-jump.bam', 'callPet': 'phase_5.5/models/char/tt_a_chr_dgs_shorts_legs_callPet.bam', 'throw': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_legs_pie-throw.bam', 'catch-eatneutral': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_eat_neutral.bam', 'tug-o-war': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_tug-o-war.bam', 'bow': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_bow.bam', 'swing': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_swing.bam', 'climb': 'phase_5/models/char/tt_a_chr_dgs_shorts_legs_climb.bam', 'scientistWork': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_scientistWork.bam', 'think': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_think.bam', 'catch-intro-throw': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_gameThrow.bam', 'walk': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_legs_walk.bam', 'down': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_down.bam', 'pole': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_pole.bam', 'periscope': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_legs_periscope.bam', 'duck': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_legs_duck.bam', 'curtsy': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_curtsy.bam', 'jump-land': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_legs_jump-zend.bam', 'loop-dig': 'phase_5.5/models/char/tt_a_chr_dgs_shorts_legs_loop_dig.bam', 'angry': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_legs_angry.bam', 'bored': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_bored.bam', 'swing-putt': 'phase_6/models/char/tt_a_chr_dgs_shorts_legs_swing-putt.bam', 'pet-end': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_petend.bam', 'spit': 'phase_5/models/char/tt_a_chr_dgs_shorts_legs_spit.bam', 'right-point': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_legs_right-point.bam', 'start-dig': 'phase_5.5/models/char/tt_a_chr_dgs_shorts_legs_into_dig.bam', 'castlong': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_castlong.bam', 'confused': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_confused.bam', 'neutral': 'phase_3/models/char/tt_a_chr_dgs_shorts_legs_neutral.bam', 'jump-idle': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_legs_jump-zhang.bam', 'reel': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_reel.bam', 'slip-backward': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_slip-backward.bam', 'sound': 'phase_5/models/char/tt_a_chr_dgs_shorts_legs_shout.bam', 'sidestep-left': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_legs_sidestep-left.bam', 'up': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_up.bam', 'fish-again': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_fishAGAIN.bam', 'cast': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_cast.bam', 'phoneBack': 'phase_5.5/models/char/tt_a_chr_dgs_shorts_legs_phoneBack.bam', 'phoneNeutral': 'phase_5.5/models/char/tt_a_chr_dgs_shorts_legs_phoneNeutral.bam', 'scientistJealous': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_scientistJealous.bam', 'battlecast': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_fish.bam', 'sit-start': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_intoSit.bam', 'toss': 'phase_5/models/char/tt_a_chr_dgs_shorts_legs_toss.bam', 'happy-dance': 'phase_5/models/char/tt_a_chr_dgs_shorts_legs_happy-dance.bam', 'running-jump-squat': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_legs_leap_zstart.bam', 'teleport': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_legs_teleport.bam', 'sit': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_sit.bam', 'sad-walk': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_losewalk.bam', 'give-props-start': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_legs_give-props-start.bam', 'book': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_legs_book.bam', 'running-jump-idle': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_legs_leap_zhang.bam', 'scientistEmcee': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_scientistEmcee.bam', 'leverPull': 'phase_10/models/char/tt_a_chr_dgs_shorts_legs_leverPull.bam', 'tutorial-neutral': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_legs_tutorial-neutral.bam', 'badloop-putt': 'phase_6/models/char/tt_a_chr_dgs_shorts_legs_badloop-putt.bam', 'give-props': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_legs_give-props.bam', 'hold-magnet': 'phase_5/models/char/tt_a_chr_dgs_shorts_legs_hold-magnet.bam', 'hypnotize': 'phase_5/models/char/tt_a_chr_dgs_shorts_legs_hypnotize.bam', 'left-point': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_legs_left-point.bam', 'leverReach': 'phase_10/models/char/tt_a_chr_dgs_shorts_legs_leverReach.bam', 'feedPet': 'phase_5.5/models/char/tt_a_chr_dgs_shorts_legs_feedPet.bam', 'reel-H': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_reelH.bam', 'applause': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_applause.bam', 'smooch': 'phase_5/models/char/tt_a_chr_dgs_shorts_legs_smooch.bam', 'rotateR-putt': 'phase_6/models/char/tt_a_chr_dgs_shorts_legs_rotateR-putt.bam', 'fish-neutral': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_fishneutral.bam', 'push': 'phase_9/models/char/tt_a_chr_dgs_shorts_legs_push.bam', 'catch-neutral': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_gameneutral.bam', 'left': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_left.bam'}
 
torsoAnimDict = {'right-hand-start': 'phase_3.5/models/char/tt_a_chr_dgl_skirt_torso_right-hand-start.bam', 'firehose': 'phase_5/models/char/tt_a_chr_dgl_skirt_torso_firehose.bam', 'rotateL-putt': 'phase_6/models/char/tt_a_chr_dgl_skirt_torso_rotateL-putt.bam', 'slip-forward': 'phase_4/models/char/tt_a_chr_dgl_skirt_torso_slip-forward.bam', 'catch-eatnrun': 'phase_4/models/char/tt_a_chr_dgl_skirt_torso_eatnrun.bam', 'tickle': 'phase_5/models/char/tt_a_chr_dgl_skirt_torso_tickle.bam', 'water-gun': 'phase_5/models/char/tt_a_chr_dgl_skirt_torso_water-gun.bam', 'leverNeutral': 'phase_10/models/char/tt_a_chr_dgl_skirt_torso_leverNeutral.bam', 'swim': 'phase_4/models/char/tt_a_chr_dgl_skirt_torso_swim.bam', 'catch-run': 'phase_4/models/char/tt_a_chr_dgl_skirt_torso_gamerun.bam', 'sad-neutral': 'phase_4/models/char/tt_a_chr_dgl_skirt_torso_sad-neutral.bam', 'pet-loop': 'phase_4/models/char/tt_a_chr_dgl_skirt_torso_petloop.bam', 'jump-squat': 'phase_3.5/models/char/tt_a_chr_dgl_skirt_torso_jump-zstart.bam', 'wave': 'phase_3.5/models/char/tt_a_chr_dgl_skirt_torso_wave.bam', 'reel-neutral': 'phase_4/models/char/tt_a_chr_dgl_skirt_torso_reelneutral.bam', 'pole-neutral': 'phase_4/models/char/tt_a_chr_dgl_skirt_torso_poleneutral.bam', 'bank': 'phase_5.5/models/char/tt_a_chr_dgl_skirt_torso_jellybeanJar.bam', 'scientistGame': 'phase_4/models/char/tt_a_chr_dgl_skirt_torso_scientistGame.bam', 'right-hand': 'phase_3.5/models/char/tt_a_chr_dgl_skirt_torso_right-hand.bam', 'lookloop-putt': 'phase_6/models/char/tt_a_chr_dgl_skirt_torso_lookloop-putt.bam', 'victory': 'phase_3.5/models/char/tt_a_chr_dgl_skirt_torso_victory-dance.bam', 'lose': 'phase_5/models/char/tt_a_chr_dgl_skirt_torso_lose.bam', 'cringe': 'phase_3.5/models/char/tt_a_chr_dgl_skirt_torso_cringe.bam', 'right': 'phase_4/models/char/tt_a_chr_dgl_skirt_torso_right.bam', 'headdown-putt': 'phase_6/models/char/tt_a_chr_dgl_skirt_torso_headdown-putt.bam', 'conked': 'phase_3.5/models/char/tt_a_chr_dgl_skirt_torso_conked.bam', 'jump': 'phase_3.5/models/char/tt_a_chr_dgl_skirt_torso_jump.bam', 'into-putt': 'phase_6/models/char/tt_a_chr_dgl_skirt_torso_into-putt.bam', 'fish-end': 'phase_4/models/char/tt_a_chr_dgl_skirt_torso_fishEND.bam', 'running-jump-land': 'phase_3.5/models/char/tt_a_chr_dgl_skirt_torso_leap_zend.bam', 'shrug': 'phase_3.5/models/char/tt_a_chr_dgl_skirt_torso_shrug.bam', 'sprinkle-dust': 'phase_5/models/char/tt_a_chr_dgl_skirt_torso_sprinkle-dust.bam', 'hold-bottle': 'phase_5/models/char/tt_a_chr_dgl_skirt_torso_hold-bottle.bam', 'takePhone': 'phase_5.5/models/char/tt_a_chr_dgl_skirt_torso_takePhone.bam', 'melt': 'phase_5/models/char/tt_a_chr_dgl_skirt_torso_melt.bam', 'pet-start': 'phase_4/models/char/tt_a_chr_dgl_skirt_torso_petin.bam', 'look-putt': 'phase_6/models/char/tt_a_chr_dgl_skirt_torso_look-putt.bam', 'loop-putt': 'phase_6/models/char/tt_a_chr_dgl_skirt_torso_loop-putt.bam', 'good-putt': 'phase_6/models/char/tt_a_chr_dgl_skirt_torso_good-putt.bam', 'juggle': 'phase_5/models/char/tt_a_chr_dgl_skirt_torso_juggle.bam', 'run': 'phase_3/models/char/tt_a_chr_dgl_skirt_torso_run.bam', 'pushbutton': 'phase_3.5/models/char/tt_a_chr_dgl_skirt_torso_press-button.bam', 'sidestep-right': 'phase_3.5/models/char/tt_a_chr_dgl_skirt_torso_jump-back-right.bam', 'water': 'phase_5.5/models/char/tt_a_chr_dgl_skirt_torso_water.bam', 'right-point-start': 'phase_3.5/models/char/tt_a_chr_dgl_skirt_torso_right-point-start.bam', 'bad-putt': 'phase_6/models/char/tt_a_chr_dgl_skirt_torso_bad-putt.bam', 'struggle': 'phase_5/models/char/tt_a_chr_dgl_skirt_torso_struggle.bam', 'running-jump': 'phase_3.5/models/char/tt_a_chr_dgl_skirt_torso_running-jump.bam', 'callPet': 'phase_5.5/models/char/tt_a_chr_dgl_skirt_torso_callPet.bam', 'throw': 'phase_3.5/models/char/tt_a_chr_dgl_skirt_torso_pie-throw.bam', 'catch-eatneutral': 'phase_4/models/char/tt_a_chr_dgl_skirt_torso_eat_neutral.bam', 'tug-o-war': 'phase_4/models/char/tt_a_chr_dgl_skirt_torso_tug-o-war.bam', 'bow': 'phase_4/models/char/tt_a_chr_dgl_skirt_torso_bow.bam', 'swing': 'phase_4/models/char/tt_a_chr_dgl_skirt_torso_swing.bam', 'climb': 'phase_5/models/char/tt_a_chr_dgl_skirt_torso_climb.bam', 'scientistWork': 'phase_4/models/char/tt_a_chr_dgl_skirt_torso_scientistWork.bam', 'think': 'phase_4/models/char/tt_a_chr_dgl_skirt_torso_think.bam', 'catch-intro-throw': 'phase_4/models/char/tt_a_chr_dgl_skirt_torso_gameThrow.bam', 'walk': 'phase_3.5/models/char/tt_a_chr_dgl_skirt_torso_walk.bam', 'down': 'phase_4/models/char/tt_a_chr_dgl_skirt_torso_down.bam', 'pole': 'phase_4/models/char/tt_a_chr_dgl_skirt_torso_pole.bam', 'periscope': 'phase_3.5/models/char/tt_a_chr_dgl_skirt_torso_periscope.bam', 'duck': 'phase_3.5/models/char/tt_a_chr_dgl_skirt_torso_duck.bam', 'curtsy': 'phase_4/models/char/tt_a_chr_dgl_skirt_torso_curtsy.bam', 'jump-land': 'phase_3.5/models/char/tt_a_chr_dgl_skirt_torso_jump-zend.bam', 'loop-dig': 'phase_5.5/models/char/tt_a_chr_dgl_skirt_torso_loop_dig.bam', 'angry': 'phase_3.5/models/char/tt_a_chr_dgl_skirt_torso_angry.bam', 'bored': 'phase_4/models/char/tt_a_chr_dgl_skirt_torso_bored.bam', 'swing-putt': 'phase_6/models/char/tt_a_chr_dgl_skirt_torso_swing-putt.bam', 'pet-end': 'phase_4/models/char/tt_a_chr_dgl_skirt_torso_petend.bam', 'spit': 'phase_5/models/char/tt_a_chr_dgl_skirt_torso_spit.bam', 'right-point': 'phase_3.5/models/char/tt_a_chr_dgl_skirt_torso_right-point.bam', 'start-dig': 'phase_5.5/models/char/tt_a_chr_dgl_skirt_torso_into_dig.bam', 'castlong': 'phase_4/models/char/tt_a_chr_dgl_skirt_torso_castlong.bam', 'confused': 'phase_4/models/char/tt_a_chr_dgl_skirt_torso_confused.bam', 'neutral': 'phase_3/models/char/tt_a_chr_dgl_skirt_torso_neutral.bam', 'jump-idle': 'phase_3.5/models/char/tt_a_chr_dgl_skirt_torso_jump-zhang.bam', 'reel': 'phase_4/models/char/tt_a_chr_dgl_skirt_torso_reel.bam', 'slip-backward': 'phase_4/models/char/tt_a_chr_dgl_skirt_torso_slip-backward.bam', 'sound': 'phase_5/models/char/tt_a_chr_dgl_skirt_torso_shout.bam', 'sidestep-left': 'phase_3.5/models/char/tt_a_chr_dgl_skirt_torso_sidestep-left.bam', 'up': 'phase_4/models/char/tt_a_chr_dgl_skirt_torso_up.bam', 'fish-again': 'phase_4/models/char/tt_a_chr_dgl_skirt_torso_fishAGAIN.bam', 'cast': 'phase_4/models/char/tt_a_chr_dgl_skirt_torso_cast.bam', 'phoneBack': 'phase_5.5/models/char/tt_a_chr_dgl_skirt_torso_phoneBack.bam', 'phoneNeutral': 'phase_5.5/models/char/tt_a_chr_dgl_skirt_torso_phoneNeutral.bam', 'scientistJealous': 'phase_4/models/char/tt_a_chr_dgl_skirt_torso_scientistJealous.bam', 'battlecast': 'phase_4/models/char/tt_a_chr_dgl_skirt_torso_fish.bam', 'sit-start': 'phase_4/models/char/tt_a_chr_dgl_skirt_torso_intoSit.bam', 'toss': 'phase_5/models/char/tt_a_chr_dgl_skirt_torso_toss.bam', 'happy-dance': 'phase_5/models/char/tt_a_chr_dgl_skirt_torso_happy-dance.bam', 'running-jump-squat': 'phase_3.5/models/char/tt_a_chr_dgl_skirt_torso_leap_zstart.bam', 'teleport': 'phase_3.5/models/char/tt_a_chr_dgl_skirt_torso_teleport.bam', 'sit': 'phase_4/models/char/tt_a_chr_dgl_skirt_torso_sit.bam', 'sad-walk': 'phase_4/models/char/tt_a_chr_dgl_skirt_torso_losewalk.bam', 'give-props-start': 'phase_3.5/models/char/tt_a_chr_dgl_skirt_torso_give-props-start.bam', 'book': 'phase_3.5/models/char/tt_a_chr_dgl_skirt_torso_book.bam', 'running-jump-idle': 'phase_3.5/models/char/tt_a_chr_dgl_skirt_torso_leap_zhang.bam', 'scientistEmcee': 'phase_4/models/char/tt_a_chr_dgl_skirt_torso_scientistEmcee.bam', 'leverPull': 'phase_10/models/char/tt_a_chr_dgl_skirt_torso_leverPull.bam', 'tutorial-neutral': 'phase_3.5/models/char/tt_a_chr_dgl_skirt_torso_tutorial-neutral.bam', 'badloop-putt': 'phase_6/models/char/tt_a_chr_dgl_skirt_torso_badloop-putt.bam', 'give-props': 'phase_3.5/models/char/tt_a_chr_dgl_skirt_torso_give-props.bam', 'hold-magnet': 'phase_5/models/char/tt_a_chr_dgl_skirt_torso_hold-magnet.bam', 'hypnotize': 'phase_5/models/char/tt_a_chr_dgl_skirt_torso_hypnotize.bam', 'left-point': 'phase_3.5/models/char/tt_a_chr_dgl_skirt_torso_left-point.bam', 'leverReach': 'phase_10/models/char/tt_a_chr_dgl_skirt_torso_leverReach.bam', 'feedPet': 'phase_5.5/models/char/tt_a_chr_dgl_skirt_torso_feedPet.bam', 'reel-H': 'phase_4/models/char/tt_a_chr_dgl_skirt_torso_reelH.bam', 'applause': 'phase_4/models/char/tt_a_chr_dgl_skirt_torso_applause.bam', 'smooch': 'phase_5/models/char/tt_a_chr_dgl_skirt_torso_smooch.bam', 'rotateR-putt': 'phase_6/models/char/tt_a_chr_dgl_skirt_torso_rotateR-putt.bam', 'fish-neutral': 'phase_4/models/char/tt_a_chr_dgl_skirt_torso_fishneutral.bam', 'push': 'phase_9/models/char/tt_a_chr_dgl_skirt_torso_push.bam', 'catch-neutral': 'phase_4/models/char/tt_a_chr_dgl_skirt_torso_gameneutral.bam', 'left': 'phase_4/models/char/tt_a_chr_dgl_skirt_torso_left.bam'}
 
catHead = loader.loadModel('phase_3/models/char/cat-heads-1000.bam')
otherParts = catHead.findAllMatches('**/*long*')
for partNum in range(0, otherParts.getNumPaths()):
    otherParts.getPath(partNum).removeNode()
ntrlMuzzle = catHead.find('**/*muzzle*neutral')
otherParts = catHead.findAllMatches('**/*muzzle*')
for partNum in range(0, otherParts.getNumPaths()):
    part = otherParts.getPath(partNum)
    if part != ntrlMuzzle:
        otherParts.getPath(partNum).removeNode()
catTorso = loader.loadModel('phase_3/models/char/tt_a_chr_dgl_skirt_torso_1000.bam')
catLegs  = loader.loadModel('phase_3/models/char/tt_a_chr_dgs_shorts_legs_1000.bam')
otherParts = catLegs.findAllMatches('**/boots*')+catLegs.findAllMatches('**/shoes')
for partNum in range(0, otherParts.getNumPaths()):
    otherParts.getPath(partNum).removeNode()
 
catBody = Actor({'head':catHead, 'torso':catTorso, 'legs':catLegs},
                {'torso':torsoAnimDict, 'legs':legsAnimDict})
catBody.attach('head', 'torso', 'def_head')
catBody.attach('torso', 'legs', 'joint_hips')
 
gloves = catBody.findAllMatches('**/hands')
ears = catBody.findAllMatches('**/*ears*')
head = catBody.findAllMatches('**/head-*')
sleeves = catBody.findAllMatches('**/sleeves')
shirt = catBody.findAllMatches('**/torso-top')
skirt = catBody.findAllMatches('**/torso-bot')
neck = catBody.findAllMatches('**/neck')
arms = catBody.findAllMatches('**/arms')
legs = catBody.findAllMatches('**/legs')
feet = catBody.findAllMatches('**/feet')
 
bodyNodes = []
bodyNodes += [gloves]
bodyNodes += [head, ears]
bodyNodes += [sleeves, shirt, skirt]
bodyNodes += [neck, arms, legs, feet]
bodyNodes[0].setColor(0.4, 0.4, 0.4, 1)
bodyNodes[1].setColor(0.242188, 0.742188, 0.515625, 1)
bodyNodes[2].setColor(0.242188, 0.742188, 0.515625, 1)
bodyNodes[3].setColor(0.242188, 0.742188, 0.515625, 1)
bodyNodes[4].setColor(0.242188, 0.742188, 0.515625, 1)
bodyNodes[5].setColor(0.433594, 0.90625, 0.835938, 1)
bodyNodes[6].setColor(1, 1, 1, 1)
bodyNodes[7].setColor(1, 1, 1, 1)
bodyNodes[8].setColor(0.7, 0.7, 0.8, 1)
bodyNodes[9].setColor(0.7, 0.7, 0.8, 1)
 
topTex = loader.loadTexture('phase_4/maps/tt_t_chr_avt_shirt_marathon1.jpg')
botTex = loader.loadTexture('phase_4/maps/tt_t_chr_avt_shorts_fishing1.jpg')
sleeveTex = loader.loadTexture('phase_4/maps/tt_t_chr_avt_shirtSleeve_fishing1.jpg')
 
bodyNodes[3].setTexture(sleeveTex, 1)
bodyNodes[4].setTexture(topTex, 1)
bodyNodes[5].setTexture(botTex, 1)
 
catBody.reparentTo(render)
 
geom = catBody.getGeomNode()
geom.getChild(0).setSx(0.730000019073)
geom.getChild(0).setSz(0.730000019073)
 
offset = 3.2375
 
base.camera.reparentTo(catBody)
base.camera.setPos(0, -10.0 - offset, offset)
wallBitmask = BitMask32(1)
floorBitmask = BitMask32(2)
base.cTrav = CollisionTraverser()
def getAirborneHeight():
    return offset + 0.025000000000000001
walkControls = GravityWalker(legacyLifter=True)
walkControls.setWallBitMask(wallBitmask)
walkControls.setFloorBitMask(floorBitmask)
walkControls.setWalkSpeed(16.0, 24.0, 8.0, 80.0)
walkControls.initializeCollisions(base.cTrav, catBody, floorOffset=0.025, reach=4.0)
#base.cTrav.showCollisions(render)
walkControls.setAirborneHeightFunc(getAirborneHeight)
walkControls.enableAvatarControls()
catBody.physControls = walkControls
 
def setWatchKey(key, input, keyMapName):
    def watchKey(active=True):
        if active == True:
            inputState.set(input, True)
            keyMap[keyMapName] = 1
        else:
            inputState.set(input, False)
            keyMap[keyMapName] = 0
    base.accept(key, watchKey, [True])
    base.accept(key+'-up', watchKey, [False])
 
keyMap = {'left':0, 'right':0, 'forward':0, 'backward':0, 'control':0}
 
setWatchKey('arrow_up', 'forward', 'forward')
setWatchKey('control-arrow_up', 'forward', 'forward')
setWatchKey('alt-arrow_up', 'forward', 'forward')
setWatchKey('shift-arrow_up', 'forward', 'forward')
setWatchKey('arrow_down', 'reverse', 'backward')
setWatchKey('control-arrow_down', 'reverse', 'backward')
setWatchKey('alt-arrow_down', 'reverse', 'backward')
setWatchKey('shift-arrow_down', 'reverse', 'backward')
setWatchKey('arrow_left', 'turnLeft', 'left')
setWatchKey('control-arrow_left', 'turnLeft', 'left')
setWatchKey('alt-arrow_left', 'turnLeft', 'left')
setWatchKey('shift-arrow_left', 'turnLeft', 'left')
setWatchKey('arrow_right', 'turnRight', 'right')
setWatchKey('control-arrow_right', 'turnRight', 'right')
setWatchKey('alt-arrow_right', 'turnRight', 'right')
setWatchKey('shift-arrow_right', 'turnRight', 'right')
setWatchKey('control', 'jump', 'control')
 
movingNeutral, movingForward = (False, False)
movingRotation, movingBackward = (False, False)
movingJumping = False
 
def setMovementAnimation(loopName, playRate=1.0):
    global movingNeutral
    global movingForward
    global movingRotation
    global movingBackward
    global movingJumping
    if 'jump' in loopName:
        movingJumping = True
        movingForward = False
        movingNeutral = False
        movingRotation = False
        movingBackward = False
    elif loopName == 'run':
        movingJumping = False
        movingForward = True
        movingNeutral = False
        movingRotation = False
        movingBackward = False
    elif loopName == 'walk':
        movingJumping = False
        movingForward = False
        movingNeutral = False
        if playRate == -1.0:
            movingBackward = True
            movingRotation = False
        else:
            movingBackward = False
            movingRotation = True
    elif loopName == 'neutral':
        movingJumping = False
        movingForward = False
        movingNeutral = True
        movingRotation = False
        movingBackward = False
    else:
        movingJumping = False
        movingForward = False
        movingNeutral = False
        movingRotation = False
        movingBackward = False
    ActorInterval(catBody, loopName, playRate=playRate).loop()
 
def handleMovement(task):
    global movingNeutral, movingForward
    global movingRotation, movingBackward, movingJumping
    if keyMap['control'] == 1:
        if keyMap['forward'] or keyMap['backward'] or keyMap['left'] or keyMap['right']:
            if movingJumping == False:
                if catBody.physControls.isAirborne:
                    setMovementAnimation('running-jump-idle')
                else:
                    if keyMap['forward']:
                        if movingForward == False:
                            setMovementAnimation('run')
                    elif keyMap['backward']:
                        if movingBackward == False:
                            setMovementAnimation('walk', playRate=-1.0)
                    elif keyMap['left'] or keyMap['right']:
                        if movingRotation == False:
                            setMovementAnimation('walk')
            else:
                if not catBody.physControls.isAirborne:
                    if keyMap['forward']:
                        if movingForward == False:
                            setMovementAnimation('run')
                    elif keyMap['backward']:
                        if movingBackward == False:
                            setMovementAnimation('walk', playRate=-1.0)
                    elif keyMap['left'] or keyMap['right']:
                        if movingRotation == False:
                            setMovementAnimation('walk')
        else:
            if movingJumping == False:
                if catBody.physControls.isAirborne:
                    setMovementAnimation('jump-idle')
                else:
                    if movingNeutral == False:
                        setMovementAnimation('neutral')
            else:
                if not catBody.physControls.isAirborne:
                    if movingNeutral == False:
                        setMovementAnimation('neutral')
    elif keyMap['forward'] == 1:
        if movingForward == False:
            if not catBody.physControls.isAirborne:
                setMovementAnimation('run')
    elif keyMap['backward'] == 1:
        if movingBackward == False:
            if not catBody.physControls.isAirborne:
                setMovementAnimation('walk', playRate=-1.0)
    elif keyMap['left'] or keyMap['right']:
        if movingRotation == False:
            if not catBody.physControls.isAirborne:
                setMovementAnimation('walk')
    else:
        if not catBody.physControls.isAirborne:
            if movingNeutral == False:
                setMovementAnimation('neutral')
    return Task.cont
 
base.taskMgr.add(handleMovement, 'controlManager')
 
def collisionsOn():
    catBody.physControls.setCollisionsActive(True)
    catBody.physControls.isAirborne = True
def collisionsOff():
    catBody.physControls.setCollisionsActive(False)
    catBody.physControls.isAirborne = True
def toggleCollisions():
    if catBody.physControls.getCollisionsActive():
        catBody.physControls.setCollisionsActive(False)
        catBody.physControls.isAirborne = True
    else:
        catBody.physControls.setCollisionsActive(True)
        catBody.physControls.isAirborne = True
base.accept('f1', toggleCollisions)
catBody.collisionsOn = collisionsOn
catBody.collisionsOff = collisionsOff
catBody.toggleCollisions = toggleCollisions
 
localAvatar = catBody
base.localAvatar = localAvatar

loadHub = True
if len(argv) > 1:
    filepath = argv[1]
    if '.' in filepath:
        try:
            execfile(filepath)
            loadHub = False
        except Exception, e:
            loadHub = False
            print e
    else:
        loadHub = True
 
if loadHub == True:
 
    onScreenDebug.add('Loaded CogHQ', 'Default (Cog Nation - Train Station)')
 
    Hub = loader.loadModel('phase_14/models/cogHQ/CN_TrainStation.bam')
    HubNode = render.attachNewNode('Hub')
    Hub.reparentTo(render)
    Hub.setScale(2)
    Hub.setPos(0,0,-2)
    Hub.setHpr(0,0,0)

else:
 
    onScreenDebug.add('Loaded CogHQ', argv[1])
 
localAvatar.physControls.placeOnFloor()
 
onScreenDebug.enabled = True
 
def updateOnScreenDebug(task):
 
    onScreenDebug.add('Avatar Position', localAvatar.getPos())
    onScreenDebug.add('Avatar Angle', localAvatar.getHpr())
 
    return Task.cont
 
base.taskMgr.add(updateOnScreenDebug, 'UpdateOSD')

from direct.directbase import DirectStart
 
from direct.actor.Actor import Actor
from pandac.PandaModules import *
from direct.task import Task
import math
from math import pi, sin, cos
from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from direct.interval.IntervalGlobal import *
from pandac.PandaModules import Point3
 
#Hub

bgMusic1 = base.loader.loadSfx("phase_14/audio/bgm/Courtyard.wav")
bgMusic1.setLoop(True)
bgMusic1.play()

tunnel = loader.loadModel('phase_6/models/cogHQ/Cog_Tunnel.bam')
tunnel.reparentTo(render)
tunnel.setScale(0.8)
tunnel.setPos(124,4.3,2)
tunnel.setHpr(90,0,0)
tunnel.find('**/pCube39').hide()
tunnel.find('**/pCube32').hide()
tunnel.find('**/pCube31').hide()
tunnel.find('**/pCube47').hide()
tunnel.find('**/pCube33').hide()
tunnel.find('**/pCube51').hide()
tunnel.find('**/cog').hide()

train_1 = loader.loadModel('phase_10/models/cogHQ/CashBotLocomotive.bam')
train_1.reparentTo(render)
train_1.setScale(0.2)
train_1.setPos(-9,79,-2)
train_1.setHpr(90,0,0)

train_cart_1 = loader.loadModel('phase_10/models/cogHQ/CashBotBoxCar.bam')
train_cart_1.reparentTo(train_1)
train_cart_1.setX(80)

train_cart_2 = loader.loadModel('phase_10/models/cogHQ/CashBotBoxCar.bam')
train_cart_2.reparentTo(train_1)
train_cart_2.setX(160)

train_cart_3 = loader.loadModel('phase_10/models/cogHQ/CashBotBoxCar.bam')
train_cart_3.reparentTo(train_1)
train_cart_3.setX(240)

stage_1 = train_1.posInterval(5, Point3(-9, 0, -2))
stage_2 = train_1.posInterval(3, Point3(-9, -10, -2))
stage_3 = train_1.posInterval(7, Point3(-9, -10, -2))
stage_4 = train_1.posInterval(3, Point3(-9, -20, -2))
stage_5 = train_1.posInterval(30, Point3(-9,-900, -2))

mySequence = Sequence()
mySequence.append(stage_1)
mySequence.append(stage_2)
mySequence.append(stage_3)
mySequence.append(stage_4)
mySequence.append(stage_5)
mySequence.start()
mySequence.loop()

botcam1 = Actor("phase_9/models/char/BotCam-zero.bam",{"botcamneutral":"phase_9/models/char/BotCam-neutral.bam"})
botcam1.reparentTo(render)
botcam1.loop("botcamneutral")
botcam1.setPos(1,-31,14)
botcam1.setHpr(88,0,0)
botcam1.setScale(1.4)

botcam2 = Actor("phase_9/models/char/BotCam-zero.bam",{"botcamneutral":"phase_9/models/char/BotCam-neutral.bam"})
botcam2.reparentTo(render)
botcam2.loop("botcamneutral")
botcam2.setPos(1,30,14)
botcam2.setHpr(88,0,0)
botcam2.setScale(1.4)

tbooth = loader.loadModel('phase_14/models/props/tbooth.bam')
tbooth.reparentTo(render)
tbooth.setPos(86,-38,2)
tbooth.setHpr(88,0,0)
tbooth.setScale(1.4)
#Use for later : Tboot rotating
#tbooth.find('**/smallgear').hprInterval(5, Point3(0, 360, 0)).loop()

boxes = loader.loadModel('phase_14/models/props/CN_boxes.bam')
boxes.reparentTo(render)
boxes.setPos(106,31,5)
boxes.setHpr(0,0,0)
boxes.setScale(1)

boxes2 = loader.loadModel('phase_14/models/props/CN_boxes.bam')
boxes2.reparentTo(render)
boxes2.setPos(106,-27,5)
boxes2.setHpr(0,0,0)
boxes2.setScale(1)

cbhq = loader.loadModel('phase_10/models/cogHQ/CashBotShippingStation.bam')
cbhq.reparentTo(render)
cbhq.setPos(580,-280,25)
cbhq.setHpr(840,0,0)
cbhq.setScale(1)

timeMachine = loader.loadModel('phase_14/models/props/TT_TimeMachine.bam')
timeMachine.reparentTo(render)
timeMachine.setPos(0,0,0)
timeMachine.setScale(1)

def CollCheck(neededx1, neededx2, neededz1, neededz2, neededy1, neededy2, gotox, gotoy, gotoz, rotx, roty, rotz,zone):
    x = int(base.localAvatar.getX())
    y = int(base.localAvatar.getY())
    z = int(base.localAvatar.getZ())
    
    if x >= neededx1 and x <= neededx2 and z <= neededz1 and z >= neededz2 and y <= neededy1 and y >=neededy2 :
        print "Land Collisions: \'localAvatar\' has collided with \'a teleport\'"
        base.localAvatar.collisionsOff()
        base.localAvatar.setPosHpr(gotox,gotoy,gotoz,rotx,roty,rotz)
        base.localAvatar.collisionsOn()

def waitTillCheckCollisions():
  seq = Sequence()
  seq.append(Func(CollCheck, 120, 132, 2, 0, 15, 4, 208, -104, 2, 208, 0,0, 2000))
  seq.start()
  seq.loop()

waitTillCheckCollisions()

run()