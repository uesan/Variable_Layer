import copy, json


class StoryOverView:
    """
    時間軸クラス
    あるインスタンスの変数の変更をデータ構造(dict)で時系列順に保存しておき、呼び出すことができる
    次の場面が作られるまでは今の場面に変更を更新していく

    overViewの中に入るもの
    ・時間（場面の集合）
    ・インスタンス生成時の場面と変数の数
    ・同じ離散時間にある場面の集合たち

    sceneの中に入るもの
    ・関係

    インスタンスにはname変数(str)が必要

    :param over_view
    dict{
        (str)場面の関係性:{
            (str)場面名:{
                (str)'previous_scene':(list)この場面の一つ前の場面名たち -> [場面名A,場面名B,...]
                (str)'same_time_scene':(list)この場面と同じ時間の場面名たち -> [場面名A,場面名B,...]
                (str)'next_scene':(list)この場面の次の場面名たち -> [場面名A,場面名B,...]
            }
        (str)キャラの関係性:{
            (str)場面名:{
                (str)インスタンス名A(from):{
                    インスタンス名B(to):'関係性'
                }
            }
        }
        (str)時間軸の集合:{
            (str)時間軸名:{
                (str)場面名:{
                    (str)'場面の変化':(dict)場面の変化{
                        (str)クラス名:{
                            (str)インスタンス名:(dict)インスタンスの変更{
                                (str)変数名:(?)変数の変更
                            }
                        }
                    }
                }
        }
    }

    ---工事中---
    overView{
        time_axis_name(str):scene_list(list)[
            scene{(str)scene_name:(dict)scene_changes{
                (str)instance_name:(dict)instance_changes{
                    (str)val_name:(?)val_changes
                }
            }
        ]
    }

    例
    {
        'quest':[
            {
                'section1':{
                    'takashi':{
                        name:'takashi'
                        age:15
                        power:7
                        defence:5
                    }
                    'kenji':{
                        name:'kenji'
                        age:17
                        power:8
                        defence:6
                    }
                }

                'section2':{
                    'takashi':{
                        age:16
                        power:10
                    }
                    'kenji':{
                        age:18
                        power:12
                    }
                }
            }
        ]
    }
    ---ここまで工事中---

    (str)インスタンスディクト:{
            (str)キャラ名:{
                キャラ制作場面:(str)
                製作時の変数の数:(number)
                }
            }

    :param current_time_axis_name :type str

    """

    over_view = {}
    scenes_context = {}
    relationship = {}
    time_axises = {}
    over_view.update({'scenes_context': scenes_context, 'relationship': relationship, 'time_axises': time_axises})
    instance_dict = {}
    current_time_axis_name = None
    current_scene_name = None

    '''
    setter & getter
    セッター：時間軸と場面
    ゲッター：指定された時間軸、今の時間軸、指定された場面、今の場面、指定された場面の変更、今の場面の変更
    '''

    @classmethod
    def set_time_axis(cls, time_axis_name):
        cls.current_time_axis_name = time_axis_name

    @classmethod
    def set_scene(cls, scene_name):
        cls.current_scene_name = scene_name

    @classmethod
    def get_current_time_axis(cls):
        """

        :return: current_scene_dict:type dict
        """
        return cls.get_time_axis(cls.current_time_axis_name)

    @classmethod
    def get_time_axis(cls, time_axis_name):
        """

        :param time_axis_name:type str

        :return: scene_dict:type dict
        """
        time_axises = cls.over_view.get('time_axises')
        if time_axis_name in time_axises:
            return time_axises.get(time_axis_name)
        print('\'' + time_axis_name + '\' is not found')
        return None

    @classmethod
    def get_scene(cls, received_scene_name):
        """

        :param received_scene_name: :type dict
        :return: scene :type dict
        """
        time_axises = cls.over_view.get('time_axises')
        for time_axis_name, scene_dict in time_axises.items():
            for scene_name in scene_dict:
                if received_scene_name == scene_name:
                    return scene_dict.get(scene_name)
        print('\'' + received_scene_name + '\' is not found in ' + cls.current_time_axis_name)
        return None

    @classmethod
    def get_current_scene(cls):
        """

        :return scene(:type dict) or None
        """
        current_scene_dict = cls.get_current_time_axis()
        for scene_name in current_scene_dict:
            if cls.current_scene_name == scene_name:
                return current_scene_dict.get(scene_name)
        print('\'' + cls.current_scene_name + '\'(current scene) is not found')
        return None

    @classmethod
    def get_scene_changes(cls, scene_name):
        """

        :param scene_name:
        :return: scene_changes :type dict(class_name:{instance_name:{instance_change}})
        """
        scene = cls.get_scene(scene_name)
        scene_changes = scene.get('scene_changes')
        return scene_changes

    @classmethod
    def get_current_scene_changes(cls):
        return cls.get_scene_changes(cls.current_scene_name)

    @classmethod
    def get_scene_context(cls, scene_name):
        scenes_context = cls.over_view.get('scenes_context')
        return scenes_context.get(scene_name)

    @classmethod
    def get_previous_scenes(cls, scene_name):
        scene_context = cls.get_scene_context(scene_name)
        return scene_context.get('previous_scene')

    @classmethod
    def get_next_scenes(cls, scene_name):
        scene_context = cls.get_scene_context(scene_name)
        return scene_context.get('next_scene')

    @classmethod
    def get_same_time_scenes(cls, scene_name):
        scene_context = cls.get_scene_context(scene_name)
        return scene_context.get('same_time_scene')

    @classmethod
    def get_instance_changes_in_scene(cls, instance,scene_name):
        scene_changes = cls.get_scene_changes(scene_name)
        instance_changes = scene_changes.get(instance.__class__.__name__)
        return instance_changes.get(instance.name)

    @classmethod
    def get_scenes_relation(cls, scene_name):
        relationship = cls.over_view.get('relationship')
        return relationship.get(scene_name)

    '''
    createの関数たち
    新たな時間軸や場面を生み出す関数群
    '''

    @classmethod
    def create_time_axis(cls, time_axis_name):
        time_axises = cls.over_view.get('time_axises')
        if time_axis_name in cls.time_axises:
            print("\"" + time_axis_name + "\"(time axis) is already created.")
        scene_dict = {}
        time_axises.update({time_axis_name: scene_dict})
        cls.set_time_axis(time_axis_name)

    @classmethod
    def create_new_scene(cls, scene_name):

        if cls.search_scene_time_axis(scene_name):
            print("\"" + scene_name + "\"(scene) is already created.")
            return False

        scene_dict = cls.get_current_time_axis()
        if cls.current_time_axis_name in cls.over_view.get('time_axises'):
            scene_content = {}
            scene_context = {'previous_scene': [], 'same_time_scene': [], 'next_scene': []}
            scene_content.update({'scene_changes': {}})
            scene_dict.update({scene_name: scene_content})
            scenes_context = cls.over_view.get('scenes_context')
            scenes_context.update({scene_name: scene_context})
            scene_relation = {}
            scenes_relation = cls.over_view.get('relationship')
            scenes_relation.update({scene_name: scene_relation})
            cls.set_scene(scene_name)
            return True
        print('\'' + scene_name + "\' could not created.")
        return False

    @classmethod
    def create_next_scene(cls, scene_name):
        previous_scene_name = cls.current_scene_name
        if cls.create_new_scene(scene_name):
            cls.grant_BaA_context(previous_scene_name, scene_name)
            return True
        return False

    @classmethod
    def create_previous_scene(cls, scene_name):
        next_scene_name = cls.current_scene_name
        if cls.create_new_scene(scene_name):
            cls.grant_BaA_context(scene_name, next_scene_name)
            return True
        return False

    @classmethod
    def create_same_time_scene(cls, scene_name):
        old_scene_name = cls.current_scene_name
        if cls.create_new_scene(scene_name):
            cls.grant_same_time_context(scene_name, old_scene_name)
            return True
        return False

    '''
    場面に時間的な関係を付与する関数群
    '''
    @classmethod
    def grant_BaA_context(cls,before_scene_name,after_scene_name):
        before_scene_context = cls.get_scene_context(before_scene_name)
        (before_scene_context.get('next_scene')).append(after_scene_name)
        after_scene_context = cls.get_scene_context(after_scene_name)
        (after_scene_context.get('previous_scene')).append(before_scene_name)
        """
        before_scene = cls.get_scene(before_scene_name)
        before_scene_next = before_scene.get('next_scene')
        
        time_axis = cls.search_scene(after_scene_name)
        if not time_axis:
            return False

        if time_axis in before_scene_next:
            (before_scene_next.get(time_axis)).append(after_scene_name)
        else:
            before_scene_next.update({time_axis: after_scene_name})

        after_scene = cls.get_scene(after_scene_name)
        after_scene_previous = after_scene.get('previous_scene')

        time_axis = cls.search_scene(before_scene_name)
        if not time_axis:
            return False

        if time_axis in after_scene_previous:
            (after_scene_previous.get(time_axis)).append(before_scene_name)
        else:
            after_scene_previous.update({time_axis: before_scene_name})
        """

    @classmethod
    def grant_same_time_context(cls, a_scene_name, another_scene_name):
        a_scene_context = cls.get_scene_context(a_scene_name)
        (a_scene_context.get('same_time_scene')).append(another_scene_name)
        another_scene_context = cls.get_scene_context(another_scene_name)
        (another_scene_context.get('same_time_scene')).append(a_scene_name)
        """
        a_scene = cls.get_scene(a_scene_name)
        a_scene_same_time = a_scene.get('same_time_scene')

        time_axis = cls.search_scene(a_scene_name)
        if time_axis:
            return False

        if time_axis in a_scene_same_time:
            (a_scene_same_time.get(time_axis)).append(another_scene_name)
        else:
            a_scene_same_time.update({time_axis: another_scene_name})

        another_scene = cls.get_scene(another_scene_name)
        another_scene_same_time = another_scene.get('same_time_scene')

        time_axis = cls.search_scene(another_scene_name)
        if time_axis:
            return False

        if time_axis in another_scene_same_time:
            (another_scene_same_time.get(time_axis)).append(a_scene_name)
        else:
            another_scene_same_time.update({time_axis: a_scene_name})
        """

    @classmethod
    def grant_relation_one_side(cls, from_instance, relation, to_instance):
        """
        関係性を一方向に付与する関数
        :param from_instance:
        :param relation:
        :param to_instance:
        :return:
        """
        scenes_relation = cls.get_scenes_relation(cls.current_scene_name)
        if from_instance.name in scenes_relation:
            instances_relations = scenes_relation.get(from_instance.name)
            instances_relations.update({to_instance.name: relation})
        else:
            instances_relations = ({to_instance.name: relation})
            scenes_relation.update({from_instance.name: instances_relations})

    @classmethod
    def grant_relation_each_other(cls, from_instance, relation, to_instance):
        cls.grant_relation_one_side(from_instance, relation, to_instance)
        cls.grant_relation_one_side(to_instance, relation, from_instance)

    @classmethod
    def search_scene_time_axis(cls, received_scene_name):
        """
        引数の名前がどの時間軸にあるかを返す関数
        :return time_axis (:type string) or False
        """
        for time_axis in cls.over_view.get('time_axises'):
            scene_dict = cls.get_time_axis(time_axis)
            for scene_name in scene_dict:
                if received_scene_name in scene_name:
                    return time_axis
        return False

    @classmethod
    def current_value(cls, instance):

        return cls.decide_value(cls.current_scene_name, instance)

    @classmethod
    def that_time_value(cls, instance, scene_name):
        return cls.decide_value(scene_name, instance)

    @classmethod
    def decide_value(cls, scene_name, instance):
        scene_changes = cls.get_scene_changes(scene_name)
        scene_class_changes = scene_changes.get(instance.__class__.__name__)
        instance_changes = {}
        if instance.name in scene_class_changes:
            instance_changes.update(scene_class_changes.get(instance.name))
        scene_context = cls.get_scene_context(scene_name)
        previous_scene = scene_context.get('previous_scene')
        if not previous_scene:
            return instance_changes
        elif len(previous_scene) == 1:
            previous_changes = cls.decide_value(previous_scene[0], instance)
            current_changes = copy.deepcopy(previous_changes)
            current_changes.update(instance_changes)
            return current_changes
        else:
            """
            for scene_name in previous_scene:
                分岐後の場面に対して変化を参照する。
                分岐したことを知らせた上で、複数の値を返す？
            """
            print("以前の場面が分岐していて一意に値が決まっていません")
            return instance_changes

    @classmethod
    def current_relation(cls, instance):
        return cls.decide_relation(cls.current_scene_name, instance)

    @classmethod
    def that_time_relation(cls, instance, scene_name):
        return cls.decide_relation(scene_name, instance)

    @classmethod
    def decide_relation(cls, scene_name, instance):
        scenes_relation = cls.get_scenes_relation(scene_name)
        scene_instance_relation = {}
        if instance.name in scenes_relation:
            scene_instance_relation.update(scenes_relation.get(instance.name))
        scene_context = cls.get_scene_context(scene_name)
        previous_scene = scene_context.get('previous_scene')
        if not previous_scene:
            return scene_instance_relation
        elif len(previous_scene) == 1:
            previous_relation = cls.decide_relation(previous_scene[0], instance)
            current_relation = copy.deepcopy(previous_relation)
            current_relation.update(scene_instance_relation)
            return current_relation
        else:
            """
    for scene_name in previous_scene:
        分岐後の場面に対して変化を参照する。
        分岐したことを知らせた上で、複数の値を返す？
        """
        print("以前の場面が分岐していて一意に値が決まっていません")
        return scene_instance_relation

    '''
    インスタンスの変更を行う変数
    '''

    @classmethod
    def update_instance_change(cls, instance, instance_value_changes):
        """
        インスタンスが更新された際にその都度更新を場面（レイヤ）に反映させる
        :param instance :type str
        インスタンスの名前が渡される。
        :param instance_value_changes :type dict
        インスタンスの変数の名前と変更がkeyとvalueになっている辞書型の変数
        :return: なし(0 or NULL or NONE?)
        """
        instance_class = instance.__class__.__name__
        current_scene_changes = cls.get_current_scene_changes()
        new_changes = copy.deepcopy(instance_value_changes)
        if instance_class in current_scene_changes:
            if instance.name in current_scene_changes.get(instance_class):
                #print('Update \'' + instance.name + '\' changes in \'' + cls.current_scene_name)
                instance_class_changes = current_scene_changes.get(instance_class)
                instance_changes = instance_class_changes.get(instance.name)
                instance_changes.update(new_changes)
            else:
                #print('Create new \'' + instance.name + '\' changes in \'' + cls.current_scene_name)
                instance_class_changes = current_scene_changes.get(instance_class)
                instance_class_changes.update({instance.name: new_changes})
        else:
            #print('Create new \'' + instance.name + '\' changes in \'' + cls.current_scene_name)
            current_scene_changes.update({instance_class: {instance.name: new_changes}})

    @classmethod
    def history_of_object(cls, instance, scene_name):
        a_list = cls.related_scene_until(instance, scene_name)
        history = {}
        for related_scene in a_list:
            scene_changes = cls.get_scene_changes(related_scene)
            instance_changes = scene_changes.get(instance.__class__.__name__)
            history.update({related_scene: instance_changes.get(instance.name)})
        return history

    searched_scene_list = []

    @classmethod
    def related_scene(cls, instance):
        """
        あるインスタンスがどの場面に関わっているのかを示す関数
        :param instance:
        :return:
        """
        oldest_scenes_name = cls.oldest_scene()
        a_list = []
        for scene_name in oldest_scenes_name:
            a_list.extend(cls.__find_relate_scene__(instance, scene_name))
        cls.searched_scene_list.clear()
        return a_list

    @classmethod
    def related_scene_until(cls, instance, scene_name):
        cls.next_scene_regard_searched(scene_name)
        same_time_scenes = cls.get_same_time_scenes(scene_name)
        for same_time_scene in same_time_scenes:
            cls.next_scene_regard_searched(same_time_scene)
        return cls.related_scene(instance)

    @classmethod
    def next_scene_regard_searched(cls, scene_name):
        next_scenes = cls.get_next_scenes(scene_name)
        cls.searched_scene_list.extend(next_scenes)
        for next_scene in next_scenes:
            cls.next_scene_regard_searched(next_scene)

    @classmethod
    def __find_relate_scene__(cls, instance, scene_name):
        cls.searched_scene_list.append(scene_name)
        scene_changes = cls.get_scene_changes(scene_name)
        print(scene_changes)
        a_list = []
        if instance.name in scene_changes.get(instance.__class__.__name__):
            a_list.append(scene_name)

        for old_scene_name in cls.get_previous_scenes(scene_name):
            if old_scene_name not in cls.searched_scene_list:
                a_list.extend(cls.__find_relate_scene__(instance, old_scene_name))

        for same_time_scene_name in cls.get_same_time_scenes(scene_name):
            if same_time_scene_name not in cls.searched_scene_list:
                a_list.extend(cls.__find_relate_scene__(instance, same_time_scene_name))

        for next_scene_name in cls.get_next_scenes(scene_name):
            if next_scene_name not in cls.searched_scene_list:
                a_list.extend(cls.__find_relate_scene__(instance, next_scene_name))

        return a_list

    @classmethod
    def latest_scene(cls):
        """
        一番最後にあたる場面名のリストを表示する。孤立した場面も表示される。
        :return: latest :type list
        """
        scenes_context = cls.over_view.get('scenes_context')
        latest = []
        for scene_name, scene_context in scenes_context.items():
            if not scene_context.get('next_scene'):
                latest.append(scene_name)
        return latest

    @classmethod
    def oldest_scene(cls):
        """
        一番最初にあたる場面名のリストを表示する。孤立した場面も表示される。

        :return: oldest :type list
        """
        scenes_context = cls.over_view.get('scenes_context')
        oldest = []
        for scene_name, scene_context in scenes_context.items():
            if not scene_context.get('previous_scene'):
                oldest.append(scene_name)
        return oldest


    """
    show関数
    時間軸や、場面などの内容を確認するために標準出力に出力するための関数
    """
    @classmethod
    def show_over_view(cls):
        """
        クラス変数である時間軸の束を出力する関数。
        import json が必要
        :return: なし
        """
        cls.show_dict(cls.over_view)

    @classmethod
    def show_scenes_context(cls):
        """
        クラス変数である場面の関係を出力する関数。
        import json が必要
        :return: なし
        """
        cls.show_dict(cls.over_view.get('scenes_context'))

    @classmethod
    def show_dict(cls, a_dict):
        print("{}".format(json.dumps(a_dict, ensure_ascii=False, indent=4)))
