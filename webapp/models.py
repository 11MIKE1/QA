from django.db import models


class First_Title(models.Model):
    litle_title = models.CharField(max_length=50, null=False, blank=False, verbose_name='Пред заголовок')
    main_title = models.CharField(max_length=50, null=False, blank=False, verbose_name='Главный заголовок')
    button_1 = models.CharField(max_length=50, null=False, blank=False, verbose_name='Первая кнопка')
    button_2 = models.CharField(max_length=50, null=False, blank=False, verbose_name='Вторая кнопка')

    def __str__(self) -> str:
        return self.litle_title
    
    class Meta:
        verbose_name = "1) Первый раздел-Название курсов"
        verbose_name_plural = "1) Первый раздел-Название курсов"
    


class Second_Title(models.Model):
    title = models.CharField(max_length=50, null=False, blank=False, default=None, verbose_name='Заголовок')
    description = models.TextField(max_length=3000, blank=False, default=None, verbose_name='Описание')
    button = models.CharField(max_length=50, null=False, default=None, blank=False, verbose_name='Кнопка')

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = "2) Второй раздел-Подробное описание"
        verbose_name_plural = "2)Второй раздел-Подробное описание"


class Title(models.Model):
    first_title = models.CharField(max_length=50, null=False, blank=False, verbose_name='Заголовок третьего раздела')
    first_litle_title = models.CharField(max_length=50, null=False, blank=False, verbose_name='Пред заголовок третьего раздела')
    second_title = models.CharField(max_length=50, null=False, blank=False, verbose_name='Заголовок четвёртого раздела')
    third_title = models.CharField(max_length=50, null=False, blank=False, verbose_name='Заголовок пятого раздела')
    third_litle_title = models.CharField(max_length=50, null=False, blank=False, verbose_name='Пред заголовок пятого раздела')
    forth_title = models.CharField(max_length=50, null=False, blank=False, verbose_name='Заголовок седьмого раздела')
    forth_litle_title = models.CharField(max_length=50, null=False, blank=False, verbose_name='Пред заголовок седьмого раздела')

    def __str__(self) -> str:
        return self.first_title
    
    class Meta:
        verbose_name = "Заголовки разделов"
        verbose_name_plural = "Заголовки разделов"


class Third_title(models.Model):
    number = models.IntegerField(null=False, blank=False, default=None, verbose_name='Цифра')
    description = models.CharField(max_length=50, null=False, default=None, blank=False, verbose_name='Описание')

    def __str__(self) -> str:
        return self.description
    
    class Meta:
        verbose_name = "3) Третий раздел-Статистика обучающихся"
        verbose_name_plural = "3)Третий раздел-Статистика обучающихся"


class Forth_title(models.Model):
    litle_title = models.CharField(max_length=50, default=None, null=False, blank=False, verbose_name='Пред заголовок')
    name = models.CharField(max_length=50, null=False, default=None, blank=False, verbose_name='Имя ментора')
    experience = models.TextField(max_length=3000, blank=False, default=None, verbose_name='Опыт ментора')
    image = models.ImageField(default=None, verbose_name='Фото ментора')
    
    def __str__(self) -> str:
        return self.litle_title
    
    class Meta:
        verbose_name = "4) Четвёртый раздел-Менторы"
        verbose_name_plural = "4) Четвёртый раздел-Менторы"


class Fifth_title(models.Model):
    advantage = models.CharField(max_length=50, default=None, null=False, blank=False, verbose_name='Преимущество курса')
    price = models.CharField(max_length=50, null=False, blank=False, default=123, verbose_name='Стоимость курса')
    description_1 = models.CharField(max_length=50, null=False, default=None, blank=False, verbose_name='Первое описание')
    name = models.CharField(max_length=50, null=False, default=None, blank=False, verbose_name='Название курса')
    description_2 = models.CharField(max_length=50, null=False, default=None, blank=False, verbose_name='Подробное описание курса')
    button = models.CharField(max_length=50, null=False, default=None, blank=False, verbose_name='Кнопка')

    def __str__(self) -> str:
        return self.advantage
    
    class Meta:
        verbose_name = "5) Пятый раздел-Стоимость курсов"
        verbose_name_plural = "5) Пятый раздел-Стоимость курсов"


class Sixth_title(models.Model):
    litle_title = models.CharField(max_length=50, null=False, blank=False, verbose_name='Пред заголовок')
    main_title_1 = models.CharField(max_length=50, null=False, blank=False, verbose_name='Левый заголовок')
    description_1 = models.CharField(max_length=50, null=False, blank=False, verbose_name='Леове описание')
    main_title_2 = models.CharField(max_length=50, null=False, blank=False, verbose_name='Правый заголовок')
    description_2 = models.CharField(max_length=50, null=False, blank=False, verbose_name='Правое описание')
    button = models.CharField(max_length=50, null=False, blank=False, verbose_name='Кнопка')

    def __str__(self) -> str:
        return self.litle_title
    
    class Meta:
        verbose_name = "6) Шестой раздел-Дополнительная информация"
        verbose_name_plural = "6) Шестой раздел-Дополнительная информация"


class Seventh_title(models.Model):
    litle_title = models.TextField(max_length=500, null=False, default='Ниже выберите фото или логотипы организаций помощников ("Это поле необязательно к заполнению)', blank=False, verbose_name='Подсказка')
    image_1 = models.ImageField(default=None, verbose_name='Фото организации')
    image_2 = models.ImageField(default=None, verbose_name='Фото организации')
    
    def __str__(self) -> str:
        return self.litle_title
    
    class Meta:
        verbose_name = "7) Седьмой раздел-Помошники в организации курсов"
        verbose_name_plural = "7) Седьмой раздел-Помошники в организации курсов"

class Eighth_title(models.Model):   
    url_1 = models.CharField(max_length=100, verbose_name='Ссылки навигации №1', blank=True)
    url_2 = models.CharField(max_length=100, verbose_name='Ссылки навигации №2', blank=True)
    url_3 = models.CharField(max_length=100, verbose_name='Ссылки навигации №3', blank=True)

    class Meta:
        verbose_name = "8) Восьмой раздел-Ссылки навигации"
        verbose_name_plural = "8) Восьмой раздел-Ссылки навигации"
    
    def str(self):
        return f'{self.url_1} {self.url_2} {self.url_3}'

class Footer(models.Model):
    main_title = models.CharField(max_length=50, null=False, blank=False, verbose_name='Главный заголовок')
    url_1 = models.URLField(verbose_name='Первый сайт')
    url_2 = models.URLField(verbose_name='Второй сайт')
    url_3 = models.URLField(verbose_name='Третий сайт')
    
    def __str__(self) -> str:
        return self.main_title
    
    class Meta:
        verbose_name = "9) Футер сайта"
        verbose_name_plural = "9) Футер сайта"


