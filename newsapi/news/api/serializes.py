from rest_framework import serializers
from news.models import Article,TourPack

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

class TourPackSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    description = serializers.CharField()
    price = serializers.CharField()
    tour_img = serializers.ImageField(read_only=True, )
    from_to = serializers.CharField()
    start_date = serializers.DateField()
    end_date = serializers.DateField()
    quantity = serializers.IntegerField()
    created_at = serializers.DateTimeField(read_only=True)
    updeted_at = serializers.DateTimeField(read_only=True)
    status = serializers.IntegerField()
    
    def create(self, validation_data):
        print(validation_data)
        return TourPack.objects.create(**validation_data)

    def update(self, instance, validation_data):
        instance.name = validation_data.get('name', instance.name)
        instance.description = validation_data.get('description', instance.title)
        instance.price = validation_data.get('price', instance.price)
        instance.tour_img = validation_data.get('tour_img', instance.tour_img )
        instance.from_to = validation_data.get('from_to', instance.from_to)
        instance.start_date = validation_data.get('start_date', instance.start_date)
        instance.end_date = validation_data.get('end_date', instance.end_date)
        instance.quantity = validation_data.get('quantity', instance.quantity)
        instance.status = validation_data.get('status', instance.status)
        instance.save()
        return instance