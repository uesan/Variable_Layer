import Scene


class Character:

    def __init__(self, name, age=0, level=0, class_level=None, talent=None, bugi=None):
        self.name = name
        self.change_age(age)
        self.change_level(level)
        self.class_level = {}
        self.change_class_level(class_level)
        self.change_talent(talent)
        self.bugi = []
        self.change_bugi(bugi)
        self.item = {}

    def __str__(self):
        str(self.name)

    def change_item(self, item_name, amount):
        a = {item_name: amount}
        self.item.update(a)
        self.create_changes('item', self.item)

    def change_age(self, age):
        self.age = age
        self.create_changes('age', self.age)

    def change_level(self, level):
        self.level = level
        self.create_changes('level', self.level)

    def change_class_level(self, class_level):
        if class_level:
            self.class_level.update(class_level)
            self.create_changes('class_level', self.class_level)
        else:
            self.create_changes('class_level', None)

    def change_talent(self, talent):
        self.talent = talent
        self.create_changes('talent', self.talent)

    def change_bugi(self, bugi):
        self.bugi.append(bugi)
        self.create_changes('bugi', self.bugi)

    def relate_scene(self):
        Scene.StoryOverView.update_instance_change(self, {})

    def create_changes(self, changed_name, changed_value):
        a = {changed_name: changed_value}
        Scene.StoryOverView.update_instance_change(self, a)