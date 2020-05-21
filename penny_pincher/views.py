from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import TemplateView

from goal.models import Goal, GoalTransaction
from wallet.models import Wallet, WalletTransaction


class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        # goal,wallet
        context = super().get_context_data(**kwargs)
        order_by_list = ['-opened']  # order desc
        # get latest wallet
        wallet = Wallet.objects.filter(owner=self.request.user).order_by(*order_by_list).first()
        context['wallet'] = wallet

        # Get Latest Goal
        goal = Goal.objects.filter(owner=self.request.user).order_by(*order_by_list).first()
        context['goal'] = goal
        return context


def custom_page_not_found_view(request, exception):
    template = 'errors/404.html'
    context = {}
    return render(request, template, context)


def custom_error_view(request, exception=None):
    template = 'errors/500.html'
    context = {}
    return render(request, template, context)


def custom_permission_denied_view(request, exception=None):
    template = 'errors/403.html'
    context = {}
    return render(request, template, context)


def custom_bad_request_view(request, exception=None):
    template = 'errors/400.html'
    context = {}
    return render(request, template, context)
