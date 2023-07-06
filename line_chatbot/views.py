from django.http import HttpResponse
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage

line_bot_api = LineBotApi('xNFX6oUap2qKVSk1ImnTOMcjECTJDVLy4SeoTlPxu7k/8fHeGuMC2M2IhA4AeWLEsliEgpTM1cAXLIyFRpT2sbwOCpWytK2YOFc+gSDX+s/zvzsv6T/tknM/bhY7NxD6EPL0StbtPr+7DCtua8L83wdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('7d01a80ca09355c3c706041f1d6aa1b0')

def line_webhook(request):
    if request.method == 'POST':
        signature = request.headers['X-Line-Signature']
        body = request.body.decode()
        try:
            handler.handle(body, signature)
        except InvalidSignatureError:
            return HttpResponse(status=400)
        return HttpResponse(status=200)
    return HttpResponse(status=405)

@handler.add(MessageEvent, message=TextMessage)
def handle_text_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextMessage(text='Hello, world!'))