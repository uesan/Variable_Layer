import Scene, StarWars

Scene.StoryOverView.create_time_axis('エピソード4')
Scene.StoryOverView.create_new_scene('強い力を手にいれる')
Luke = StarWars.Character("ルーク", 20)
Anakin = StarWars.Character("アナキン", 45)
Empire = StarWars.Organization("銀河帝国")
Alliance = StarWars.Organization("反乱同盟")
Scene.StoryOverView.create_next_scene('悪の組織と戦うことに')
Scene.StoryOverView.grant_relation_each_other(Luke, '仲間', Alliance)
Scene.StoryOverView.grant_relation_each_other(Luke, '敵', Empire)
Scene.StoryOverView.create_next_scene('悪の組織の基地を１つ破壊')
Scene.StoryOverView.create_next_scene('悪の組織の幹部が実の父だった')
Scene.StoryOverView.grant_relation_each_other(Luke, '親子', Anakin)
Scene.StoryOverView.create_next_scene('父と共に組織のボスを倒す')


Scene.StoryOverView.show_dict(Scene.StoryOverView.that_time_relation(Luke, '強い力を手にいれる'))
Scene.StoryOverView.show_dict(Scene.StoryOverView.that_time_relation(Luke, '悪の組織の基地を１つ破壊'))
Scene.StoryOverView.show_dict(Scene.StoryOverView.current_relation(Luke))

