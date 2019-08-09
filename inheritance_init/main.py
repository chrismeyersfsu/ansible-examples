#!/usr/bin/env python


class A(object):
    def __init__(self, member_attr, name_attr='foobar'):
        print("Called A.__init__()");
        print("Required is {} and option is {}".format(member_attr, name_attr))


class B(A):
    def __init___(self, member_attr, name_attr='foobar'):
        print("Called B.__init__()");
        super(B, self).__init__('member', name_attr)


B(member_attr='member_not', name_attr='foobarish')
