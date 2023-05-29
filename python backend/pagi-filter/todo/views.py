from rest_framework.viewsets import ModelViewSet
from .serializers import Todo, TodoSerializer

# Alternatif geçici yöntem:
# from rest_framework.pagination import PageNumberPagination


from .paginations import (
    CustomPageNumberPagination,
    CustomLimitOffsetPagination,
    CustomCursorPagination
)

class TodoView(ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    pagination_class = CustomPageNumberPagination # Local Setting.

    # Alternatif (sadece bu class için çalışan) yöntem:
    # pagination_class = PageNumberPagination
    # PageNumberPagination.page_size = 25
    # PageNumberPagination.page_size_query_param = 'adet' # URL ile kaç adet gösterileceğini belirleyebilirim
    # PageNumberPagination.page_query_param = 'sayfa' # aktif sayfa numarası için "page" yerinde başka bir isim kullanabilirim.

    # Override:
    def get_queryset(self):
        # URL'den parametre değerini yakala:
        title = self.request.query_params.get('title')
        if title is None:
        # Arama yapma (parametre yok)
            return super().get_queryset()
        else:
        # Arama yap:
            # queryset içinde ara:
            return self.queryset.filter(title__contains=title)