# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: preconfig.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x0fpreconfig.proto\x12\x15yoshi.synth.preconfig"\x91\x01\n\tPreconfig\x12M\n\x0fprecloned_repos\x18\x01 \x03(\x0b\x32\x34.yoshi.synth.preconfig.Preconfig.PreclonedReposEntry\x1a\x35\n\x13PreclonedReposEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x62\x06proto3'
)


_PRECONFIG = DESCRIPTOR.message_types_by_name["Preconfig"]
_PRECONFIG_PRECLONEDREPOSENTRY = _PRECONFIG.nested_types_by_name["PreclonedReposEntry"]
Preconfig = _reflection.GeneratedProtocolMessageType(
    "Preconfig",
    (_message.Message,),
    {
        "PreclonedReposEntry": _reflection.GeneratedProtocolMessageType(
            "PreclonedReposEntry",
            (_message.Message,),
            {
                "DESCRIPTOR": _PRECONFIG_PRECLONEDREPOSENTRY,
                "__module__": "preconfig_pb2"
                # @@protoc_insertion_point(class_scope:yoshi.synth.preconfig.Preconfig.PreclonedReposEntry)
            },
        ),
        "DESCRIPTOR": _PRECONFIG,
        "__module__": "preconfig_pb2"
        # @@protoc_insertion_point(class_scope:yoshi.synth.preconfig.Preconfig)
    },
)
_sym_db.RegisterMessage(Preconfig)
_sym_db.RegisterMessage(Preconfig.PreclonedReposEntry)

if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _PRECONFIG_PRECLONEDREPOSENTRY._options = None
    _PRECONFIG_PRECLONEDREPOSENTRY._serialized_options = b"8\001"
    _PRECONFIG._serialized_start = 43
    _PRECONFIG._serialized_end = 188
    _PRECONFIG_PRECLONEDREPOSENTRY._serialized_start = 135
    _PRECONFIG_PRECLONEDREPOSENTRY._serialized_end = 188
# @@protoc_insertion_point(module_scope)
