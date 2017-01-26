def solution(P, C):
    maxP = 2*C
    return C if P>maxP else P//2
