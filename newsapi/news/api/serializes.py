from rest_framework import serializers
from news.models import Article

class ArticleSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    author = serializers.CharField()
    title = serializers.CharField()
    description = serializers.CharField()
    body = serializers.CharField()
    location = serializers.CharField()
    publication_date = serializers.DateField()
    active = serializers.BooleanField()
    created_at = serializers.DateTimeField(read_only=True)
    updeted_at = serializers.DateTimeField(read_only=True)
    
    def create(self, validation_data):
        # print(validation_data)
        return Article.objects.create(**validation_data)

    def update(self, instance, validation_data):
        instance.author = validation_data.get('author', instance.author)
        instance.title = validation_data.get('title', instance.title)
        instance.body = validation_data.get('body', instance.bodycd )
        instance.description = validation_data.get('description', instance.description)
        instance.location = validation_data.get('location', instance.location)
        instance.publication_date = validation_data.get('publication_date', instance.publication_date)
        instance.active = validation_data.get('active', instance.active)
        instance.save()
        return instance
