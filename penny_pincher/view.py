from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

from wallet.models import Wallet


class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # get wallet
        order_by_list = ['-updated', '-created']  # order desc
        wallets = Wallet.objects.filter(owner=self.request.user).order_by(*order_by_list)
        context['wallets'] = wallets
        return context
