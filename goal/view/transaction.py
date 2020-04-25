from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView, ListView

from goal.models import GoalTransaction


class TransactionListView(ListView, LoginRequiredMixin):
    model = GoalTransaction

    def get_queryset(self):
        return GoalTransaction.objects.filter(goal__owner=self.request.user)

class CreateTransactionView(CreateView, LoginRequiredMixin):
    model = GoalTransaction


class TransactionDetailView(DetailView, LoginRequiredMixin):
    model = GoalTransaction


class UpdateTransactionView(UpdateView, LoginRequiredMixin):
    model = GoalTransaction


class DetailTransactionView(DeleteView, LoginRequiredMixin):
    model = GoalTransaction

    def get_queryset(self):
        return GoalTransaction.objects.filter(goal__owner=self.request.user)
