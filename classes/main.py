# Необходимо реализовать классы животных на ферме:
#
# Коровы, козы, овцы, свиньи;
# Утки, куры, гуси.
# Условия:
#
# Должен быть один базовый класс, который наследуют все остальные животные.
# Базовый класс должен определять общие характеристики и интерфейс.

class FarmAnimal(object):
    def __init__(
            self,
            species,
            resource,
            sound,
    ):
        self.species = species
        self.resource = resource
        self.sound = sound

    def get_species(self):
        return self.species

    def get_resource(self):
        return self.resource

    def get_sound(self):
        return self.sound

    def __str__(self):
        return 'it is a %s' % self.species


class FarmAnimalBird(FarmAnimal):
    def __init__(
            self,
            species,
            resource,
            sound,
            canfly,
    ):
        super().__init__(species, resource, sound)
        self.canfly = canfly

    def can_fly(self):
        return self.canfly and 'it is ready to fly' or 'No fly today'


class Cow(FarmAnimal):
    def __init__(
            self,
            name,
            weight,
            color,
    ):
        super().__init__('Cow', 'Milk', 'Mooo')
        self.weight = weight
        self.name = name
        self.color = color

    def cow_name(self):
        return self.name

    def cow_weight(self):
        return self.weight

    def cow_color(self):
        return '%s is %s color' % (self.name, self.color)


class Goat(FarmAnimal):
    def __init__(
            self,
            name,
            weight,
            color,
            children,
    ):
        super().__init__('Goat', 'Milk', 'Meee')
        self.weight = weight
        self.name = name
        self.color = color
        self.children = children

    def goat_name(self):
        return self.name

    def goat_weight(self):
        return self.weight

    def goat_color(self):
        return '%s is %s color' % (self.name, self.color)

    def goat_how_many_children(self):
        return '%s has %s children' % (self.name, self.children)


class Sheep(FarmAnimal):
    def __init__(
            self,
            name,
            weight,
            color,
            wool,
    ):
        super().__init__('Sheep', 'Wool', 'Beee')
        self.weight = weight
        self.name = name
        self.color = color
        self.wool = weight

    def sheep_name(self):
        return self.name

    def sheep_weight(self):
        return self.weight

    def sheep_color(self):
        return '%s is %s color' % (self.name, self.color)

    def sheep_it_has_wool(self):
        return self.wool and '%s has wool' % self.name or '%s already was cropped' % self.name

class Pig(FarmAnimal):
    def __init__(self, name, weight):
        super().__init__('Pig', 'Meat', 'Oink')
        self.weight = weight
        self.name = name

    def pig_name(self):
        return self.name

    def pig_weight(self):
        return self.weight


class Duck(FarmAnimalBird):
    def __init__(
            self,
            name,
            sex,
            ready_to_soup,
    ):
        super().__init__('Duck', 'Meat', 'Quack', True)
        self.sex = sex
        self.name = name
        self.ready_to_soup = ready_to_soup

    def duck_name(self):
        return self.name

    def duck_sex(self):
        if self.sex == 'Male':
            return 'It is a drake'
        else:
            return 'It is a female duck'

    def duck_ready_to_soup(self):
        if self.ready_to_soup:
            return 'Get ready to meal'
        else:
            return 'Just only couple of day'


class Chicken(FarmAnimalBird):
    def __init__(self, name, eggs):
        super().__init__('Chicken', 'Egg', 'KoKoKo',False)
        self.eggs = eggs
        self.name = name

    def chicken_name(self):
        return self.name

    def chicken_eggs(self):
        return self.eggs


class Goose(FarmAnimalBird):
    def __init__(self, name, color):
        super().__init__('Goose', 'Meat', 'GaGa', True)
        self.color = color
        self.name = name

    def goose_name(self):
        return self.name

    def goose_color(self):
        return self.color


Peppa = Pig('Peppa', 300)
print(Peppa.pig_name())
print(Peppa.get_sound())

Howard = Duck('Howard', 'Male', True)
print(Howard.can_fly())
print(Howard.duck_ready_to_soup())
print(Howard.duck_sex())
