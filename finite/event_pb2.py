# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: event.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='event.proto',
  package='finite',
  syntax='proto3',
  serialized_options=_b('\n\037com.project.factom.finite.eventB\nEventProtoP\001'),
  serialized_pb=_b('\n\x0b\x65vent.proto\x12\x06\x66inite\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x19google/protobuf/any.proto\"\x1b\n\x0bJsonPayload\x12\x0c\n\x04json\x18\x01 \x01(\x0c\"\x0e\n\x0cMachineQuery\"\x15\n\x04Ping\x12\r\n\x05nonce\x18\x01 \x01(\t\"#\n\x04Pong\x12\r\n\x05nonce\x18\x01 \x01(\t\x12\x0c\n\x04\x63ode\x18\x02 \x01(\x03\"1\n\x05Query\x12\x0e\n\x06schema\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\t\x12\x0c\n\x04uuid\x18\x03 \x01(\t\"(\n\tEventList\x12\x1b\n\x04list\x18\x01 \x03(\x0b\x32\r.finite.Event\"(\n\tStateList\x12\x1b\n\x04list\x18\x01 \x03(\x0b\x32\r.finite.State\"*\n\x06\x41\x63tion\x12\x0e\n\x06\x61\x63tion\x18\x01 \x01(\t\x12\x10\n\x08multiple\x18\x02 \x01(\x04\"u\n\x07\x43ommand\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0e\n\x06schema\x18\x02 \x01(\t\x12\r\n\x05\x63hain\x18\x03 \x01(\t\x12\x1e\n\x06\x61\x63tion\x18\x04 \x03(\x0b\x32\x0e.finite.Action\x12\x10\n\x08multiple\x18\x05 \x01(\x04\x12\r\n\x05state\x18\x06 \x03(\x04\"\xa9\x01\n\x05State\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0e\n\x06schema\x18\x02 \x01(\t\x12\r\n\x05\x63hain\x18\x03 \x01(\t\x12\r\n\x05state\x18\x04 \x03(\x04\x12\x0c\n\x04head\x18\x05 \x01(\t\x12+\n\x07\x63reated\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12+\n\x07updated\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"J\n\x0b\x45ventStatus\x12\x1c\n\x05state\x18\x01 \x01(\x0b\x32\r.finite.State\x12\x0c\n\x04\x63ode\x18\x02 \x01(\x03\x12\x0f\n\x07message\x18\x03 \x01(\t\"\xce\x01\n\x05\x45vent\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0e\n\x06schema\x18\x02 \x01(\t\x12\r\n\x05\x63hain\x18\x03 \x01(\t\x12\x1e\n\x06\x61\x63tion\x18\x04 \x03(\x0b\x32\x0e.finite.Action\x12%\n\x07payload\x18\x05 \x01(\x0b\x32\x14.google.protobuf.Any\x12\r\n\x05state\x18\x06 \x03(\x04\x12&\n\x02ts\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0c\n\x04uuid\x18\x08 \x01(\t\x12\x0e\n\x06parent\x18\t \x01(\t\"\x16\n\x05Guard\x12\r\n\x05\x64\x65lta\x18\x01 \x03(\x03\"\x97\x01\n\nTransition\x12\r\n\x05\x64\x65lta\x18\x01 \x03(\x03\x12\x0c\n\x04role\x18\x02 \x01(\t\x12.\n\x06guards\x18\x03 \x03(\x0b\x32\x1e.finite.Transition.GuardsEntry\x1a<\n\x0bGuardsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x1c\n\x05value\x18\x02 \x01(\x0b\x32\r.finite.Guard:\x02\x38\x01\"\x1a\n\x08Schemata\x12\x0e\n\x06schema\x18\x01 \x03(\t\"\xbb\x01\n\x07Machine\x12\x0e\n\x06schema\x18\x01 \x01(\t\x12\x0f\n\x07initial\x18\x02 \x03(\x04\x12\x10\n\x08\x63\x61pacity\x18\x03 \x03(\x04\x12\x35\n\x0btransitions\x18\x04 \x03(\x0b\x32 .finite.Machine.TransitionsEntry\x1a\x46\n\x10TransitionsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12!\n\x05value\x18\x02 \x01(\x0b\x32\x12.finite.Transition:\x02\x38\x01\"\x1b\n\x0bMachineList\x12\x0c\n\x04list\x18\x01 \x03(\t2\xb5\x02\n\nEventStore\x12&\n\x06Status\x12\x0c.finite.Ping\x1a\x0c.finite.Pong\"\x00\x12;\n\x0cListMachines\x12\x14.finite.MachineQuery\x1a\x13.finite.MachineList\"\x00\x12.\n\nGetMachine\x12\r.finite.Query\x1a\x0f.finite.Machine\"\x00\x12\x32\n\x08\x44ispatch\x12\x0f.finite.Command\x1a\x13.finite.EventStatus\"\x00\x12.\n\x08GetEvent\x12\r.finite.Query\x1a\x11.finite.EventList\"\x00\x12.\n\x08GetState\x12\r.finite.Query\x1a\x11.finite.StateList\"\x00\x42/\n\x1f\x63om.project.factom.finite.eventB\nEventProtoP\x01\x62\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,google_dot_protobuf_dot_any__pb2.DESCRIPTOR,])




_JSONPAYLOAD = _descriptor.Descriptor(
  name='JsonPayload',
  full_name='finite.JsonPayload',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='json', full_name='finite.JsonPayload.json', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=83,
  serialized_end=110,
)


_MACHINEQUERY = _descriptor.Descriptor(
  name='MachineQuery',
  full_name='finite.MachineQuery',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=112,
  serialized_end=126,
)


_PING = _descriptor.Descriptor(
  name='Ping',
  full_name='finite.Ping',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='nonce', full_name='finite.Ping.nonce', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=128,
  serialized_end=149,
)


_PONG = _descriptor.Descriptor(
  name='Pong',
  full_name='finite.Pong',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='nonce', full_name='finite.Pong.nonce', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='code', full_name='finite.Pong.code', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=151,
  serialized_end=186,
)


_QUERY = _descriptor.Descriptor(
  name='Query',
  full_name='finite.Query',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='schema', full_name='finite.Query.schema', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='id', full_name='finite.Query.id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='uuid', full_name='finite.Query.uuid', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=188,
  serialized_end=237,
)


_EVENTLIST = _descriptor.Descriptor(
  name='EventList',
  full_name='finite.EventList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='list', full_name='finite.EventList.list', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=239,
  serialized_end=279,
)


_STATELIST = _descriptor.Descriptor(
  name='StateList',
  full_name='finite.StateList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='list', full_name='finite.StateList.list', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=281,
  serialized_end=321,
)


_ACTION = _descriptor.Descriptor(
  name='Action',
  full_name='finite.Action',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='action', full_name='finite.Action.action', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='multiple', full_name='finite.Action.multiple', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=323,
  serialized_end=365,
)


_COMMAND = _descriptor.Descriptor(
  name='Command',
  full_name='finite.Command',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='finite.Command.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='schema', full_name='finite.Command.schema', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='chain', full_name='finite.Command.chain', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='action', full_name='finite.Command.action', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='multiple', full_name='finite.Command.multiple', index=4,
      number=5, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='state', full_name='finite.Command.state', index=5,
      number=6, type=4, cpp_type=4, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=367,
  serialized_end=484,
)


_STATE = _descriptor.Descriptor(
  name='State',
  full_name='finite.State',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='finite.State.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='schema', full_name='finite.State.schema', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='chain', full_name='finite.State.chain', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='state', full_name='finite.State.state', index=3,
      number=4, type=4, cpp_type=4, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='head', full_name='finite.State.head', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='created', full_name='finite.State.created', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='updated', full_name='finite.State.updated', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=487,
  serialized_end=656,
)


_EVENTSTATUS = _descriptor.Descriptor(
  name='EventStatus',
  full_name='finite.EventStatus',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='state', full_name='finite.EventStatus.state', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='code', full_name='finite.EventStatus.code', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='message', full_name='finite.EventStatus.message', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=658,
  serialized_end=732,
)


_EVENT = _descriptor.Descriptor(
  name='Event',
  full_name='finite.Event',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='finite.Event.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='schema', full_name='finite.Event.schema', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='chain', full_name='finite.Event.chain', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='action', full_name='finite.Event.action', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='payload', full_name='finite.Event.payload', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='state', full_name='finite.Event.state', index=5,
      number=6, type=4, cpp_type=4, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ts', full_name='finite.Event.ts', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='uuid', full_name='finite.Event.uuid', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='parent', full_name='finite.Event.parent', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=735,
  serialized_end=941,
)


_GUARD = _descriptor.Descriptor(
  name='Guard',
  full_name='finite.Guard',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='delta', full_name='finite.Guard.delta', index=0,
      number=1, type=3, cpp_type=2, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=943,
  serialized_end=965,
)


_TRANSITION_GUARDSENTRY = _descriptor.Descriptor(
  name='GuardsEntry',
  full_name='finite.Transition.GuardsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='finite.Transition.GuardsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='finite.Transition.GuardsEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1059,
  serialized_end=1119,
)

_TRANSITION = _descriptor.Descriptor(
  name='Transition',
  full_name='finite.Transition',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='delta', full_name='finite.Transition.delta', index=0,
      number=1, type=3, cpp_type=2, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='role', full_name='finite.Transition.role', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='guards', full_name='finite.Transition.guards', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_TRANSITION_GUARDSENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=968,
  serialized_end=1119,
)


_SCHEMATA = _descriptor.Descriptor(
  name='Schemata',
  full_name='finite.Schemata',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='schema', full_name='finite.Schemata.schema', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1121,
  serialized_end=1147,
)


_MACHINE_TRANSITIONSENTRY = _descriptor.Descriptor(
  name='TransitionsEntry',
  full_name='finite.Machine.TransitionsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='finite.Machine.TransitionsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='finite.Machine.TransitionsEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1267,
  serialized_end=1337,
)

_MACHINE = _descriptor.Descriptor(
  name='Machine',
  full_name='finite.Machine',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='schema', full_name='finite.Machine.schema', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='initial', full_name='finite.Machine.initial', index=1,
      number=2, type=4, cpp_type=4, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='capacity', full_name='finite.Machine.capacity', index=2,
      number=3, type=4, cpp_type=4, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='transitions', full_name='finite.Machine.transitions', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_MACHINE_TRANSITIONSENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1150,
  serialized_end=1337,
)


_MACHINELIST = _descriptor.Descriptor(
  name='MachineList',
  full_name='finite.MachineList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='list', full_name='finite.MachineList.list', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1339,
  serialized_end=1366,
)

_EVENTLIST.fields_by_name['list'].message_type = _EVENT
_STATELIST.fields_by_name['list'].message_type = _STATE
_COMMAND.fields_by_name['action'].message_type = _ACTION
_STATE.fields_by_name['created'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_STATE.fields_by_name['updated'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_EVENTSTATUS.fields_by_name['state'].message_type = _STATE
_EVENT.fields_by_name['action'].message_type = _ACTION
_EVENT.fields_by_name['payload'].message_type = google_dot_protobuf_dot_any__pb2._ANY
_EVENT.fields_by_name['ts'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_TRANSITION_GUARDSENTRY.fields_by_name['value'].message_type = _GUARD
_TRANSITION_GUARDSENTRY.containing_type = _TRANSITION
_TRANSITION.fields_by_name['guards'].message_type = _TRANSITION_GUARDSENTRY
_MACHINE_TRANSITIONSENTRY.fields_by_name['value'].message_type = _TRANSITION
_MACHINE_TRANSITIONSENTRY.containing_type = _MACHINE
_MACHINE.fields_by_name['transitions'].message_type = _MACHINE_TRANSITIONSENTRY
DESCRIPTOR.message_types_by_name['JsonPayload'] = _JSONPAYLOAD
DESCRIPTOR.message_types_by_name['MachineQuery'] = _MACHINEQUERY
DESCRIPTOR.message_types_by_name['Ping'] = _PING
DESCRIPTOR.message_types_by_name['Pong'] = _PONG
DESCRIPTOR.message_types_by_name['Query'] = _QUERY
DESCRIPTOR.message_types_by_name['EventList'] = _EVENTLIST
DESCRIPTOR.message_types_by_name['StateList'] = _STATELIST
DESCRIPTOR.message_types_by_name['Action'] = _ACTION
DESCRIPTOR.message_types_by_name['Command'] = _COMMAND
DESCRIPTOR.message_types_by_name['State'] = _STATE
DESCRIPTOR.message_types_by_name['EventStatus'] = _EVENTSTATUS
DESCRIPTOR.message_types_by_name['Event'] = _EVENT
DESCRIPTOR.message_types_by_name['Guard'] = _GUARD
DESCRIPTOR.message_types_by_name['Transition'] = _TRANSITION
DESCRIPTOR.message_types_by_name['Schemata'] = _SCHEMATA
DESCRIPTOR.message_types_by_name['Machine'] = _MACHINE
DESCRIPTOR.message_types_by_name['MachineList'] = _MACHINELIST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

JsonPayload = _reflection.GeneratedProtocolMessageType('JsonPayload', (_message.Message,), {
  'DESCRIPTOR' : _JSONPAYLOAD,
  '__module__' : 'event_pb2'
  # @@protoc_insertion_point(class_scope:finite.JsonPayload)
  })
_sym_db.RegisterMessage(JsonPayload)

MachineQuery = _reflection.GeneratedProtocolMessageType('MachineQuery', (_message.Message,), {
  'DESCRIPTOR' : _MACHINEQUERY,
  '__module__' : 'event_pb2'
  # @@protoc_insertion_point(class_scope:finite.MachineQuery)
  })
_sym_db.RegisterMessage(MachineQuery)

Ping = _reflection.GeneratedProtocolMessageType('Ping', (_message.Message,), {
  'DESCRIPTOR' : _PING,
  '__module__' : 'event_pb2'
  # @@protoc_insertion_point(class_scope:finite.Ping)
  })
_sym_db.RegisterMessage(Ping)

Pong = _reflection.GeneratedProtocolMessageType('Pong', (_message.Message,), {
  'DESCRIPTOR' : _PONG,
  '__module__' : 'event_pb2'
  # @@protoc_insertion_point(class_scope:finite.Pong)
  })
_sym_db.RegisterMessage(Pong)

Query = _reflection.GeneratedProtocolMessageType('Query', (_message.Message,), {
  'DESCRIPTOR' : _QUERY,
  '__module__' : 'event_pb2'
  # @@protoc_insertion_point(class_scope:finite.Query)
  })
_sym_db.RegisterMessage(Query)

EventList = _reflection.GeneratedProtocolMessageType('EventList', (_message.Message,), {
  'DESCRIPTOR' : _EVENTLIST,
  '__module__' : 'event_pb2'
  # @@protoc_insertion_point(class_scope:finite.EventList)
  })
_sym_db.RegisterMessage(EventList)

StateList = _reflection.GeneratedProtocolMessageType('StateList', (_message.Message,), {
  'DESCRIPTOR' : _STATELIST,
  '__module__' : 'event_pb2'
  # @@protoc_insertion_point(class_scope:finite.StateList)
  })
_sym_db.RegisterMessage(StateList)

Action = _reflection.GeneratedProtocolMessageType('Action', (_message.Message,), {
  'DESCRIPTOR' : _ACTION,
  '__module__' : 'event_pb2'
  # @@protoc_insertion_point(class_scope:finite.Action)
  })
_sym_db.RegisterMessage(Action)

Command = _reflection.GeneratedProtocolMessageType('Command', (_message.Message,), {
  'DESCRIPTOR' : _COMMAND,
  '__module__' : 'event_pb2'
  # @@protoc_insertion_point(class_scope:finite.Command)
  })
_sym_db.RegisterMessage(Command)

State = _reflection.GeneratedProtocolMessageType('State', (_message.Message,), {
  'DESCRIPTOR' : _STATE,
  '__module__' : 'event_pb2'
  # @@protoc_insertion_point(class_scope:finite.State)
  })
_sym_db.RegisterMessage(State)

EventStatus = _reflection.GeneratedProtocolMessageType('EventStatus', (_message.Message,), {
  'DESCRIPTOR' : _EVENTSTATUS,
  '__module__' : 'event_pb2'
  # @@protoc_insertion_point(class_scope:finite.EventStatus)
  })
_sym_db.RegisterMessage(EventStatus)

Event = _reflection.GeneratedProtocolMessageType('Event', (_message.Message,), {
  'DESCRIPTOR' : _EVENT,
  '__module__' : 'event_pb2'
  # @@protoc_insertion_point(class_scope:finite.Event)
  })
_sym_db.RegisterMessage(Event)

Guard = _reflection.GeneratedProtocolMessageType('Guard', (_message.Message,), {
  'DESCRIPTOR' : _GUARD,
  '__module__' : 'event_pb2'
  # @@protoc_insertion_point(class_scope:finite.Guard)
  })
_sym_db.RegisterMessage(Guard)

Transition = _reflection.GeneratedProtocolMessageType('Transition', (_message.Message,), {

  'GuardsEntry' : _reflection.GeneratedProtocolMessageType('GuardsEntry', (_message.Message,), {
    'DESCRIPTOR' : _TRANSITION_GUARDSENTRY,
    '__module__' : 'event_pb2'
    # @@protoc_insertion_point(class_scope:finite.Transition.GuardsEntry)
    })
  ,
  'DESCRIPTOR' : _TRANSITION,
  '__module__' : 'event_pb2'
  # @@protoc_insertion_point(class_scope:finite.Transition)
  })
_sym_db.RegisterMessage(Transition)
_sym_db.RegisterMessage(Transition.GuardsEntry)

Schemata = _reflection.GeneratedProtocolMessageType('Schemata', (_message.Message,), {
  'DESCRIPTOR' : _SCHEMATA,
  '__module__' : 'event_pb2'
  # @@protoc_insertion_point(class_scope:finite.Schemata)
  })
_sym_db.RegisterMessage(Schemata)

Machine = _reflection.GeneratedProtocolMessageType('Machine', (_message.Message,), {

  'TransitionsEntry' : _reflection.GeneratedProtocolMessageType('TransitionsEntry', (_message.Message,), {
    'DESCRIPTOR' : _MACHINE_TRANSITIONSENTRY,
    '__module__' : 'event_pb2'
    # @@protoc_insertion_point(class_scope:finite.Machine.TransitionsEntry)
    })
  ,
  'DESCRIPTOR' : _MACHINE,
  '__module__' : 'event_pb2'
  # @@protoc_insertion_point(class_scope:finite.Machine)
  })
_sym_db.RegisterMessage(Machine)
_sym_db.RegisterMessage(Machine.TransitionsEntry)

MachineList = _reflection.GeneratedProtocolMessageType('MachineList', (_message.Message,), {
  'DESCRIPTOR' : _MACHINELIST,
  '__module__' : 'event_pb2'
  # @@protoc_insertion_point(class_scope:finite.MachineList)
  })
_sym_db.RegisterMessage(MachineList)


DESCRIPTOR._options = None
_TRANSITION_GUARDSENTRY._options = None
_MACHINE_TRANSITIONSENTRY._options = None

_EVENTSTORE = _descriptor.ServiceDescriptor(
  name='EventStore',
  full_name='finite.EventStore',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=1369,
  serialized_end=1678,
  methods=[
  _descriptor.MethodDescriptor(
    name='Status',
    full_name='finite.EventStore.Status',
    index=0,
    containing_service=None,
    input_type=_PING,
    output_type=_PONG,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='ListMachines',
    full_name='finite.EventStore.ListMachines',
    index=1,
    containing_service=None,
    input_type=_MACHINEQUERY,
    output_type=_MACHINELIST,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetMachine',
    full_name='finite.EventStore.GetMachine',
    index=2,
    containing_service=None,
    input_type=_QUERY,
    output_type=_MACHINE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Dispatch',
    full_name='finite.EventStore.Dispatch',
    index=3,
    containing_service=None,
    input_type=_COMMAND,
    output_type=_EVENTSTATUS,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetEvent',
    full_name='finite.EventStore.GetEvent',
    index=4,
    containing_service=None,
    input_type=_QUERY,
    output_type=_EVENTLIST,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetState',
    full_name='finite.EventStore.GetState',
    index=5,
    containing_service=None,
    input_type=_QUERY,
    output_type=_STATELIST,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_EVENTSTORE)

DESCRIPTOR.services_by_name['EventStore'] = _EVENTSTORE

# @@protoc_insertion_point(module_scope)
