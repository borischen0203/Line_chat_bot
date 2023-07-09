from django.http import HttpResponse
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import *
from django.views.decorators.csrf import csrf_exempt

line_bot_api = LineBotApi('CQm0BL4z/a2K/U83zm7QbTMWGBkmjlUXvurjeYQxHXNKZy5uUmpcUzaV+xY1oM/JbDxttHOkIWtSfCucgDvtRiiSCq1p6fmx7neitBe3GZ5B11Fq8IHyUGRB2o/w3b7U4TP7miGzB9ibjyKuQhx59AdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('ba98c88fab9fdec489f9b5bb31e53fe0')

@csrf_exempt  # Add this decorator to bypass CSRF verification for Line webhook
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
    user_message = event.message.text

    if user_message == "學校清單":
        reply_text = "Computer Science Conversion Programmes List\n"
        reply_text += "https://www.cs-conversion-list.com/"
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=reply_text)
        )
    elif user_message == "留學論壇":
        reply_message = TemplateSendMessage(
            alt_text="留學論壇",
            template=CarouselTemplate(
                columns=[
                    CarouselColumn(
                        title="英語系論壇",
                        text="可以到各校校版查詢申請進度",
                        actions=[
                            URIAction(label="The Student Room", uri="https://www.thestudentroom.co.uk/"),
                            URIAction(label="Reddit", uri="https://www.reddit.com/?feed=home")                           
                        ]
                    ),
                    CarouselColumn(
                        title="大陸論壇",
                        text="可查詢#轉碼申請",
                        actions=[
                            URIAction(label="一畝三分地", uri="https://www.1point3acres.com/bbs/"),
                            URIAction(label="小紅書", uri="https://www.xiaohongshu.com/search_result?keyword=%25E8%25BD%25AC%25E7%25A0%2581%25E7%2595%2599%25E5%25AD%25A6&source=web_search_result_notes"),
                            
                        ]
                    ),
                    CarouselColumn(
                        title="台灣論壇",
                        text="PTT另有英國留學版、荷蘭留學版、雅思版",
                        actions=[
                            URIAction(label="PTT 留學版", uri="https://www.pttweb.cc/bbs/studyabroad"),
                            URIAction(label="Dcard 留學版", uri="https://www.dcard.tw/f/studyabroad"),
                        ]
                    ),            
                ]
            )
        )

        line_bot_api.reply_message(
            event.reply_token,
            reply_message
        )

    else:
        reply_message = TemplateSendMessage(
            alt_text="功能說明",
            template=ButtonsTemplate(
                text="功能說明",
                actions=[
                    MessageAction(label="學校清單", text="學校清單"),
                    MessageAction(label="留學論壇", text="留學論壇"),
                    MessageAction(label="其他功能", text="其他功能")
                ]
            )
        )

        line_bot_api.reply_message(
            event.reply_token,
            reply_message
        )