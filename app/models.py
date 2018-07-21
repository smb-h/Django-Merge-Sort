from django.db import models
from django.urls import reverse




# Tree
class Tree(models.Model):
    root = models.CharField(max_length = 1000)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)

    def get_absolute_url(self):
        return reverse('Detail', kwargs= {'id': self.id })

    class Meta:
        verbose_name = 'Tree'
        verbose_name_plural = 'Tree'
        ordering = ('-created',)

    def __str__(self):
        # return ('{} - {}'.format(self.data, self.created))
        return ('{}'.format(self.root))



# Nodes Information
class Node(models.Model):
    TreeRoot = models.ForeignKey(Tree, on_delete = models.CASCADE)
    parent = models.CharField(max_length = 1000, blank=True, null=True)
    nodeData = models.CharField(max_length = 1000)
    lchild = models.CharField(max_length = 500, blank=True, null=True)
    rchild = models.CharField(max_length = 500, blank=True, null=True)
    # children = models.CharField(max_length = 500, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
