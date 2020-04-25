from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView, ListView

from goal.models import GoalTransaction


class CreateTransactionView(CreateView, LoginRequiredMixin):
    model = GoalTransaction


class UpdateTransactionView(UpdateView, LoginRequiredMixin):
    model = GoalTransaction


class DeleteTransactionView(DeleteView, LoginRequiredMixin):
    model = GoalTransaction

    def get_queryset(self):
        return GoalTransaction.objects.filter(goal__owner=self.request.user)
