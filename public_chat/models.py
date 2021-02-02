from django.db import models
from django.conf import settings

# Create your models here.
class PublicChatRoom(models.Model):

    title = models.CharField(max_length=255,unique=True, blank=False,)
    users = models.ManyToManyField(settings.AUTH_USER_MODEL, help_text='useres who are online in chat', blank=True)

    def __str__(self):
        return self.title
    
    def connect_user(self,user):
        is_user_added = False
        if not user in self.users.all():
            self.users.add(user)
            self.save()
            is_user_added = True
        elif user in self.users.all():
            is_user_added = True
        return is_user_added
    
    def disconnect_user(self,user):
        is_user_removed = False
        if user in self.users.all():
            self.users.remove(user)
            self.save()
            is_user_removed = True
        return is_user_removed

    @property
    def group_name(self):
        # used in sockets and notifications
        return f"publicChatRoom-{self.id}"

class PublicRoomChatMessageManager(models.Manager):
    def by_room(self,room):
        sort = PublicRoomChatMessage.object.filter(room=room).order_by("-timestamp")
        return sort

class PublicRoomChatMessage(models.Model):
    #individual messages in the chat
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    room = models.ForeignKey(PublicChatRoom, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField(unique=False,blank=False)

    def __str__(self):
        return self.content