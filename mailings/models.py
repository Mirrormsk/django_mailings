from django.db import models


class Client(models.Model):
    first_name = models.CharField(max_length=30, verbose_name='имя')
    last_name = models.CharField(max_length=30, verbose_name='фамилия')
    email = models.EmailField(verbose_name='email')
    note = models.CharField(max_length=300, verbose_name='комментарий')


class Periods(models.Model):
    name = models.CharField(max_length=50, verbose_name='название')
    pattern = models.CharField(max_length=20, verbose_name='cron-шаблон')


class Message(models.Model):
    body = models.TextField(verbose_name='содержимое')
    title = models.CharField(max_length=150, verbose_name='заголовок')


class Mailing(models.Model):
    STATUS_CREATED = 'created'
    STATUS_STARTED = 'started'
    STATUS_FINISHED = 'finished'

    STATUSES = (
        (STATUS_CREATED, 'Создана'),
        (STATUS_STARTED, 'Запущена'),
        (STATUS_FINISHED, 'Завершена'),
    )
    name = models.CharField(max_length=150, verbose_name='Название')
    status = models.CharField(max_length=20, choices=STATUSES, verbose_name='статус', default=STATUS_CREATED)
    period = models.ForeignKey(Periods, on_delete=models.CASCADE, verbose_name='периодичность')

    recipients = models.ManyToManyField(Client, verbose_name='получатели')
    start_time = models.DateTimeField(verbose_name='время начала')
    end_time = models.DateTimeField(verbose_name='время окончания')
    content = models.ForeignKey(Message, on_delete=models.CASCADE, verbose_name='Содержание')
