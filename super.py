# Settings
Root.default.set("D")
Scale.default = Scale.major
Clock.bpm = 60

I   = PGroup(0, 2, 4)
II  = PGroup(1, 3, 5)
III = PGroup(2, 4,-1)
IV  = PGroup(3, 5, 0)
V   = PGroup(4,-1, 1)
VI  = PGroup(5, 0, 2)
VII = PGroup(-1,1, 3)

I7   = PGroup(I).concat(6)
II7  = PGroup(II).concat(7)
III7 = PGroup(III).concat(8)
IV7  = PGroup(IV).concat(9)
V7   = PGroup(V).concat(10)
VI7  = PGroup(VI).concat(11)
VII7 = PGroup(VII).concat(12)


ch = var([IV7, III7, VI7, VI7], 4)
c1 >> piano(ch, dur=4)

b0 >> bass(P[1,3,4,5,6,3,4,5] - 1, dur=2, oct=4, sample=1, amp=0.9)

b0.stop()

b1 >> bass(P[1,3,4,5,6,5,4,5] - 1, dur=[2, 2, 4], oct=4, sample=1, amp=0.9)

b1.stop()

be >> bell[P[4,5,7,1], dur=PDur(3,8)]

d0 >> play("#", dur=16)
d1 >> play("x ", sample=4)
d2 >> play(" -", sample=4)
d2 >> play("( o)- {-* [---]}", sample=8)

p0 >> piano(P[1,3,5] - 1, dur=1/4, amp=1.3, pan=-1)

p1 >> piano(P[3, 5, 7, 10, 9, 8, 7, 8] - 1, dur=1, amp=1.3, pan=1)

p2 >> piano(P[10, 9, 8, 7, 6], dur=[1/2, 1/4, 1/4, 1/4, 3/4])

p0.stop()
p1.stop()
p2.stop()

d1 >> play(P["Hello kobe univ! We are Pablo :)"] & P["(Xo)--[----]"], sample=[1,2])

d1.stop()

d_all.stop()


super_melody = [
    [4,4 ,5, 4, 2, 4] * 2,
    [0,0 ,1, 2,  0, 2, 4, 4],
    [0, 0, 0, 1, 2] * 2,
    [1,1,0,1,2, 4, 3, 2, 1],
]
super_durations = [
    [1/2,1,1/2, 1/2,1/2,1] * 2,
    [1/2,1,1/2, 3/2,1/2, 3/2,1/2, 2],
    [1/2,1/2,1/2, 1/2, 2] * 2,
    [1/2,1,1/2, 1, 1, 1, 1, 1, 1],
]

print(sum(super_melody, []))

p0 >> pluck(sum(super_melody, []), dur=sum(super_durations, []))

p1 >> pluck([4,4 ,5, 4, 2, 4]*2, dur=[1/2,1,1/2, 1/2,1/2,1], hpf=linvar([0,4000],[32,0]))
p1 >> blip([0,0 ,1, 2,  0, 2, 4, 4], dur=[1/2,1,1/2, 3/2,1/2, 3/2,1/2, 2])
p1 >> pads([0, 0, 0, 1, 2]*2, dur=[1/2,1/2,1/2, 1/2, 2]*2)
p1 >> pads([1,1,0,1,2, 4, 3, 2, 1], dur=[1/2,1,1/2, 1, 1, 1, 1, 1, 1])
p6 >> pads(P[-10:40], dur=1/50, amp=1).every(3,"reverse")


p1 >> pluck([4,4 ,5, 4, 2, 4], dur=[1/2,1,1/2, 1/2,1/2,1])

p_all.stop()

### mem
print(SynthDefs)

# 01235 01245
for n in P[0,1,2,[3,4],5]:
    print(n)

c = var([0,5,1,4], 4)
b1 >> bass(c, dur=4)

def verse():
    c = var([0,5,1,4], 4)
    b1 >> bass(c, dur=4)
    p1 >> pluck([0,4], dur=1/2)
    d1 >> play("x--x--x-")
    Clock.future(16, chorus)
def chorus():
    b1 >> bass([0,4,5,3], dur=4)
    p1 >> pluck([0,4,7,9], dur=1/4)
    d1 >> play("x-o-")
    Clock.future(16, verse)
verse()

from FoxDot import Chord
print(Chord)
