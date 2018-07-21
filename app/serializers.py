# from django.contrib.auth.models import User, Group
from .models import Node, Tree
from rest_framework import serializers


class TreeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tree
        fields = ('root',)


class NodeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Node
        fields = ('TreeRoot', 'parent', 'nodeData', 'lchild', 'rchild')