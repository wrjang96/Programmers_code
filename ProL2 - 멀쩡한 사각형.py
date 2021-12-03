from math import *
def gcd(x,y):
    while y:
        x,y = y, x%y
    return x

def solution(w,h):
    answer= 0
    if w ==1 or h ==1 :
        return 0
    elif w == h:
        return w*h - w
    else:
        tmpgcd = gcd(w,h)
        return w * h - (w+ h - tmpgcd)
    return answer
