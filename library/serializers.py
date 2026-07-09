from rest_framework import serializers
from .models import Book
from django.utils import timezone

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
        read_only_fields = ('created_at',)

    def validate_title(self, value):
        value = value.strip().title()
        if len(value) < 3:
            raise serializers.ValidationError("عنوان بایذ بیشتر از سه کاراکتر باشد. ")
        return value

    def validate_author(self, value):
        value = value.strip().title()
        return value

    def validate_price(self, value):
        if value < 0:
            raise serializers.ValidationError('قیمت باید بزرگ‌تر از صفر باشد. ')
        return value

    def validate_pages(self, value):
        if value <= 10:
            raise serializers.ValidationError('تعداد صفهات باید بیشتر از ده باشذ. ')
        return value

    def validate_published_year(self, value):
        current_year = timezone.now().year

        if value < 1900 or value > current_year:
            raise serializers.ValidationError(
                "سال انتشار نامعتبر است."
            )

        return value

    def validate(self, attrs):
        book_page = attrs.get('pages')
        book_is_available = attrs.get('is_available')

        if book_page > 0 and book_is_available is False:
            raise serializers.ValidationError('فبلد نامعتبر هست ')
        return attrs