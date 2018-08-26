# Copyright (c) 2017-2018 luispenagos91@gmail.com
# Distribuido bajo la licencia MIT Software Licence
# Mas informacion http://www.opensource.org/licenses/mit-license.php

from core import schedule2
from apps.administracion.estadisticas.models import registroConectados
from apps.player.models import Player, Guild
from django.utils import timezone
from datetime import timedelta
from apps.varios.models import Top


def ha():

    now = timezone.now()
    count = Player.objects.all().filter(last_play__range=[now - timedelta(minutes=55), now]).count()
    registroConectados(time=now, count=count).save()

    """def getLastIdTop():
        try:
            last_id = Top.objects.values('id').last()['id']
            return last_id
        except Top.DoesNotExist:
            return 0 """

    Top.objects.all().delete()
    b = Player.objects.all().values('id', 'account_id', 'name', 'job', 'level', 'exp', 'ranking')
    for i in b:
        try:
            b = Guild.objects.get(id=i['id'])
        except Guild.DoesNotExist:
            pass
        a = Top()
        a.account_id = i['account_id']
        a.name = i['name']
        a.job = i['job']
        a.level = i['level']
        a.exp = i['exp']
        a.guild_name = b.name
        a.ranking = i['ranking']
        a.save()


def run_task(funcion_principal, funcion_secundaria):
    funcion_principal.every(1).hours.at(0).do(funcion_secundaria)
    funcion_principal.run_continuously()


run_task(schedule2, ha)
