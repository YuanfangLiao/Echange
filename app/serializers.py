from rest_framework import serializers

from app.models import Book


class PublisherSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=32)


class AuthorSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=32)

    # class BookSerializer(serializers.Serializer):
    #     id = serializers.IntegerField(required=False)  # 反序列化的时候不必要
    #     title = serializers.CharField(max_length=32)
    #     pub_time = serializers.DateField()
    #
    #     category = serializers.CharField(source="get_category_display", read_only=True)
    #     post_category = serializers.IntegerField(write_only=True)
    #
    #     publisher = PublisherSerializer(read_only=True)
    #     post_publisher_id = serializers.IntegerField(write_only=True)
    #
    #     authors = AuthorSerializer(many=True, read_only=True)
    #     post_authors_list = serializers.ListField(write_only=True)
    #
    #     def create(self, validated_data):
    #         # validated_data 是校验通过的数据 就是book_obj
    #         # 通过ORM操作给book表增加数据
    #         book_obj = Book.objects.create(title=validated_data['title'], pub_time=validated_data['pub_time'],
    #                                        category=validated_data['post_category'],
    #                                        publisher_id=validated_data['post_publisher_id'],
    #                                        )
    #         book_obj.authors.add(*validated_data['post_authors_list'])
    #         return book_obj

    def update(self, instance, validated_data):
        ...

    def validate_title(self, value):
        ...

    def validate(self, attrs):
        ...


class BookSerializer(serializers.ModelSerializer):
    publisher = serializers.SerializerMethodField()
    authors = serializers.SerializerMethodField()

    def get_authors(self, obj):
        authors_queryset = obj.authors.all()
        return [{"id": author.id, "name": author.name} for author in authors_queryset]

    def get_publisher(self, obj):
        publisher_obj = obj.publisher
        return {"id": publisher_obj.id, "title": publisher_obj.title}

    class Meta:
        model = Book
        fields = "__all__"
        extra_kwargs = {"publisher": {"write_only": True}, "authors": {"write_only": True}}
