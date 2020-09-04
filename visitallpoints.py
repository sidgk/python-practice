class Solution:
    def minTimeToVisitAllPoints(self, points):
        size=len(points)
        total_t=0
        for i in range(size-1):
            x=abs(points[i][0]-points[i+1][0])
            y=abs(points[i][1]-points[i+1][1])
            total_t+=max(x,y)
        return total_t
