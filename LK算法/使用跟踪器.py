import lktrack

imnames = ['bt.003.pgm','bt.002.pgm','bt.001.pgm','bt.000.pgm']

#创建跟踪对象
lkt = lktrack.LKTracker(imnames)

#在第一帧进行检测，跟踪剩下的帧

lkt.detect_points()
lkt.draw()
for i in range(len(imnames)-1):
    lkt.track_points()
    lkt.draw()

