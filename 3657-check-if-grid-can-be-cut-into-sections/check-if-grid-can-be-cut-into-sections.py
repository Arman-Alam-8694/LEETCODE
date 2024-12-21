class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        rectangles.sort(key=lambda x: x[1])
        ycnt = 0
        yy = 0
        py = -1
        ymax = float("-inf")
        ymin = float("inf")
        prevy = rectangles[0][1]
     
        for idx in rectangles:
            if prevy != idx[1]:

                if py != -1 and py < ymax:
                  
                    ycnt += ymax - py
                    if ymin >= py:
                        yy += 1

                if py == -1:
                  
                    ycnt += ymax
                    if ymin >= py:
                        yy += 1
                py = max(py, ymax)
                prevy = idx[1]
                ymin = prevy

            ymax = max(ymax, idx[3])
            ymin = min(ymin, idx[1])
       
        if ymax > py:
            ycnt += ymax - py
            if ymin >= py:
                yy += 1

   
        if ycnt == ymax and yy >= 3:
            return True
        rectangles.sort(key=lambda x: x[0])
     
        xcnt = 0
        xmax = float("-inf")
        xmin = float("inf")
        px = -1
        xx = 0
        prevx = rectangles[0][0]
        for idx in rectangles:
            if prevx != idx[0]:
               
                if px != -1 and px < xmax:
                    xcnt += xmax - px
                    if xmin >= px:
                        xx += 1
                if px == -1:
                    xcnt += xmax
                    if xmin >= px:
                        xx += 1

                prevx = idx[0]
                px = max(px, xmax)
               
                xmin = prevx
            xmax = max(xmax, idx[2])
            xmin = min(xmin, idx[0])

       
        if xmax > px:
            xcnt += xmax - px
            if xmin >= px:
                xx += 1

    
        if xcnt == xmax and xx >= 3:
            return True
        return False
