#over raiding
class animal:
    def sound(self):
        return "generic animal sound"
class dog(animal):
    def sound(self):
        return "woof"
class cat(animal):
    def sound(self):
        return "meow"
a = dog()
b = cat()
print(a.sound())
print(b.sound())
        #method OR in python occurs when  a sub class provides for a specific implmentation
# for a method that is already defined in its superclass this allows the superclass to customize or extent the behavior of the inheritance method

