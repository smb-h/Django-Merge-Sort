from django.contrib import admin
from .models import Tree, Node



class NodeInline(admin.TabularInline):
    model = Node


class TreeAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Data', {'fields': ['root']}),
    ]
    inlines = [NodeInline]

    # Display
    list_display = ('root', 'created', 'id')

    # Filter
    list_filter = ['id', 'created']

    # Search
    search_fields = ['created', 'id', 'root']


admin.site.register(Tree, TreeAdmin)


# class NodeAdmin(admin.ModelAdmin):
#     fieldsets = [
#         ('Info', {'fields': ['data', 'nodeData', 'parent', 'lchild', 'rchild']}),
#     ]

# admin.site.register(Node, NodeAdmin)