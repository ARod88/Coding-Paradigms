class Podracer:
    def __init__(self, max_speed, condition, price):
        self.max_speed = max_speed
        self.condition = condition
        self.price = price

# repair method 

    def repair(self):
        self.condition = "repaired"

class AnakinsPod(Podracer): 
    def __init__(self, max_speed, condition, price):
        super().__init__(max_speed, condition, price)
#boost method
    def boost(self):
        self.max_speed *= 2

class SebulbasPod(Podracer):
     def __init__(self, max_speed, condition, price):
        super().__init__(max_speed, condition, price)

     def flame_jet(self, other_podracer):
        other_podracer.condition = "trashed"

podracer1 = Podracer(500, "perfect", 2000)
print(podracer1.condition)
podracer1.repair()
print(podracer1.condition)

anakins_pod = AnakinsPod(800, "repaired", 2500)
print(anakins_pod.max_speed)
anakins_pod.boost()
print(anakins_pod.max_speed)

sebulbas_pod = SebulbasPod(900, "trashed", 3500)
other_podracer = Podracer(800, "perfect", 2000)
print(other_podracer.condition)
sebulbas_pod.flame_jet(other_podracer)
print(other_podracer.condition)

"""How does this solution demonstrate the four pillars of OOP? (It may not demonstrate all of them, describe only those that apply)
Encapsulation- the classes encapsulate the instances
Abstraction-
Inheritance- Anakins and Sebulbas Pod inherit the attributes of the Podracer which is the parent class
Polymorphism- the subclasses can use the instances that are added on the subclasses
Would it have been easier to implement a solution to this problem using a different coding style? Why or why not?
no because it deals with objects
How in particular did Object Oriented Programming assist in the solving of this problem?
It assisted by modeling the podracer objects. it organized it by encapsulating date and behaviors and allowed it to inherit other behaviors in other classes."""