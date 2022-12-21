#!/usr/bin/python3
"""Class to define Node singly linked list"""


class Node:
    """ Node class rep """

    def __init__(self, data, next_node=None):
        """ initialize the attributes """

        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """ retrieve data """
        return self.__data

    @data.setter
    def data(self, value):
        """ sets attribute data to a value """
        if (not isinstance(value, int)):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """ retrieve attribute next_node """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """ Sets attribute next_node with class Node value """
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:

    """ Class of singly linked list """
    def __init__(self):
        """ initialize attributes """
        self.__head = None

    def sorted_insert(self, value):
        """ add new node in a sorted position """
        new = Node(value)
        if self.__head is None:
            new.next_node = None
            self.__head = new
        elif self.__head.data > value:
            new.next_node = self.__head
            self.__head = new
        else:
            temp = self.__head
            while (temp.next_node is not None and temp.next_node.data < value):
                temp = temp.next_node
            new.next_node = temp.next_node
            temp.next_node = new

    def __str__(self):
        """ Make the class printable"""
        val = []
        temp = self.__head
        while temp is not None:
            val.append(str(temp.data))
            temp = temp.next_node
        return ('\n'.join(val))
