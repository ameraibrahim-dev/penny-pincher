from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

from goal.models import Goal, GoalTransaction
from wallet.models import Wallet, WalletTransaction


class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        # goal,wallet
        context = super().get_context_data(**kwargs)
        order_by_list = ['-updated', '-created']  # order desc
        # get latest wallet
        wallet = WalletTransaction.objects.filter(wallet__owner=self.request.user).order_by(*order_by_list).first()
        if not wallet:
            wallet = Wallet.objects.filter(owner=self.request.user).order_by(*order_by_list).first()
        else:
            # extract wallet from transaction
            wallet = wallet.wallet
        context['wallet'] = wallet

        # Get Latest Goal
        goal = GoalTransaction.objects.filter(goal__owner=self.request.user).order_by(*order_by_list).first()
        if not goal:
            goal = Goal.objects.filter(owner=self.request.user).order_by(*order_by_list).first()
        else:
            # extract goal from transaction
            goal = goal.goal
        context['goal'] = goal
        return context
