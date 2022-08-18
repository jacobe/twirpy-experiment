from twirp.asgi import TwirpASGIApp
from rpc.test.service_twirp import TestServiceServer
from twirp.exceptions import TwirpServerException
import twirp.errors
import twirp.context
import rpc.test.service_pb2


class TestService:

    def ListTests(self, context: twirp.context.Context, request):
        pass

    def GetTest(self, context: twirp.context.Context, request):
        pass

    def CreateTest(self, context: twirp.context.Context, request):
        return rpc.test.service_pb2.Test(id=1, name="test")

    def UpdateTest(self, context: twirp.context.Context, request):
        pass

    def DeleteTest(self, context: twirp.context.Context, request):
        raise TwirpServerException(code=twirp.errors.Errors.Unimplemented,
                                   message="Not implemented")


async def authorize(context: twirp.context.Context, request: any, next):
    headers = context.get('raw_headers')
    auth = headers.get('authorization') if headers else None
    if not auth:
        raise TwirpServerException(code=twirp.errors.Errors.Unauthenticated,
                                   message="Missing Authorization header")

    return await next(context, request)


service = TestServiceServer(service=TestService())
app = TwirpASGIApp(authorize)
app.add_service(service)
