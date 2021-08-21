# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import worker_pb2 as worker__pb2


class WorkerStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.setDriverPort = channel.unary_unary(
        '/workerPackage.Worker/setDriverPort',
        request_serializer=worker__pb2.driverPort.SerializeToString,
        response_deserializer=worker__pb2.status.FromString,
        )
    self.map = channel.unary_unary(
        '/workerPackage.Worker/map',
        request_serializer=worker__pb2.mapInput.SerializeToString,
        response_deserializer=worker__pb2.status.FromString,
        )
    self.reduce = channel.unary_unary(
        '/workerPackage.Worker/reduce',
        request_serializer=worker__pb2.rid.SerializeToString,
        response_deserializer=worker__pb2.status.FromString,
        )
    self.die = channel.unary_unary(
        '/workerPackage.Worker/die',
        request_serializer=worker__pb2.empty.SerializeToString,
        response_deserializer=worker__pb2.status.FromString,
        )
    self.nothing = channel.unary_unary(
        '/workerPackage.Worker/nothing',
        request_serializer=worker__pb2.empty.SerializeToString,
        response_deserializer=worker__pb2.empty.FromString,
        )


class WorkerServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def setDriverPort(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def map(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def reduce(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def die(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def nothing(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_WorkerServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'setDriverPort': grpc.unary_unary_rpc_method_handler(
          servicer.setDriverPort,
          request_deserializer=worker__pb2.driverPort.FromString,
          response_serializer=worker__pb2.status.SerializeToString,
      ),
      'map': grpc.unary_unary_rpc_method_handler(
          servicer.map,
          request_deserializer=worker__pb2.mapInput.FromString,
          response_serializer=worker__pb2.status.SerializeToString,
      ),
      'reduce': grpc.unary_unary_rpc_method_handler(
          servicer.reduce,
          request_deserializer=worker__pb2.rid.FromString,
          response_serializer=worker__pb2.status.SerializeToString,
      ),
      'die': grpc.unary_unary_rpc_method_handler(
          servicer.die,
          request_deserializer=worker__pb2.empty.FromString,
          response_serializer=worker__pb2.status.SerializeToString,
      ),
      'nothing': grpc.unary_unary_rpc_method_handler(
          servicer.nothing,
          request_deserializer=worker__pb2.empty.FromString,
          response_serializer=worker__pb2.empty.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'workerPackage.Worker', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
