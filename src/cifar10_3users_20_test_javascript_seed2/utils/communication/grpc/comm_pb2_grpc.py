# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

import comm_pb2 as comm__pb2

GRPC_GENERATED_VERSION = '1.64.0'
GRPC_VERSION = grpc.__version__
EXPECTED_ERROR_RELEASE = '1.65.0'
SCHEDULED_RELEASE_DATE = 'June 25, 2024'
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    warnings.warn(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in comm_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
        + f' This warning will become an error in {EXPECTED_ERROR_RELEASE},'
        + f' scheduled for release on {SCHEDULED_RELEASE_DATE}.',
        RuntimeWarning
    )


class CommunicationServerStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.send_data = channel.unary_unary(
                '/CommunicationServer/send_data',
                request_serializer=comm__pb2.Data.SerializeToString,
                response_deserializer=comm__pb2.Empty.FromString,
                _registered_method=True)
        self.send_model = channel.unary_unary(
                '/CommunicationServer/send_model',
                request_serializer=comm__pb2.Model.SerializeToString,
                response_deserializer=comm__pb2.Empty.FromString,
                _registered_method=True)
        self.get_rank = channel.unary_unary(
                '/CommunicationServer/get_rank',
                request_serializer=comm__pb2.Empty.SerializeToString,
                response_deserializer=comm__pb2.Rank.FromString,
                _registered_method=True)
        self.get_model = channel.unary_unary(
                '/CommunicationServer/get_model',
                request_serializer=comm__pb2.Empty.SerializeToString,
                response_deserializer=comm__pb2.Model.FromString,
                _registered_method=True)
        self.get_current_round = channel.unary_unary(
                '/CommunicationServer/get_current_round',
                request_serializer=comm__pb2.Empty.SerializeToString,
                response_deserializer=comm__pb2.Round.FromString,
                _registered_method=True)
        self.update_port = channel.unary_unary(
                '/CommunicationServer/update_port',
                request_serializer=comm__pb2.PeerId.SerializeToString,
                response_deserializer=comm__pb2.Empty.FromString,
                _registered_method=True)
        self.send_peer_ids = channel.unary_unary(
                '/CommunicationServer/send_peer_ids',
                request_serializer=comm__pb2.PeerIds.SerializeToString,
                response_deserializer=comm__pb2.Empty.FromString,
                _registered_method=True)
        self.send_quorum = channel.unary_unary(
                '/CommunicationServer/send_quorum',
                request_serializer=comm__pb2.Quorum.SerializeToString,
                response_deserializer=comm__pb2.Empty.FromString,
                _registered_method=True)
        self.send_finished = channel.unary_unary(
                '/CommunicationServer/send_finished',
                request_serializer=comm__pb2.Rank.SerializeToString,
                response_deserializer=comm__pb2.Empty.FromString,
                _registered_method=True)


class CommunicationServerServicer(object):
    """Missing associated documentation comment in .proto file."""

    def send_data(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def send_model(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def get_rank(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def get_model(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def get_current_round(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def update_port(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def send_peer_ids(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def send_quorum(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def send_finished(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_CommunicationServerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'send_data': grpc.unary_unary_rpc_method_handler(
                    servicer.send_data,
                    request_deserializer=comm__pb2.Data.FromString,
                    response_serializer=comm__pb2.Empty.SerializeToString,
            ),
            'send_model': grpc.unary_unary_rpc_method_handler(
                    servicer.send_model,
                    request_deserializer=comm__pb2.Model.FromString,
                    response_serializer=comm__pb2.Empty.SerializeToString,
            ),
            'get_rank': grpc.unary_unary_rpc_method_handler(
                    servicer.get_rank,
                    request_deserializer=comm__pb2.Empty.FromString,
                    response_serializer=comm__pb2.Rank.SerializeToString,
            ),
            'get_model': grpc.unary_unary_rpc_method_handler(
                    servicer.get_model,
                    request_deserializer=comm__pb2.Empty.FromString,
                    response_serializer=comm__pb2.Model.SerializeToString,
            ),
            'get_current_round': grpc.unary_unary_rpc_method_handler(
                    servicer.get_current_round,
                    request_deserializer=comm__pb2.Empty.FromString,
                    response_serializer=comm__pb2.Round.SerializeToString,
            ),
            'update_port': grpc.unary_unary_rpc_method_handler(
                    servicer.update_port,
                    request_deserializer=comm__pb2.PeerId.FromString,
                    response_serializer=comm__pb2.Empty.SerializeToString,
            ),
            'send_peer_ids': grpc.unary_unary_rpc_method_handler(
                    servicer.send_peer_ids,
                    request_deserializer=comm__pb2.PeerIds.FromString,
                    response_serializer=comm__pb2.Empty.SerializeToString,
            ),
            'send_quorum': grpc.unary_unary_rpc_method_handler(
                    servicer.send_quorum,
                    request_deserializer=comm__pb2.Quorum.FromString,
                    response_serializer=comm__pb2.Empty.SerializeToString,
            ),
            'send_finished': grpc.unary_unary_rpc_method_handler(
                    servicer.send_finished,
                    request_deserializer=comm__pb2.Rank.FromString,
                    response_serializer=comm__pb2.Empty.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'CommunicationServer', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('CommunicationServer', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class CommunicationServer(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def send_data(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/CommunicationServer/send_data',
            comm__pb2.Data.SerializeToString,
            comm__pb2.Empty.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def send_model(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/CommunicationServer/send_model',
            comm__pb2.Model.SerializeToString,
            comm__pb2.Empty.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def get_rank(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/CommunicationServer/get_rank',
            comm__pb2.Empty.SerializeToString,
            comm__pb2.Rank.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def get_model(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/CommunicationServer/get_model',
            comm__pb2.Empty.SerializeToString,
            comm__pb2.Model.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def get_current_round(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/CommunicationServer/get_current_round',
            comm__pb2.Empty.SerializeToString,
            comm__pb2.Round.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def update_port(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/CommunicationServer/update_port',
            comm__pb2.PeerId.SerializeToString,
            comm__pb2.Empty.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def send_peer_ids(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/CommunicationServer/send_peer_ids',
            comm__pb2.PeerIds.SerializeToString,
            comm__pb2.Empty.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def send_quorum(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/CommunicationServer/send_quorum',
            comm__pb2.Quorum.SerializeToString,
            comm__pb2.Empty.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def send_finished(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/CommunicationServer/send_finished',
            comm__pb2.Rank.SerializeToString,
            comm__pb2.Empty.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
