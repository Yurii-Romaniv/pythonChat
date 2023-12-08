from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render
from django.db.models import Q
from django.utils.decorators import method_decorator
from .models import Chats, Messages
from django.views import View


@method_decorator(login_required, name='dispatch')
class UserPanel(View):

    def _load_user(self, user):
        class chatR:
            def __init__(self, name, chat_w):
                self.name = str(name)
                self.id = chat_w
                self.messages = (
                    Messages.objects.filter(Q(author=user) | Q(author=name)).filter(chat=chat_w)).order_by("id")

        chats_queries = Chats.objects.filter(Q(owner1=user.id) | Q(owner2=user.id))
        chats = []

        for chat in chats_queries:
            chats.append(chatR(chat.owner1 if chat.owner2 == user else chat.owner2, chat.id))

        resp = {"user": user, "chats": chats}
        return resp

    def get(self, request):
        return render(request, 'mkchat/userPanel.html', self._load_user(request.user))


@method_decorator(login_required, name='dispatch')
class SendMess(View):
    def post(self, request):
        chat = request.POST['chat']
        text = request.POST['text']

        mess = Messages(author=request.user, text=text, chat=Chats.objects.get(id=chat))
        mess.save()

        return JsonResponse({"a": 1, "b": 2})
