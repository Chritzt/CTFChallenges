import os
from concurrent import futures
import grpc
from grpc_reflection.v1alpha import reflection
import challenge_pb2
import challenge_pb2_grpc

FLAG = os.getenv("FLAG", "CLA{dummy_flag}")

class UserService(challenge_pb2_grpc.UserServiceServicer):
    def GetStatus(self, request, context):
        return challenge_pb2.StatusResponse(
            message=f"Welcome {request.username}! NanoCorp API v2.1 is fully operational."
        )

class MagicMirrorService(challenge_pb2_grpc.MagicMirrorServiceServicer):
    def RevealSecret(self, request, context):
        if request.question and "who is the fairest of them all" in request.question.lower():
            return challenge_pb2.SecretResponse(flag=f"You are! And here is your reward: {FLAG}")
        else:
            return challenge_pb2.SecretResponse(flag="The mirror remains silent. Ask the right question!")

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    
    challenge_pb2_grpc.add_UserServiceServicer_to_server(UserService(), server)
    challenge_pb2_grpc.add_MagicMirrorServiceServicer_to_server(MagicMirrorService(), server)
    
    SERVICE_NAMES = (
        challenge_pb2.DESCRIPTOR.services_by_name['UserService'].full_name,
        challenge_pb2.DESCRIPTOR.services_by_name['MagicMirrorService'].full_name,
        reflection.SERVICE_NAME,
    )
    reflection.enable_server_reflection(SERVICE_NAMES, server)
    
    server.add_insecure_port('0.0.0.0:50051')
    print("[+] gRPC Python Server läuft stabil auf Port 50051")
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()