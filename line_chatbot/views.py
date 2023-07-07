from django.http import HttpResponse
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage

line_bot_api = LineBotApi(
    "CQm0BL4z/a2K/U83zm7QbTMWGBkmjlUXvurjeYQxHXNKZy5uUmpcUzaV+xY1oM/JbDxttHOkIWtSfCucgDvtRiiSCq1p6fmx7neitBe3GZ5B11Fq8IHyUGRB2o/w3b7U4TP7miGzB9ibjyKuQhx59AdB04t89/1O/w1cDnyilFU="
)
handler = WebhookHandler("ba98c88fab9fdec489f9b5bb31e53fe0")


def line_webhook(request):
    if request.method == "POST":
        signature = request.headers["X-Line-Signature"]
        body = request.body.decode()
        try:
            handler.handle(body, signature)
        except InvalidSignatureError:
            return HttpResponse(status=400)
        return HttpResponse(status=200)
    return HttpResponse(status=405)


@handler.add(MessageEvent, message=TextMessage)
def handle_text_message(event):
    line_bot_api.reply_message(event.reply_token, TextMessage(text="Hello, world!"))
