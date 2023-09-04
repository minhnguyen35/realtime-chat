from .models import Conversations, Messages, User_Conversations
from authentication.models import Users
class LoadConversations:
    def execute(self, email):
        try:
            user = Users.objects.filter(email=email)[0]
            allConversationsId = User_Conversations.objects.filter(user_email=user).values_list('conversation_id', flat=True)
            conversations = Conversations.objects.filter(id__in=allConversationsId)
            print(conversations)
            return conversations
        except Exception as e:
            print(e)
            return []
class LoadMessages:
    def execute(self, conversation_id):
        try:
            messages = Messages.objects.get(conversation_id=conversation_id)[:100]
            return messages
        except Exception as e:
            print(e)
            return []

class CreateNewConversation:
    def execute(self, user_email, room_name):
        try:
            conversation = Conversations(name=room_name)
            conversation.save()
            print('new conversation ', conversation)

            user = Users.objects.filter(email=user_email)[0]
            user_conversation = User_Conversations(user_email=user, conversation_id=conversation)
            user_conversation.save()
            return conversation.id
        except Exception as e:
            print(e)
            return None