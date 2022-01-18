
class shape:
    def __init__(self,color,type):
        self.color = color
        self.type = type
    
    
class cricle_obj(shape):
    def __init__(self,color,type,radios):
        super().__init__(color,type)
        self.radios = radios
    def _get_perimeter(self):
        return self.radios * 3.14 * 2
    
    def _get_area(self):
        return 3.14 * self.radios**2
    
    def print_info(self):
        print("object information:")
        print("\ttype : {0}\n\tcircle perimeter : {1}\n\tcircle area : {2}\n\n".format(self.type,self._get_perimeter(),self._get_area()))

    def __del__(self):
        print("Object ",self.type," deleted ")
    
    

class square(shape):
    def __init__(self,color,type,side):
        super().__init__(color,type)
        self.__side = side
    
    @property
    def side(self):
        return self.__side
    
    @side.setter
    def side(self, side):
        if side <= 0 :
            print("side tall must be bigger than 0")
        else:
            self.__side = side
    
    def _get_perimeter(self):
        return self.side * 4
    
    def _get_area(self):
        return self.side**2
    
    def print_info(self):
        print("object information:")
        print("\ttype : {0}\n\tsquare perimeter : {1}\n\tsquare area : {2}\n\n".format(self.type,self._get_perimeter(),self._get_area()))

    def __del__(self):
        print("Object ",self.type," deleted ")

c1 = cricle_obj("red","circle",2)
c1.print_info()
s1 = square("blue","square",5)
s1.print_info()

s1.side = 0 #change the side value to 0 will print not valied to change it
s1.side = 3
print("\nprint squuare info after changing squrae side's tall")
s1.print_info()