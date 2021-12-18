from django.http import HttpResponse
from hello.client import APNsClient
from hello.payload import Payload
import collections
import pathlib
import json
from django.shortcuts import render
import os

# Create your views here.
def index(request):
    # device token
    if request.method == "POST":
        print(os.path.dirname(__file__))
        model = json.loads(request.body)
        token_hex = model["token"]
        phone_from = model["phone_from"]
        ws_room = model["ws_room"]
        payload = Payload(
            alert="Hello World!",
            sound="default",
            badge=1,
            custom={
                "phoneFrom": phone_from,
                "wsRoom": ws_room
            }
        )
        topic = 'ru.openbank.pushtest.voip'

        # client = APNsClient('/app/hello/voip.pem', use_sandbox=True, use_alternative_port=False)
        client = APNsClient('/Users/kirillvolodin/P2P/python-getting-started/hello/voip.pem', use_sandbox=True, use_alternative_port=False)
        client.send_notification(token_hex, payload, topic)

        # To send multiple notifications in a batch
        Notification = collections.namedtuple('Notification', ['token', 'payload'])
        notifications = [Notification(payload=payload, token=token_hex)]
        client.send_notification_batch(notifications=notifications, topic=topic)
        return HttpResponse(status=200)
    else:
        return HttpResponse(status=200)


def room(request, room_name):
    return render(request, 'room.html', {
        'room_name': room_name
    })