from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from goal.forms import CreateGoalForm
from goal.models import Goal


class GoalListView(LoginRequiredMixin, ListView):
    def get_queryset(self):
        return Goal.objects.filter(owner=self.request.user)


class CreateGoalView(LoginRequiredMixin, CreateView):
    model = Goal
    form_class = CreateGoalForm

    def get_queryset(self):
        return Goal.objects.filter(owner=self.request.user)

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.owner = self.request.user
        name = form.cleaned_data.get('name')
        if Goal.objects.filter(owner=self.request.user, name=name):
            form.add_error('name', 'This goal is duplicated')
            return self.form_invalid(form)
        return super(CreateGoalView, self).form_valid(form)


class UpdateGoalView(LoginRequiredMixin, UpdateView):
    model = Goal
    fields = ['']

    def get_queryset(self):
        return Goal.objects.filter(owner=self.request.user)

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.owner = self.request.user
        name = form.cleaned_data.get('name')
        if Goal.objects.filter(owner=self.request.user, name=name):
            form.add_error('name', 'This goal is duplicated')
            return self.form_invalid(form)
        return super(CreateGoalView, self).form_valid(form)


class DeleteGoalView(LoginRequiredMixin, DeleteView):
    model = Goal
    fields = ['']

    def get_queryset(self):
        return Goal.objects.filter(owner=self.request.user)

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.owner = self.request.user
        name = form.cleaned_data.get('name')
        if Goal.objects.filter(owner=self.request.user, name=name):
            form.add_error('name', 'This goal is duplicated')
            return self.form_invalid(form)
        return super(CreateGoalView, self).form_valid(form)
