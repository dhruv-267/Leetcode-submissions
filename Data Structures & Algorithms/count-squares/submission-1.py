class CountSquares:

    def __init__(self):
        self.counts = collections.defaultdict(int) #imp : initialises all dicts with 0
        self.pts = []

    def add(self, point: List[int]) -> None:
        self.counts[tuple(point)]+=1
        self.pts.append(point)

    def count(self, point: List[int]) -> int:
        px, py = point
        res = 0
        for x, y in self.pts:
            if abs(px-x) != abs(py-y) or px==x or py==y:
                continue
            else:
                res+=self.counts[(x,py)] * self.counts[(px,y)]
        return res

        
