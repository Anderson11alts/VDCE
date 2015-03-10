__author__ = 'Saturnino Mateus'
from geometric import *

points = []

'''
img =  np.zeros((512,512,3), np.uint8)
line = Line(0,512,img,points)

for i in xrange(500):
    line.scanner(points,img)
    k = cv2.waitKey(33)
    if k==27:    # Esc key to stop
        break
'''

img =  np.zeros((512,512,3), np.uint8)
square = Square(500,(50,50),img)


for i in xrange(500):
    k = cv2.waitKey(33)
    if k==27:    # Esc key to stop
        break