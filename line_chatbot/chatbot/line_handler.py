from django.http import HttpResponse
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage

from line_chatbot.line_settings import CHANNEL_ACCESS_TOKEN, CHANNEL_SECRET

line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(CHANNEL_SECRET)

def line_webhook(request):
    signature = request.META['HTTP_X_LINE_SIGNATURE']
    body = request.body.decode('utf-8')

    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        return HttpResponse(status=400)

    return HttpResponse(status=200)

@handler.add(MessageEvent, message=TextMessage)
def handle_text_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextMessage(text="Hello, you said: " + event.message.text)
    )
