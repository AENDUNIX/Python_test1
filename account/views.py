from django.contrib.auth.models import User
from django.views.generic import ListView

from .models import UserInfo


class Profile(ListView):
    template_name = 'account/profile.html'
    context_object_name = 'object'
    model = User

    def get_context_data(self, *, object_list=None, **kwargs):
        if self.request.user.is_authenticated:
            ctx = super(Profile, self).get_context_data(**kwargs)
            user = UserInfo.objects.filter(user=self.request.user)[0]
            ctx['user'] = user.user
            ctx['name'] = user.name
            ctx['user_name'] = user.user_name
            ctx['user_telegram_id'] = user.user_telegram_id
            return ctx
        print(self.request.user.is_authenticated)

