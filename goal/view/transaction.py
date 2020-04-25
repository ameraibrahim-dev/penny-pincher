from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView, ListView

from goal.forms import GoalTransactionForm
from goal.models import GoalTransaction, Goal
from django.urls import reverse_lazy

class CreateTransactionView(CreateView, LoginRequiredMixin):
    model = GoalTransaction
    form_class = GoalTransactionForm
    template_name = 'goal_transaction/transaction_form.html'
    def form_valid(self, form):
        instance = form.save(commit=False)
        goal_pk = self.kwargs.get('pk')
        goal = Goal.objects.get(pk=goal_pk)
        instance.goal = goal
        return super(CreateTransactionView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Add Transaction'
        return context
    def get_success_url(self):
        return reverse_lazy()



class UpdateTransactionView(UpdateView, LoginRequiredMixin):
    model = GoalTransaction
    form_class = GoalTransactionForm
    template_name = 'goal_transaction/transaction_form.html'

    def get_queryset(self):
        return GoalTransaction.objects.filter(goal__owner=self.request.user)


class DeleteTransactionView(DeleteView, LoginRequiredMixin):
    model = GoalTransaction

    def get_queryset(self):
        return GoalTransaction.objects.filter(goal__owner=self.request.user)

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)
