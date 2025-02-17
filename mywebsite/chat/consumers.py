import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync

class ChatConsumer(WebsocketConsumer):
    # ------from the initial request of the client----------
    def connect(self):
        self.room_group_name = 'test'
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        # send message back about conection
        self.accept()

        

    #--- listening messages from chat room (Client)
    def receive(self, text_data):
        text_data_jeson = json.loads(text_data)
        message = text_data_jeson['message']

        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type':'chat_message',
                'message':message
            }
        )
        #---------------------------------------------------
        # print('Message:', message)
        # # --- send to the client -----
        # self.send(text_data=json.dumps({
        #     'type':'chat',
        #     'message':message
        # }))

    def chat_message(self, event):
        message = event['message']

        self.send(text_data=json.dumps({
            'type':'chat',
            'message':message
        }))


    def disconnect(self, close_code):
        pass
