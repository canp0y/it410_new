{"filter":false,"title":"viewsets.py","tooltip":"/backend/api/viewsets.py","undoManager":{"mark":0,"position":0,"stack":[[{"start":{"row":0,"column":0},"end":{"row":8,"column":38},"action":"insert","lines":["","from rest_framework import viewsets","","from .models import Users","from .serializers import UsersSerializer","","class UsersViewSet(viewsets.ModelViewSet):","    queryset = Users.objects.all()","    serializer_class = UsersSerializer"],"id":1}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":8,"column":38},"end":{"row":8,"column":38},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1614666429221,"hash":"2e569f8f7d8aab7dbd40b9bce4e12424a14323a8"}