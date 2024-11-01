from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
# from asgi app in core
from django.core.asgi import get_asgi_application
#import from chat app
import chat.routing

# use the converter of http to WS (analogy to urlpatterns)
application = ProtocolTypeRouter({
    'http':get_asgi_application(),
    'websocket':AuthMiddlewareStack(
        URLRouter(
            chat.routing.websocket_urlpatterns
        )

    )
})