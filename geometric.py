import numpy as np
import cv2


class Line(object):
    def __init__(self,src, dest,img,points):
        #create a line
        for i in xrange(dest+1):
          cv2.line(img,(i,src),(i,src),(255,255,255),10)
          points.append([i,src])
        print 'Points: '+str(points)
        cv2.imshow('img',img)
        print 'Line 1 drawn'

    def scanner(self,points,img):
        for i in xrange(len(points)):
            x  = points[i][0]
            y = points[i][1]
            #coloring the line to black again
            cv2.line(img,(x,y),(x,y),(0,0,0),10)

        #printing the next line
        for i in xrange(len(points)):
          #Updating points coordinates
          points[i][1] = y+1
          cv2.line(img,(i,y+1),(i,y+1),(255,255,255),10)
          print 'New Line: '+str(i)+' '+str(y+1)

        cv2.imshow('img',img)
        print 'Updated Points: '+str(points)

class Square(object):
    '''This class construct a square from a given center_point and length'''
    def __init__(self, length, center_point, img):
        top_points = []
        bottom_points = []
        left_points = []
        right_points = []

        square_points = {} #This dict will contain a left, right, top and bottom points
        #---------------------------------
        x_top = center_point[0]-length/2.0
        y_top = center_point[1] - length/2.0

        x_bottom = x_top
        y_bottom = y_top+length
        top_points.append([x_top,y_top])
        bottom_points.append([x_bottom,y_bottom])

        square_points['bottom_points'] = bottom_points
        square_points['top_points'] = top_points
        print square_points
        #---------------------------------

        #create a square with center in the given center_point and length
        for i in xrange(length):
            new_top = [x_top+i,y_top]
            new_bottom = [x_bottom+i,y_bottom]

            cv2.line(img,(int(x_top+i),int(y_top)),(int(x_top+i),int(y_top)),(255,255,255),10)
            cv2.line(img,(int(x_bottom+i),int(y_bottom)),(int(x_bottom+i),int(y_bottom)),(255,255,255),10)
            square_points['bottom_points']
        cv2.imshow('img',img)
        print 'Square drawn'










