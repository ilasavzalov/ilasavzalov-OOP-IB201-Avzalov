class BoundingRectangle:
    def __init__(self):
        self.points = []
    
    def add_point(self, x, y):
        self.points.append((x, y))
    
    def _update_bounds(self):
        if not self.points:
            return None, None, None, None
        
        xs = [p[0] for p in self.points]
        ys = [p[1] for p in self.points]
        
        return min(xs), max(xs), min(ys), max(ys)
    
    def left_x(self):
        min_x = (self._update_bounds())[0]
        return min_x
    
    def right_x(self):
        max_x = (self._update_bounds())[1]
        return max_x
    
    def bottom_y(self):
        min_y = (self._update_bounds())[2]
        return min_y
    
    def top_y(self):
        max_y = (self._update_bounds())[3]
        return max_y
    
    def width(self):
        min_x = (self._update_bounds())[0]
        max_x = (self._update_bounds())[1]
        return max_x - min_x
    
    def height(self):
        min_y = (self._update_bounds())[2]
        max_y = (self._update_bounds())[3]
        return max_y - min_y





rect = BoundingRectangle()
rect.add_point(-11, -12)
rect.add_point(13, -14)
rect.add_point(-15, 10)
print(rect.left_x(), rect.right_x())
print(rect.bottom_y(), rect.top_y())
print(rect.width(), rect.height())
print()
rect.add_point(-21, -12)
rect.add_point(13, -14)
rect.add_point(-15, 36)
print(rect.width(), rect.height())
print(rect.left_x(), rect.right_x())
print(rect.bottom_y(), rect.top_y())
print()
rect.add_point(-21, 78)
rect.add_point(13, -14)
rect.add_point(-55, 36)
print(rect.bottom_y(), rect.top_y())
print(rect.width(), rect.height())
print(rect.left_x(), rect.right_x())
