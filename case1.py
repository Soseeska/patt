from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def __init__(self, color, type, id, material): #абстрактный метод так как количество переменных может быть разным
        self.color = color
        self.type = type
        self.id = id
        self.material = material

    def draw(self):
        print("Представим, что фигура нарисована " + self.color)

    def materials(self):
        print("Представим, что фигура состоит из " + self.material)

    @abstractmethod
    def square(main):#абстрактный метод для вычисления метода
        pass

    @abstractmethod
    def visible(self):#абстрактный метод для прозрачности
        pass

class Curqile(Shape): #описываем класс круга
    def __init__(self, color, type, id, material,r,visCoef):
        self.color = color
        self.type = type
        self.id = id
        self.material = material
        self.r = r
        self.visCoef = visCoef
    def square(self): #формула площади завязана на радиусе
        sqr=self.r**2*3.14
        return (sqr)
    def visible(self):
        print("Фигура будет нарисована с прозрачностью "+str(self.visCoef))


class Rectangle(Shape): #описываем класс прямоугольника
    def __init__(self, color, type, id, material,a,b):
        self.color = color
        self.type = type
        self.id = id
        self.material = material
        self.a=a
        self.b=b
    def square(self):
        sqr=self.a*self.b
        return (sqr)
    def visible(self):
        print("Фигура непрозрачна")



cirql=Curqile("красным","krug",12,"песка",12,13) #повызываем разное для круга
cirql.draw()
cirql.materials()
cirql.visible()
a=cirql.square()
print(str(a))

print('\n')

cirql=Rectangle("синим","krug",12,"стекла",5,10) #повызываем разное для квадрата
cirql.draw()
cirql.materials()
cirql.visible()
a=cirql.square()
print(str(a))


