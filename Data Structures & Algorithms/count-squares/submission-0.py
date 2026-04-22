class CountSquares:

    def __init__(self):
        self.ptsmap = collections.defaultdict(int)
        self.ptsarr = []

    def add(self, point: List[int]) -> None:
        self.ptsmap[tuple(point)] +=1
        self.ptsarr.append(point)

    def count(self, point: List[int]) -> int:
        px , py = point
        res = 0
        for x, y in self.ptsarr:
            if abs(px-x)!=abs(py-y) or px == x or py == y:
                continue
            else:
                res+= self.ptsmap[(x,py)]*self.ptsmap[(px,y)]
        return res
        
