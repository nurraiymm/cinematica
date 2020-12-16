from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Category, Genre, Movie, MovieShots, Actor, RatingStar, Rating, Reviews


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('name',)


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'category')
    list_filter = ('category', 'year')
    search_fields = ('title', 'category__name')
    # fields = (('actors', 'directors', 'genres'),)
    fieldsets = (
        (None, {
            'fields': (('title', 'tagline'),)
        }),
        (None, {
            'fields': ('description', 'poster', 'movie_url')
        }),
        ('Actors', {
            'classes': ('collapse',),
            'fields': (('year', 'country', 'url'),)
        }),
        (None, {
            'fields': (('actors', 'directors', 'genres', 'category'),)
        }),

    )


@admin.register(Reviews)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'parent', 'movie')
    readonly_fields = ('name', 'email')


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name', 'url')


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'get_image')

    def get_image(self, obj):
        return mark_safe(f"<img src ={obj.image.url} width='80', height='60'")

    get_image.short_description = 'изображение'


@admin.register(MovieShots)
class MovieShotsAdmin(admin.ModelAdmin):
    list_display = ('title', 'movie')


admin.site.register(RatingStar)
admin.site.register(Rating)
