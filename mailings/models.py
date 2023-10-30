from django.db import models


class Client(models.Model):
    first_name = models.CharField(max_length=30, verbose_name='имя')
    last_name = models.CharField(max_length=30, verbose_name='фамилия')
    email = models.EmailField(verbose_name='email')
    note = models.CharField(max_length=300, verbose_name='комментарий')

    class Meta:
        verbose_name = 'клиент'
        verbose_name_plural = 'клиенты'

    def full_name(self):
        return f"{self.first_name} {self.last_name[:1]}."

    def __str__(self):
        return f"{self.first_name} {self.last_name[:1]}. ({self.email})"


class Periods(models.Model):
    name = models.CharField(max_length=50, verbose_name='название')
    pattern = models.CharField(max_length=20, verbose_name='cron-шаблон', unique=True)

    class Meta:
        verbose_name = 'период'
        verbose_name_plural = 'периоды'

    def __str__(self):
        return self.name


class Message(models.Model):
    body = models.TextField(verbose_name='содержимое')
    title = models.CharField(max_length=150, verbose_name='заголовок')

    class Meta:
        verbose_name = 'письмо'
        verbose_name_plural = 'письма'

    def __str__(self):
        return self.title


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
    content = models.OneToOneField(Message, on_delete=models.CASCADE, verbose_name='Содержание')

    class Meta:
        verbose_name = 'рассылка'
        verbose_name_plural = 'рассылки'

    def __str__(self):
        return self.name


class MailingLog(models.Model):
    STATUS_SUCCESS = 'success'
    STATUS_FAILED = 'fail'
    STATUS_ERROR = 'error'

    STATUSES = (
        (STATUS_SUCCESS, 'Доставлено'),
        (STATUS_FAILED, 'Не доставлено'),
        (STATUS_ERROR, 'Ошибка'),
    )

    time = models.DateTimeField(auto_now_add=True, verbose_name='время')
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name='получатель')
    mailing = models.ForeignKey(Mailing, on_delete=models.CASCADE, verbose_name='рассылка')
    status = models.CharField(max_length=20, choices=STATUSES, verbose_name='статус')
    error_message = models.CharField(max_length=250, verbose_name='Текст ошибки', blank=True, null=True)

    class Meta:
        verbose_name = 'лог'
        verbose_name_plural = 'логи'

    def __str__(self):
        return f"{self.client}, {self.status}, {self.time}"
