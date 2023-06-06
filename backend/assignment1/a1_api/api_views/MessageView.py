from ..api_views.__init__ import *
from ..serializers import MessageModelSerializer
from ..models import Message


class MessageView(ListCreateAPIView):
    serializer_class = MessageModelSerializer

    def get_queryset(self):
        page_size = int(self.request.query_params.get('size', 15))
        return Message.objects.all().order_by('-id')[0:page_size]

