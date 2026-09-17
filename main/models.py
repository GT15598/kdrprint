from django.db import models


class Project(models.Model):
    CATEGORY_CHOICES = [
        ('advertising', 'Жарнама'),
        ('print', 'Баспа'),
        ('design', 'Дизайн'),
        ('outdoor', 'Сыртқы жарнама'),
    ]

    title = models.CharField(
        max_length=200,
        verbose_name='Жоба атауы'
    )

    category = models.CharField(
        max_length=30,
        choices=CATEGORY_CHOICES,
        default='advertising',
        verbose_name='Санат'
    )

    description = models.TextField(
        blank=True,
        verbose_name='Сипаттама'
    )

    image = models.ImageField(
        upload_to='projects/',
        verbose_name='Негізгі сурет'
    )

    year = models.PositiveIntegerField(
        default=2026,
        verbose_name='Жыл'
    )

    is_featured = models.BooleanField(
        default=False,
        verbose_name='Таңдаулы жоба'
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Қосылған уақыты'
    )

    class Meta:
        verbose_name = 'Жоба'
        verbose_name_plural = 'Жобалар'
        ordering = ['-created_at']

    def __str__(self):
        return self.title


class Service(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name='Қызмет атауы'
    )

    slug = models.SlugField(
        max_length=200,
        unique=True,
        blank=True,
        verbose_name='URL атауы'
    )

    short_title = models.CharField(
        max_length=100,
        blank=True,
        verbose_name='Қысқа атауы'
    )

    description = models.TextField(
        verbose_name='Қысқаша сипаттама'
    )

    full_description = models.TextField(
        blank=True,
        verbose_name='Толық сипаттама'
    )

    image = models.ImageField(
        upload_to='services/',
        blank=True,
        null=True,
        verbose_name='Негізгі сурет'
    )

    number = models.PositiveIntegerField(
        default=1,
        verbose_name='Реттік нөмір'
    )

    is_active = models.BooleanField(
        default=True,
        verbose_name='Белсенді'
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Қосылған уақыты'
    )

    class Meta:
        verbose_name = 'Қызмет'
        verbose_name_plural = 'Қызметтер'
        ordering = ['number', 'created_at']

    def __str__(self):
        return self.title



class ServiceImage(models.Model):
    service = models.ForeignKey(
        Service,
        on_delete=models.CASCADE,
        related_name='gallery',
        verbose_name='Қызмет'
    )

    image = models.ImageField(
        upload_to='services/gallery/',
        verbose_name='Сурет'
    )

    caption = models.CharField(
        max_length=200,
        blank=True,
        verbose_name='Сурет атауы'
    )

    order = models.PositiveIntegerField(
        default=1,
        verbose_name='Реттік нөмір'
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Қосылған уақыты'
    )

    class Meta:
        verbose_name = 'Галерея суреті'
        verbose_name_plural = 'Галерея суреттері'
        ordering = ['order', 'created_at']

    def __str__(self):
        return f'{self.service.title} — {self.order}'


