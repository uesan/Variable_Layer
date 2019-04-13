class SinglyLinkedList(object):
    '''
    Singly-linked list such that each node is the instance of ListElement class
    '''
    def __init__(self, init_elems=[]):
        '''
        init_elemsが空でない時，init_elemsに与えられたリストに対応する連結リストを返す
        >>> s1 = SinglyLinkedList()
        >>> s1
        []
        >>> s2 = SinglyLinkedList([1, 2, 3, 4, 5])
        >>> s2
        [1, 2, 3, 4, 5]
        '''
        self.head = ListElement()
        self.head.next = None
        for ie in init_elems:
            self.append(ie)

    def __contains__(self, value):
        '''
        valueの値が連結リスト中に含まれるかを返す特殊メソッド
        'e in s'の記法によっても呼び出される
        >>> s = SinglyLinkedList([1, 2, 3])
        >>> 1 in s
        True
        >>> 3 in s
        True
        >>> 5 in s
        False
        '''
        sp = self.head
        while sp.next is not None:
            sp = sp.next
            if sp.value == value:
                return True
        else:
            return False

    def __getitem__(self, index):
        '''
        indexの位置にある値を返す特殊メソッド
        's[index]'の記法によっても呼び出される
        indexが整数でない場合，TypeError例外を返す
        indexの位置に要素が存在しない場合，IndexError例外を返す
        __iter__メソッドが定義されていない場合はforループで__getitem__メソッドが呼ばれる
        >>> s = SinglyLinkedList([1, 2, 3])
        >>> s[2]
        3
        >>> s[-3]
        1
        >>> s[5]
        Traceback (most recent call last):
            ...
        IndexError
        >>> s['hoge']
        Traceback (most recent call last):
            ...
        TypeError
        '''
        if not (isinstance(index, int)):
            raise TypeError
        if not (-1 * len(self) <= index < len(self)):
            raise IndexError
        if index < 0:
            index += len(self)
        sp = self.head
        for i in range(index):
            sp = sp.next
        return sp.next

    def __setitem__(self, index, value):
        '''
        indexの位置にある値をvalueで書き換える特殊メソッド
        's[index] = value'の記法によっても呼び出される
        例外の処理は__getitem__メソッドと同じ
        >>> s = SinglyLinkedList([1,2,3])
        >>> s[2] = 4
        >>> s
        [1, 2, 4]
        >>> s[-3] = 5
        >>> s
        [5, 2, 4]
        >>> s[-4] = 6
        Traceback (most recent call last):
            ...
        IndexError
        >>> s['fuga'] = 7
        Traceback (most recent call last):
            ...
        TypeError
        '''
        if not (isinstance(index, int)):
            raise TypeError
        if not (-1 * len(self) <= index < len(self)):
            raise IndexError
        if index < 0:
            index += len(self)
        sp = self.head
        for i in range(index):
            sp = sp.next
        sp.next.value = value

    def __delitem__(self, index):
        '''
        indexの位置にある値を連結リストから削除する特殊メソッド
        'del s[index]'の記法によっても呼び出される
        例外の処理は__getitem__メソッドと同じ
        >>> s = SinglyLinkedList([1,2,3])
        >>> del s[2]
        >>> s
        [1, 2]
        >>> del s[-2]
        >>> s
        [2]
        >>> del s[1]
        Traceback (most recent call last):
            ...
        IndexError
        >>> del s['piyo']
        Traceback (most recent call last):
            ...
        TypeError
        '''
        if not (isinstance(index, int)):
            raise TypeError
        if not (-1 * len(self) <= index < len(self)):
            raise IndexError
        if index < 0:
            index += len(self)
        sp = self.head
        for i in range(index):
            sp = sp.next
        n = sp.next
        sp.next = sp.next.next
        del n

    def __len__(self):
        '''
        連結リストの長さを返す特殊メソッド
        'len(s)'の記法によっても呼び出される
        >>> s = SinglyLinkedList([1, 2, 3])
        >>> len(s)
        3
        >>> for e in s:
        ...     print e
        1
        2
        3
        '''
        sp = self.head
        count = 0
        while sp.next is not None:
            sp = sp.next
            count += 1
        return count

    def __iter__(self):
        '''
        イテレータを返す特殊メソッド
        'iter(s)'の記法や，forループを行うごとに呼び出される
        イテレータの定義はSinglyLinkedListIteratorクラスで行う

        >>> s = SinglyLinkedList([1, 2, 3])
        >>> for e in s:
        ...     print e
        1
        2
        3
        '''
        return SinglyLinkedListIterator(self.head)

    def __str__(self):
        '''
        連結リストの「非公式な」文字列を返す特殊メソッド
        ’str(s)’や，'print s'の記法によっても呼び出される
        >>> s = SinglyLinkedList([1, 2])
        >>> str(s)
        'SinglyLinkedList: [1, 2]'
        >>> print s
        SinglyLinkedList: [1, 2]
        '''
        sp = self.head
        array = []
        while sp.next is not None:
            sp = sp.next
            array.append(sp.value)
        return 'SinglyLinkedList: ' + '[' + ', '.join(map(str, array)) + ']'

    def __repr__(self):
        '''
        連結リストの「公式な」文字列を返す特殊メソッド
        REPLによる戻り値や，'eval('s')'の記法によっても呼び出される
        __str__メソッドが定義されていない場合は，print文などでも__repr__が呼ばれる
        >>> s = SinglyLinkedList([1, 2])
        >>> s
        [1, 2]
        >>> eval('s')
        [1, 2]
        '''
        sp = self.head
        array = []
        while sp.next is not None:
            sp = sp.next
            array.append(sp.value)
        return repr(array)

    def append(self, value):
        '''
        valueの値を連結リストの末尾に追加するメソッド
        >>> s = SinglyLinkedList([1, 2, 3])
        >>> s.append(4)
        >>> s
        [1, 2, 3, 4]
        '''
        self.insert(len(self), value)

    def insert(self, index, value):
        '''
        連結リストのindexの位置にある値の直前にvalueの値を挿入するメソッド
        例外の処理は__getitem__メソッドと同じ
        >>> s = SinglyLinkedList([1, 2, 3])
        >>> s.insert(1, 4)
        >>> s
        [1, 4, 2, 3]
        >>> s.insert(4, 5)
        >>> s
        [1, 4, 2, 3, 5]
        >>> s.insert(-5, 6)
        >>> s
        [6, 1, 4, 2, 3, 5]
        >>> s.insert(7, 7)
        Traceback (most recent call last):
            ...
        IndexError
        >>> s.insert('foo', 8)
        Traceback (most recent call last):
            ...
        TypeError
        '''
        if not (isinstance(index, int)):
            raise TypeError
        if not (-1 * len(self) <= index <= len(self)):
            raise IndexError
        if index < 0:
            index += len(self)
        sp = self.head
        for i in range(index):
            sp = sp.next
        n = ListElement(value=value)
        n.next = sp.next
        sp.next = n

class ListElement(object):
    '''
    Element of linked list
    '''
    def __init__(self, value=None):
        '''
        valueが要素の値，nextが次ポインタを表す
        '''
        self.value = value
        self.next = None

    def __str__(self):
        '''
        >>> l = ListElement(3)
        >>> print l
        3
        '''
        return str(self.value)

    def __repr__(self):
        '''
        >>> l = ListElement(3)
        >>> l
        3
        '''
        return repr(self.value)

class SinglyLinkedListIterator(object):
    '''
    Iterator for the instance of SinglyLinkedList class
    '''
    def __init__(self, head):
        self.head = head
        self.node = self.head.next

    def next(self):
        '''
        イテレータをたどる際に呼ばれるメソッド
        'next(iterator)'の記法によっても呼び出される

        ループが終了した時にStopIteration例外を返す
        それ以外の場合は要素の値を返す
        '''
        if self.node is None:
            raise StopIteration
        else:
            val = self.node.value
            self.node = self.node.next
            return val

if __name__ == '__main__':
    import doctest
    doctest.testmod()