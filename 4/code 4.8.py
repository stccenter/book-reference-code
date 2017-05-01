>>> bIntersect = False
>>> def intersect(line1,line2):
        for i in len(line1.lineSegments):
            for j in len(line2.lineSegments):
                if (line1.lineSegments[i].segIntersect(line2.lineSegments[j])):
                    bIntersect = True
                    break
