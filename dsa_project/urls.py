from django.contrib import admin
from django.urls import path
from visualizer import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.home),   # Dashboard page (choose algorithms)
    path('login/', views.login),

    path('stack/', views.stack),
    path('queue/', views.queue),
    path('bfs/', views.bfs),
    path('dfs/', views.dfs),
    path('dijkstra/', views.dijkstra),
    path('astar/', views.astar),
    path('binary/', views.binary),
    path('sorting/', views.sorting),
    path('linkedlist/', views.linkedlist),
    path('tree/', views.tree),
    path('hashtable/', views.hashtable),
    path('kruskal/', views.kruskal),
    path('bellmanford/', views.bellmanford),
    path('insertion/', views.insertion),
    path('linear/', views.linear),
]