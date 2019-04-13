import Scene


class Character:

    def __init__(self, name, age=0):
        self.name = name
        self.change_age(age)

    def __str__(self):
        str(self.name)

    def change_age(self, age):
        self.age = age
        self.create_changes('age', self.age)


    def relate_scene(self):
        Scene.StoryOverView.update_instance_change(self, {})

    def create_changes(self, changed_name, changed_value):
        a = {changed_name: changed_value}
        Scene.StoryOverView.update_instance_change(self, a)


class Organization:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        str(self.name)

    def relate_scene(self):
        Scene.StoryOverView.update_instance_change(self, {})

    def create_changes(self, changed_name, changed_value):
        a = {changed_name: changed_value}
        Scene.StoryOverView.update_instance_change(self, a)