class Rectangle:

    def __init__(self, width, height) -> None:
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return (self.width * self.height)

    def get_perimeter(self):
        return (2 * self.width + 2 * self.height)

    def get_diagonal(self):
        a = self.width ** 2
        b = self.height ** 2
        c = (a + b) ** 0.5
        return c

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        else:
            picture_string = ""
            for i in range(self.height):
                for j in range(self.width):
                    picture_string += "*"
                picture_string += "\n" 
            return picture_string

    def get_amount_inside(self, shape):
        area_1 = self.get_area()
        area_2 = shape.get_area()

        return int(area_1 / area_2)

    def __str__(self) -> str:
        if self.width == self.height:
            return f"{type(self).__name__}(side={self.width})"
        else:
            return f"{type(self).__name__}(width={self.width}, height={self.height})"


class Square(Rectangle):
    
    def __init__(self, width, height=None) -> None:
        super().__init__(width, height)
        if height is None:
            self.height = width

    def set_height(self, height):
        return super().set_height(height), super().set_width(height)

    def set_width(self, width):
        return super().set_width(width), super().set_height(width)

    def set_side(self, side):
        self.width = side
        self.height = side