class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def scale(self, factor):
        """Multiply both sides by factor. Factor must be positive."""
        if factor <= 0:
            raise ValueError("factor must be positive")
        self.width *= factor
        self.height *= factor
