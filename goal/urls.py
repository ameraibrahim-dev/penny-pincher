from django.contrib import admin
from django.urls import path, include
from .view import *

app_name = 'goal'
urlpatterns = [
    # goals
    path('list/', GoalListView.as_view(), name='goal_list'),
    path('create/', CreateGoalView.as_view(), name='create_goal'),
    path('update/<int:pk>/', UpdateGoalView.as_view(), name='update_goal'),
    path('delete/<int:pk>/', DeleteGoalView.as_view(), name='delete_goal'),
    path('detail/<int:pk>/', GoalDetailView.as_view(), name='goal_detail'),

    # transactions
    path('transaction/create/', CreateTransactionView.as_view(), name='create_transaction'),
    path('transaction/update/<int:pk>/', UpdateTransactionView.as_view(), name='update_transaction'),
    path('transaction/delete/<int:pk>', DeleteTransactionView.as_view(), name='delete_transaction'),
]
