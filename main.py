import Scene,TwoSidedCalculation,Cast

'''

Scene.TimeAxis.create_time_axis('beta')
Scene.TimeAxis.create_scene('1st')
print(Scene.TimeAxis.get_current_time_axis())
Scene.TimeAxis.show_time_axis()

fibonatti = TwoSidedCalculation.TwoSidedCalculation('fibonatti')
fibonatti.plus(5)
Scene.TimeAxis.show_time_axis()
Scene.TimeAxis.create_scene('2nd')
fibonatti.plus(10)
Scene.TimeAxis.show_time_axis()

'''
Scene.StoryOverView.create_time_axis('story1')

Scene.StoryOverView.create_new_scene('1st')
momotaro = Cast.Cast('momotaro')
inu = Cast.Cast('inu')
saru = Cast.Cast('saru')
kiji = Cast.Cast('kiji')

Scene.StoryOverView.grant_relation_each_other(momotaro, 'not お供', inu)
Scene.StoryOverView.grant_relation_each_other(momotaro, 'not お供', saru)
Scene.StoryOverView.grant_relation_each_other(momotaro, 'not お供', kiji)

momotaro.all_change(5,3,"生まれたばかりで感情はわからない")

Scene.StoryOverView.create_next_scene('2nd')
momotaro.all_change(10,6,"鬼を倒して平和を守りたい")
momotaro.change_item('kibidango',15)

Scene.StoryOverView.create_next_scene('3rd')
'''
イベント：犬と桃太郎が出会う。
　　　　：桃太郎から犬にきびだんごを渡す
結　果　：桃太郎と犬は仲間になる
'''
momotaro.change_item('kibidango', 14)
inu.all_change(4, 4, "きびだんご分がんばろう")
Scene.StoryOverView.grant_relation_each_other(momotaro, 'お供', inu)

Scene.StoryOverView.create_next_scene('4th')

momotaro.change_item('kibidango', 13)
saru.all_change(6, 5, "きびだんごうます")
inu.relate_scene()

Scene.StoryOverView.grant_relation_each_other(momotaro, 'お供', saru)

Scene.StoryOverView.show_over_view()
print(Scene.StoryOverView.current_value(momotaro))

print(Scene.StoryOverView.latest_scene())

print(Scene.StoryOverView.related_scene(momotaro))

print(Scene.StoryOverView.related_scene_until(momotaro,'3rd'))

print(Scene.StoryOverView.current_relation(momotaro))
print(Scene.StoryOverView.that_time_relation(momotaro,'3rd'))


