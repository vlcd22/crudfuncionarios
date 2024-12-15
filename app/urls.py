from django.urls import path, include
urlpatterns = [

]

from django.urls import path, include
from .views import FuncionarioCreateView
urlpatterns = [
path("form_funcionario", FuncionarioCreateView.as_view()),
]

from django.urls import path, include
from .views import FuncionarioCreateView, FuncionarioListView
urlpatterns = [
path('form_funcionario', FuncionarioCreateView.as_view()),
 path('lista_funcionarios', FuncionarioListView.as_view(), name = "lista_funcionarios"),
]

from django.urls import path, include
from .views import FuncionarioCreateView, FuncionarioListView, FuncionarioUpdateView
urlpatterns = [
path('form_funcionario', FuncionarioCreateView.as_view()),
path('lista_funcionarios', FuncionarioListView.as_view(), name = "lista_funcionarios"),
 path('form_funcionario/<int:pk>', FuncionarioUpdateView.as_view(), name = "editar_funcionario"),
]

from django.urls import path
from .views import (
    FuncionarioCreateView,
    FuncionarioListView,
    FuncionarioUpdateView,
    FuncionarioDetailView
)

urlpatterns = [
    path('form_funcionario/', FuncionarioCreateView.as_view(), name='form_funcionario'),
    path('lista_funcionarios/', FuncionarioListView.as_view(), name='lista_funcionarios'),
    path('form_funcionario/<int:pk>/', FuncionarioUpdateView.as_view(), name='editar_funcionario'),
    path('lista_funcionario/<int:pk>/', FuncionarioDetailView.as_view(), name='listar_funcionario'),
]

from django.urls import path
from .views import (
    FuncionarioCreateView, 
    FuncionarioListView, 
    FuncionarioUpdateView,
    FuncionarioDetailView,
    FuncionarioDeleteView
)

urlpatterns = [
    path("form_funcionario/", FuncionarioCreateView.as_view(), name="form_funcionario"),  
    path("lista_funcionarios/", FuncionarioListView.as_view(), name="lista_funcionarios"),  
    path("form_funcionario/<int:pk>/", FuncionarioUpdateView.as_view(), name="editar_funcionario"),  
    path("lista_funcionario/<int:pk>/", FuncionarioDetailView.as_view(), name="listar_funcionario"),  
    path("remover_funcionario/<int:pk>/", FuncionarioDeleteView.as_view(), name="remover_funcionario"),  
]

from django.urls import path, include
from .views import (
FuncionarioCreateView,
FuncionarioListView,
FuncionarioUpdateView,
FuncionarioDetailView,
FuncionarioDeleteView
)

urlpatterns = [
path('form_funcionario/', FuncionarioCreateView.as_view(), name="form_funcionario"),
path('lista_funcionarios/', FuncionarioListView.as_view(), name="lista_funcionarios"),
path('form_funcionario/<int:pk>/', FuncionarioUpdateView.as_view(), name="editar_funcionario"),
path('lista_funcionario/<int:pk>/', FuncionarioDetailView.as_view(), name="listar_funcionario"),
path('remover_funcionario/<int:pk>/', FuncionarioDeleteView.as_view(), name="remover_funcionario"),
]
