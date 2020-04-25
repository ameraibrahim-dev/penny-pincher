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
        # update goal balance
        amount = -instance.amount.amount if instance.is_expense else instance.amount.amount
        instance.goal = goal
        instance.goal.balance.amount += amount
        if instance.goal.balance.amount < 0:
            form.add_error('amount', 'sufficient goal balance')
            return self.form_invalid(form)
        instance.goal.save()
        return super(CreateTransactionView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Add Transaction'
        return context

    def get_success_url(self):
        return reverse_lazy('goal:goal_detail', kwargs={'pk': self.kwargs.get('pk')})


class UpdateTransactionView(UpdateView, LoginRequiredMixin):
    model = GoalTransaction
    form_class = GoalTransactionForm
    template_name = 'goal_transaction/transaction_form.html'

    def get_queryset(self):
        return GoalTransaction.objects.filter(goal__owner=self.request.user)

    def get_success_url(self):
        return reverse_lazy('goal:goal_detail', kwargs={'pk': self.get_object().goal.pk})


class DeleteTransactionView(DeleteView, LoginRequiredMixin):
    model = GoalTransaction

    def get_queryset(self):
        return GoalTransaction.objects.filter(goal__owner=self.request.user)

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    def get_success_url(self):
        return reverse_lazy('goal:goal_detail', kwargs={'pk': self.get_object().goal.pk})
