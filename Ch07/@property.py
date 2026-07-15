

# @property decoraror is used to define a method as property it can be accessed like an attribute 
#benfit:add additional logic when read write or delete attributes
#gives you getter, setter, deleter method
class Rectangle:
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return f"{self.__width:.1f} cm"

    @property
    def height(self):
        return f"{self.__height:.1f} cm"

    @width.setter
    def width(self, new_width):
        if new_width > 0:
            self.__width = new_width
        else:
            print("Width must be greater than 0")

    @height.setter
    def height(self, new_height):
        if new_height > 0:
            self.__height = new_height
        else:
            print("Height must be greater than 0")
            
    @width.deleter
    def width(self):
        del self.__width 
        print(f"width has been deleted.")
    @height.deleter
    def height(self):
        del self.__height 
        print(f"height has been deleted.")


rectangle = Rectangle(3, 4)
rectangle.width = 5
rectangle.height = 7
del rectangle.width
del rectangle.height
