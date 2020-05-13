from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView

from goal.forms import GoalTransactionForm
from goal.models import GoalTransaction, Goal


class CreateTransactionView(CreateView, LoginRequiredMixin):
    model = GoalTransaction
    form_class = GoalTransactionForm
    template_name = 'goal_transaction/transaction_form.html'

    def form_valid(self, form):
        instance = form.save(commit=False)
        goal_pk = self.kwargs.get('pk')
        goal = Goal.objects.get(owner=self.request.user, pk=goal_pk)
        # update goal balance
        amount = -instance.amount.amount if instance.is_expense else instance.amount.amount
        instance.goal = goal
        instance.goal.balance.amount += amount
        if instance.goal.balance.amount < 0:
            form.add_error('amount', 'Insufficient goal balance')
            return self.form_invalid(form)
        instance.goal.save()
        return super(CreateTransactionView, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('goal:goal_detail', kwargs={'pk': self.kwargs.get('pk')})
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        goal_pk = self.kwargs.get('pk')
        goal = Goal.objects.filter(owner=self.request.user, pk=goal_pk).first()
        context['goal'] = goal
        return context


class UpdateTransactionView(UpdateView, LoginRequiredMixin):
    model = GoalTransaction
    form_class = GoalTransactionForm
    template_name = 'goal_transaction/transaction_form.html'

    def form_valid(self, form):
        instance = form.save(commit=False)
        original_transaction_instance = GoalTransaction.objects.get(goal__owner=self.request.user, pk=instance.pk)
        # rollback
        if original_transaction_instance.is_expense:
            instance.goal.balance.amount += original_transaction_instance.amount.amount
        else:
            instance.goal.balance.amount -= original_transaction_instance.amount.amount

        # update goal balance
        amount = -instance.amount.amount if instance.is_expense else instance.amount.amount
        instance.goal.balance.amount += amount
        if instance.goal.balance.amount < 0:
            form.add_error('amount', 'Insufficient goal balance')
            return self.form_invalid(form)
        instance.goal.save()
        return super(UpdateTransactionView, self).form_valid(form)

    def get_queryset(self):
        return GoalTransaction.objects.filter(goal__owner=self.request.user)

    def get_success_url(self):
        return reverse_lazy('goal:goal_detail', kwargs={'pk': self.get_object().goal.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['goal'] = self.get_object()
        return context


class DeleteTransactionView(DeleteView, LoginRequiredMixin):
    model = GoalTransaction

    def get_queryset(self):
        return GoalTransaction.objects.filter(goal__owner=self.request.user)

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    def get_success_url(self):
        return reverse_lazy('goal:goal_detail', kwargs={'pk': self.get_object().goal.pk})

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.goal.owner == request.user:
            if self.object.is_expense:
                self.object.goal.balance.amount += self.object.amount.amount
            else:
                self.object.goal.balance.amount -= self.object.amount.amount
            self.object.goal.save()
        return super(DeleteTransactionView, self).delete(request, args, kwargs)
