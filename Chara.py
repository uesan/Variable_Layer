

class Chara:

    def __init__(self,chara_name=None,scene=None):
        self.changed = {}
        self.changed.update(self.change_name(chara_name))
        self.changed.update(self.change_age(20))
        self.changed.update(self.change_power(5))
        self.changed.update(self.change_defence(3))
        scene.append(self)
        self.changed.clear()
        print(self.changed)

    def __str__(self):
        return str(self.name)

    def __repr__(self):
        return repr(self.name)

    def change_name(self,new_name):
        self.name = new_name
        changed = {'name':new_name}
        return changed

    def change_age(self,new_age):
        self.age = new_age
        changed = {'age':new_age}
        return changed

    def change_power(self,new_power):
        self.power = new_power
        changed = {'power':new_power}
        return changed

    def change_defence(self,new_defence):
        self.defence = new_defence
        changed = {'defence':new_defence}
        return changed



