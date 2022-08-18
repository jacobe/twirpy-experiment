from twirp.asgi import TwirpASGIApp
from rpc.test.service_twirp import TestServiceServer
from twirp.exceptions import TwirpServerException
import twirp.errors
import rpc.test.service_pb2


class TestService():

    def ListTests(self, context, request):
        pass

    def GetTest(self, context, request):
        pass

    def CreateTest(self, context, request):
        return rpc.test.service_pb2.Test(id=1, name="test")

    def UpdateTest(self, context, request):
        pass

    def DeleteTest(self, context, request):
        raise TwirpServerException(code=twirp.errors.Errors.Unimplemented,
                                   message="Not implemented")


service = TestServiceServer(service=TestService())
app = TwirpASGIApp()
app.add_service(service)
