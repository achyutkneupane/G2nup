#compressor
comp = ['','','']
comp[0] = ['COMP','Sense','Attack','Level']
comp[1] = ['RackComp','Range','Tone','Level']
comp[2] = ['M Comp','Range','Tone','Level']

#efx
efx = ['AutoWah','Resonance','Booster','Tremelo','RingMod','SlowATTCK','Octave','PedalVox','PedalCry']
for i in 0,1:
    efx[i] = [efx[i],'Sense','Reso','Level']
efx[2] = [efx[2],'Range','Tone','Level']
efx[3] = [efx[3],'Depth','Rate','Wave']
efx[4] = [efx[4],'Freq','Tone','Bal']
efx[5] = [efx[5],'Time','Curve','Level']
efx[6] = [efx[6],'Tone','OctLV','DrvLV']
for i in 7,8:
    efx[i] = [efx[i],'Freq','DryMX','Level']

#znr
znr = ['ZNR','NoiseGate','DirtyGate']
for i in range(len(znr)): 
    znr[i] = [znr[i],'THRSH']

#drv
drv = ['FD Combo','VX Combo','US Blues','BG Crunch','HW Stack','MS Crunch','MS Drive','PV Drive','DZ Drive','BG Drive','OverDrive','T Scream','Governor','Dist +','Dist 1','Squeak','FuzzSmile','GreatMuff','MetalWRLD','HotBox','Z Clean','Z Wild','Z MP1','Z Bottom','Z Dream','Z Scream','Z Neos','Lead','ExtremeDS','']
for i in range(len(drv)-1): 
    drv[i] = [drv[i],'Gain','Tone','Level']
drv[len(drv)-1] = ['Aco. Sim','Top','Body','Level']

#mod
mod = ['Chorus','VintageCE','StereoCho','Ensemble','Phaser','Flanger','DynaFLNGR','Vibrato','Step','Cry','Detune','PitchSHFT','MotoPitch','HPS','PDL Pitch','ComboFLTR','Air','Delay','TapeEcho','ModDelay','DynaDelay']
for i in 0,2,3:
    mod[i] = [mod[i],'Depth','Rate','Mix']
mod[1] = [mod[1],'Comp','Rate','Mix']
mod[4] = [mod[4],'Rate','Color','Level']
for i in 5,8:
    mod[i] = [mod[i],'Depth','Rate','Reso']
mod[6] = [mod[6],'Depth','Rate','Sense']
mod[7] = [mod[7],'Depth','Rate','Bal']
mod[9] = [mod[9],'Range','Reso','Sense']
mod[10] = [mod[10],'Cent','PreD','Mix']
for i in 11,12:
    mod[i] = [mod[i],'Shift','Tone','Bal']
mod[13] = [mod[13],'Scale','Key','Mix']
mod[14] = [mod[14],'Color','Tone','Bend']
mod[15] = [mod[15],'Freq','Reso','Mix']
mod[16] = [mod[16],'Size','Tone','Mix']
for i in 17,18,19:
    mod[i] = [mod[i],'Time','F.B','Mix']
mod[20] = [mod[20],'Time','Sense','Mix']


#dly
dly = ['Delay','Echo','AnalogDLY','PingPongD','ReverseDL']
for i in 0,1,2,3:
    dly[i] = [dly[i],'Time','F.B','Mix']
dly[4] = [dly[4],'Time','F.B','Bal']

#rev
rev = ['Hall','Room','Spring','Arena','TiledRoom','EarlyRef','MultiTapD']
for i in 0,1,2,3,4:
    rev[i] = [rev[i],'Decay','Tone','Mix']
rev[5] = [rev[5],'Decay','Shape','Mix']
rev[6] = [rev[6],'Time','PATTRN','Mix']