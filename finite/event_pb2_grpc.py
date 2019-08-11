# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import event_pb2 as event__pb2


class EventStoreStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Status = channel.unary_unary(
        '/finite.EventStore/Status',
        request_serializer=event__pb2.Ping.SerializeToString,
        response_deserializer=event__pb2.Pong.FromString,
        )
    self.ListMachines = channel.unary_unary(
        '/finite.EventStore/ListMachines',
        request_serializer=event__pb2.MachineQuery.SerializeToString,
        response_deserializer=event__pb2.MachineList.FromString,
        )
    self.GetMachine = channel.unary_unary(
        '/finite.EventStore/GetMachine',
        request_serializer=event__pb2.Query.SerializeToString,
        response_deserializer=event__pb2.Machine.FromString,
        )
    self.GetPlaceMap = channel.unary_unary(
        '/finite.EventStore/GetPlaceMap',
        request_serializer=event__pb2.Query.SerializeToString,
        response_deserializer=event__pb2.PlaceMap.FromString,
        )
    self.Dispatch = channel.unary_unary(
        '/finite.EventStore/Dispatch',
        request_serializer=event__pb2.Command.SerializeToString,
        response_deserializer=event__pb2.EventStatus.FromString,
        )
    self.GetEvent = channel.unary_unary(
        '/finite.EventStore/GetEvent',
        request_serializer=event__pb2.Query.SerializeToString,
        response_deserializer=event__pb2.EventList.FromString,
        )
    self.GetState = channel.unary_unary(
        '/finite.EventStore/GetState',
        request_serializer=event__pb2.Query.SerializeToString,
        response_deserializer=event__pb2.StateList.FromString,
        )


class EventStoreServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def Status(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ListMachines(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetMachine(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetPlaceMap(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Dispatch(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetEvent(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetState(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_EventStoreServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Status': grpc.unary_unary_rpc_method_handler(
          servicer.Status,
          request_deserializer=event__pb2.Ping.FromString,
          response_serializer=event__pb2.Pong.SerializeToString,
      ),
      'ListMachines': grpc.unary_unary_rpc_method_handler(
          servicer.ListMachines,
          request_deserializer=event__pb2.MachineQuery.FromString,
          response_serializer=event__pb2.MachineList.SerializeToString,
      ),
      'GetMachine': grpc.unary_unary_rpc_method_handler(
          servicer.GetMachine,
          request_deserializer=event__pb2.Query.FromString,
          response_serializer=event__pb2.Machine.SerializeToString,
      ),
      'GetPlaceMap': grpc.unary_unary_rpc_method_handler(
          servicer.GetPlaceMap,
          request_deserializer=event__pb2.Query.FromString,
          response_serializer=event__pb2.PlaceMap.SerializeToString,
      ),
      'Dispatch': grpc.unary_unary_rpc_method_handler(
          servicer.Dispatch,
          request_deserializer=event__pb2.Command.FromString,
          response_serializer=event__pb2.EventStatus.SerializeToString,
      ),
      'GetEvent': grpc.unary_unary_rpc_method_handler(
          servicer.GetEvent,
          request_deserializer=event__pb2.Query.FromString,
          response_serializer=event__pb2.EventList.SerializeToString,
      ),
      'GetState': grpc.unary_unary_rpc_method_handler(
          servicer.GetState,
          request_deserializer=event__pb2.Query.FromString,
          response_serializer=event__pb2.StateList.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'finite.EventStore', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
