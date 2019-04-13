import Scene


class Cast:
    def __init__(self, name):
        self.name = name
        self.item = {}

    def __str__(self):
        str(self.name)

    def all_change(self, power, defence, emortion):
        self.change_power(power)
        self.change_defence(defence)
        self.change_emortion(emortion)

    def change_item(self, item_name,amount):
        a = {item_name: amount}
        self.item.update(a)
        self.create_changes('item', self.item)

    def change_power(self, power):
        self.power = power
        self.create_changes('power', self.power)

    def change_defence(self, defence):
        self.defence = defence
        self.create_changes('defence', self.defence)

    def change_emortion(self, emotion):
        self.emotion = emotion
        self.create_changes('emotion', self.emotion)

    def relate_scene(self):
        Scene.StoryOverView.update_instance_change(self, {})

    def create_changes(self, changed_name, changed_value):
        a = {changed_name: changed_value}
        Scene.StoryOverView.update_instance_change(self, a)
