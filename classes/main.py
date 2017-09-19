# Необходимо реализовать классы животных на ферме:
#
# Коровы, козы, овцы, свиньи;
# Утки, куры, гуси.
# Условия:
#
# Должен быть один базовый класс, который наследуют все остальные животные.
# Базовый класс должен определять общие характеристики и интерфейс.

class Farm_Animal(object):
    def __init__(
            self,
            species,
            resource,
            sound,
    ):
        self.species = species
        self.resource = resource
        self.sound = sound

    def getSpecies(self):
        return self.species

    def getResource(self):
        return self.resource

    def getSound(self):
        return self.sound

    def __str__(self):
        return 'it is a %s' % self.species


class Farm_Animal_Bird(Farm_Animal):
    def __init__(
            self,
            species,
            resource,
            sound,
            canfly,
    ):
        Farm_Animal.__init__(self, species, resource, sound)
        self.canfly = canfly

    def canFly(self):
        if self.canfly:
            return 'it is ready to fly'
        else:
            return 'No fly today'


class Cow(Farm_Animal):
    def __init__(
            self,
            name,
            weight,
            color,
    ):
        Farm_Animal.__init__(self, 'Cow', 'Milk', 'Mooo')
        self.weight = weight
        self.name = name
        self.color = color

    def cowName(self):
        return self.name

    def cowWeight(self):
        return self.weight

    def cowColor(self):
        return '%s is %s color' % (self.name, self.color)


class Goat(Farm_Animal):
    def __init__(
            self,
            name,
            weight,
            color,
            children,
    ):
        Farm_Animal.__init__(self, 'Goat', 'Milk', 'Meee')
        self.weight = weight
        self.name = name
        self.color = color
        self.children = children

    def goatName(self):
        return self.name

    def goatWeight(self):
        return self.weight

    def goatColor(self):
        return '%s is %s color' % (self.name, self.color)

    def goatHowManyChildren(self):
        return '%s has %s children' % (self.name, self.children)


class Sheep(Farm_Animal):
    def __init__(
            self,
            name,
            weight,
            color,
            wool,
    ):
        Farm_Animal.__init__(self, 'Sheep', 'Wool', 'Beee')
        self.weight = weight
        self.name = name
        self.color = color
        self.wool = weight

    def sheepName(self):
        return self.name

    def sheepWeight(self):
        return self.weight

    def sheepColor(self):
        return '%s is %s color' % (self.name, self.color)

    def sheepItHasWool(self):
        if self.wool:
            return '%s has wool' % self.name
        else:
            return '%s already was cropped' % self.name


class Pig(Farm_Animal):
    def __init__(self, name, weight):
        Farm_Animal.__init__(self, 'Pig', 'Meat', 'Oink')
        self.weight = weight
        self.name = name

    def pigName(self):
        return self.name

    def pigWeight(self):
        return self.weight


class Duck(Farm_Animal_Bird):
    def __init__(
            self,
            name,
            sex,
            ready_to_soup,
    ):
        Farm_Animal_Bird.__init__(self, 'Duck', 'Meat', 'Quack', True)
        self.sex = sex
        self.name = name
        self.ready_to_soup = ready_to_soup

    def duckName(self):
        return self.name

    def duckSex(self):
        if self.sex == 'Male':
            return 'It is a drake'
        else:
            return 'It is a female duck'

    def duckReady_to_soup(self):
        if self.ready_to_soup:
            return 'Get ready to meal'
        else:
            return 'Just only couple of day'


class Chicken(Farm_Animal_Bird):
    def __init__(self, name, eggs):
        Farm_Animal_Bird.__init__(self, 'Chicken', 'Egg', 'KoKoKo',
                                  False)
        self.eggs = eggs
        self.name = name

    def chickenName(self):
        return self.name

    def chickenEggs(self):
        return self.eggs


class Goose(Farm_Animal_Bird):
    def __init__(self, name, color):
        Farm_Animal_Bird.__init__(self, 'Goose', 'Meat', 'GaGa', True)
        self.color = color
        self.name = name

    def gooseName(self):
        return self.name

    def gooseColor(self):
        return self.color


Peppa = Pig('Peppa', 300)
print(Peppa.pigName())
print(Peppa.getSound())

Howard = Duck('Howard', 'Male', True)
print(Howard.canFly())
print(Howard.duckReady_to_soup())
print(Howard.duckSex())
