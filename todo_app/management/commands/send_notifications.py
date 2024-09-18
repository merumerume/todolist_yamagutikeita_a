from django.core.management.base import BaseCommand
from django.utils import timezone
from django.core.mail import send_mail
from todo_app.models import TodoList

class Command(BaseCommand):
    help = 'TODOタスクの期限通知を送信'

    def handle(self, *args, **kwargs):
        # 現在時刻に基づいて、期限が近いタスクを取得
        now = timezone.now()
        upcoming_tasks = TodoList.objects.filter(due_date__lte=now + timezone.timedelta(days=1))

        for task in upcoming_tasks:
            if task.due_date > now:  # まだ期限が過ぎていないタスクのみ
                subject = f'TODOリマインダー: {task.title}'
                message = f'以下のタスクの期限が近づいています。\n\nタスク: {task.title}\n期限: {task.due_date}\n優先度: {task.priority}\nコメント: {task.comment}'
                recipient_list = ['recipient_email@example.com']  # 受信者のメールアドレス
                send_mail(subject, message, 'your_email@gmail.com', recipient_list)

        self.stdout.write(self.style.SUCCESS('通知を送信しました'))
