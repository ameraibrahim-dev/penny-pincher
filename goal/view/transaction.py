from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView, ListView

from goal.forms import GoalTransactionForm
from goal.models import GoalTransaction


class CreateTransactionView(CreateView, LoginRequiredMixin):
    model = GoalTransaction
    form_class = GoalTransactionForm


class UpdateTransactionView(UpdateView, LoginRequiredMixin):
    model = GoalTransaction
    form_class = GoalTransactionForm

    def get_queryset(self):
        return GoalTransaction.objects.filter(goal__owner=self.request.user)


class DeleteTransactionView(DeleteView, LoginRequiredMixin):
    model = GoalTransaction

    def get_queryset(self):
        return GoalTransaction.objects.filter(goal__owner=self.request.user)

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)
