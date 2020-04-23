from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from goal.forms import CreateGoalForm, UpdateGoalForm
from goal.models import Goal


class GoalListView(LoginRequiredMixin, ListView):
    def get_queryset(self):
        return Goal.objects.filter(owner=self.request.user)


class CreateGoalView(LoginRequiredMixin, CreateView):
    model = Goal
    form_class = CreateGoalForm
    template_name = 'goal/create_goal.html'

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

    def get_success_url(self):
        return reverse_lazy('goal:goal_detail', kwargs={'pk': self.object.pk},)


class UpdateGoalView(LoginRequiredMixin, UpdateView):
    model = Goal
    form_class = UpdateGoalForm

    def get_queryset(self):
        return Goal.objects.filter(owner=self.request.user)

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.owner = self.request.user
        name = form.cleaned_data.get('name')
        if Goal.objects.filter(owner=self.request.user, name=name):
            form.add_error('name', 'This goal is duplicated')
            return self.form_invalid(form)
        return super(UpdateGoalView, self).form_valid(form)


class DeleteGoalView(LoginRequiredMixin, DeleteView):
    success_url = reverse_lazy('')

    def get_queryset(self):
        return Goal.objects.filter(owner=self.request.user)

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


class GoalDetailView(LoginRequiredMixin, DetailView):
    model = Goal

    def get_queryset(self):
        return Goal.objects.filter(owner=self.request.user)
