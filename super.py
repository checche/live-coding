Root.default.set(2)
Clock.bpm = 160

def my_dur(values: list[float]):
  return [v * 4 for v in values]

d1 >> play("x ", sample=4)

d2 >> play(" -o-", sample=8)

d1.stop()
d2.stop()


p1 >> pluck([4,4 ,5, 4, 2, 4], dur=[1/2,1,1/2, 1/2,1/2,1])

p1.stop()

p2 >> blip([0,0 ,1, 2,  0, 2, 4, 4], dur=[1/2,1,1/2, 3/2,1/2, 3/2,1/2, 2])

p3 >> pads([0, 0, 0, 1, 2], dur=[1/2,1/2,1/2, 1/2, 2])

p5 >> pads([1,1,0,1,2, 4, 3, 2, 1], dur=[1/2,1,1/2, 1, 1, 1, 1, 1, 1])

p5 >> pads([1,1,0,1,2, 4, 3, 2, 1], dur=my_dur([1/8,1/4,1/8, 1/4, 1/4, 1/4, 1/4, 1/4, 1/4]))
