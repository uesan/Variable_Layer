import Scene

class TwoSidedCalculation:

    def __init__(self,name):
        self.name = name
        self.result = 0
        self.count = 0

    def plus(self,number):
        self.result = self.result+number
        self.count += 1
        self.show_result()
        self.create_changes()

    def create_changes(self):
        a = {'result':self.result, 'count':self.count}
        Scene.StoryOverView.update_instance_change(self.name, a)

    def show_result(self):
        print(self.result)