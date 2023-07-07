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
        url = "https://c0dc-2001-b400-e207-f782-b559-1684-ccdb-8024.ngrok-free.app/line/webhook/"
        csrf_token = request.COOKIES[
            "csrftoken"
        ]  # Obtain the CSRF token from the request's cookies

        headers = {"X-CSRFToken": csrf_token}
        response = requests.post(url, headers=headers)

        body = request.body.decode("utf-8")
        try:
            handler.handle(body, signature)
        except InvalidSignatureError:
            return HttpResponse(status=200)
        return HttpResponse(status=200)
    return HttpResponse(status=200)


@handler.add(MessageEvent, message=TextMessage)
def handle_text_message(event):
    line_bot_api.reply_message(event.reply_token, TextMessage(text="Hello, world!"))
