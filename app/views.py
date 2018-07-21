# from django.contrib.auth.models import User, Group
from .models import Tree, Node
from . import NodeGenerator as NG
from . import TreeReader as TR
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, generics
# from django.shortcuts import get_object_or_404
from .serializers import TreeSerializer, NodeSerializer
# from django.views import generic
from rest_framework.response import Response
# from rest_framework.renderers import TemplateHTMLRenderer
# from rest_framework.views import APIView

from .forms import InputForm, OutputForm
# from django.views import generic


# from django.views.generic import TemplateView

from django.views import View
from django.http import HttpResponseRedirect
from django.shortcuts import render
# from django.contrib import messages
import os


class TreeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Datas to be viewed or edited.
    """
    # queryset = Tree.objects.all().order_by('-created')
    queryset = Tree.objects.all()
    serializer_class = TreeSerializer


class NodeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Nodes to be viewed or edited.
    """
    queryset = Node.objects.all().order_by('TreeRoot','created')
    serializer_class = NodeSerializer

    # queryset = Node.objects.filter(data= 45)




class TreeDetail(View):
    Oform = OutputForm
    # initial = {'key': 'value'}

    def get(self, request, *args, **kwargs):
        Target = get_object_or_404(Tree, id=kwargs.get('id'))
        Target = str(Target)[1:-1].split(',')
        pureData = []
        for num in Target:
            pureData.append(int(num))
        sortedData = pureData
        sortedData.sort()

        # Create Tree Config
        TR.TreeReader()

        form = self.Oform(request.GET or None)
        context = {'form': form, 
        # 'self': self.__dir__,
        # 'id': kwargs.get('id'),
        # 'req': request,
        'data': sortedData,
        'pure': pureData,
        }
        return render(request, 'Detail.html', context)

    def post(self, request, *args, **kwargs):
        return HttpResponseRedirect('Index.html')


class IndexView(View):
    
    Iform = InputForm
    # initial = {'key': 'value'}

    def get(self, request, *args, **kwargs):
        # form = self.Iform(initial=self.initial)
        form = self.Iform()
        context = {'form': form}

        # Clear Json
        if os.path.exists('RestJs.json'):
            os.remove('RestJs.json')

        return render(request, 'Index.html', context)

    def post(self, request, *args, **kwargs):
        form = self.Iform(request.POST or None)
        if form.is_valid():
            Input = form.cleaned_data['root']
            Input = Input.split(',')
            Root = []
            for num in Input:
                Root.append(int(num))

            tree = Tree.objects.create(
                root = Root,
            )

            # Node Manager
            # DATA Handler
            DH = Root
            parent = DH
            NG.NodeGenerator(tree, DH, parent)

        # messages.success(request, 'Created Successfully!', extra_tags='alert alert-success')
        return HttpResponseRedirect(tree.get_absolute_url())

        # context = {'form': form}
        # return render(request, 'Index.html', context)
    
    # template_name = 'Index.html'
    # Iform = InputForm()
    # Oform = OutputForm()
    # context = {
    #     'InForm' : Iform,
    #     'OutForm' : Oform
    # }

    # Rest Api
    # renderer_classes = [TemplateHTMLRenderer]
    # template_name = 'Index.html'
    # def get(self, request, pk):
    #     data = get_object_or_404(Data, pk=pk)
    #     serializer = DataSerializer(data)
    #     return Response({'serializer': serializer, 'data': data})

    # def post(self, request, pk):
    #     data = get_object_or_404(Data, pk=pk)
    #     serializer = DataSerializer(data, data=request.data)
    #     if not serializer.is_valid():
    #         return Response({'serializer': serializer, 'data': data})
    #     serializer.save()
    #     return redirect('profile-list')



