# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cosmos/mint/v1beta1/query.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from cosmos.mint.v1beta1 import mint_pb2 as cosmos_dot_mint_dot_v1beta1_dot_mint__pb2
from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2

DESCRIPTOR = _descriptor.FileDescriptor(
    name="cosmos/mint/v1beta1/query.proto",
    package="cosmos.mint.v1beta1",
    syntax="proto3",
    serialized_options=b"Z)github.com/cosmos/cosmos-sdk/x/mint/types",
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\n\x1f\x63osmos/mint/v1beta1/query.proto\x12\x13\x63osmos.mint.v1beta1\x1a\x14gogoproto/gogo.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x1e\x63osmos/mint/v1beta1/mint.proto"\x14\n\x12QueryParamsRequest"H\n\x13QueryParamsResponse\x12\x31\n\x06params\x18\x01 \x01(\x0b\x32\x1b.cosmos.mint.v1beta1.ParamsB\x04\xc8\xde\x1f\x00"\x17\n\x15QueryInflationRequest"[\n\x16QueryInflationResponse\x12\x41\n\tinflation\x18\x01 \x01(\x0c\x42.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00"\x1e\n\x1cQueryAnnualProvisionsRequest"j\n\x1dQueryAnnualProvisionsResponse\x12I\n\x11\x61nnual_provisions\x18\x01 \x01(\x0c\x42.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\x32\xc5\x03\n\x05Query\x12\x80\x01\n\x06Params\x12\'.cosmos.mint.v1beta1.QueryParamsRequest\x1a(.cosmos.mint.v1beta1.QueryParamsResponse"#\x82\xd3\xe4\x93\x02\x1d\x12\x1b/cosmos/mint/v1beta1/params\x12\x8c\x01\n\tInflation\x12*.cosmos.mint.v1beta1.QueryInflationRequest\x1a+.cosmos.mint.v1beta1.QueryInflationResponse"&\x82\xd3\xe4\x93\x02 \x12\x1e/cosmos/mint/v1beta1/inflation\x12\xa9\x01\n\x10\x41nnualProvisions\x12\x31.cosmos.mint.v1beta1.QueryAnnualProvisionsRequest\x1a\x32.cosmos.mint.v1beta1.QueryAnnualProvisionsResponse".\x82\xd3\xe4\x93\x02(\x12&/cosmos/mint/v1beta1/annual_provisionsB+Z)github.com/cosmos/cosmos-sdk/x/mint/typesb\x06proto3',
    dependencies=[
        gogoproto_dot_gogo__pb2.DESCRIPTOR,
        google_dot_api_dot_annotations__pb2.DESCRIPTOR,
        cosmos_dot_mint_dot_v1beta1_dot_mint__pb2.DESCRIPTOR,
    ],
)


_QUERYPARAMSREQUEST = _descriptor.Descriptor(
    name="QueryParamsRequest",
    full_name="cosmos.mint.v1beta1.QueryParamsRequest",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=140,
    serialized_end=160,
)


_QUERYPARAMSRESPONSE = _descriptor.Descriptor(
    name="QueryParamsResponse",
    full_name="cosmos.mint.v1beta1.QueryParamsResponse",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="params",
            full_name="cosmos.mint.v1beta1.QueryParamsResponse.params",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=b"\310\336\037\000",
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=162,
    serialized_end=234,
)


_QUERYINFLATIONREQUEST = _descriptor.Descriptor(
    name="QueryInflationRequest",
    full_name="cosmos.mint.v1beta1.QueryInflationRequest",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=236,
    serialized_end=259,
)


_QUERYINFLATIONRESPONSE = _descriptor.Descriptor(
    name="QueryInflationResponse",
    full_name="cosmos.mint.v1beta1.QueryInflationResponse",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="inflation",
            full_name="cosmos.mint.v1beta1.QueryInflationResponse.inflation",
            index=0,
            number=1,
            type=12,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"",
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=b"\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\310\336\037\000",
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=261,
    serialized_end=352,
)


_QUERYANNUALPROVISIONSREQUEST = _descriptor.Descriptor(
    name="QueryAnnualProvisionsRequest",
    full_name="cosmos.mint.v1beta1.QueryAnnualProvisionsRequest",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=354,
    serialized_end=384,
)


_QUERYANNUALPROVISIONSRESPONSE = _descriptor.Descriptor(
    name="QueryAnnualProvisionsResponse",
    full_name="cosmos.mint.v1beta1.QueryAnnualProvisionsResponse",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="annual_provisions",
            full_name="cosmos.mint.v1beta1.QueryAnnualProvisionsResponse.annual_provisions",
            index=0,
            number=1,
            type=12,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"",
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=b"\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\310\336\037\000",
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=386,
    serialized_end=492,
)

_QUERYPARAMSRESPONSE.fields_by_name[
    "params"
].message_type = cosmos_dot_mint_dot_v1beta1_dot_mint__pb2._PARAMS
DESCRIPTOR.message_types_by_name["QueryParamsRequest"] = _QUERYPARAMSREQUEST
DESCRIPTOR.message_types_by_name["QueryParamsResponse"] = _QUERYPARAMSRESPONSE
DESCRIPTOR.message_types_by_name["QueryInflationRequest"] = _QUERYINFLATIONREQUEST
DESCRIPTOR.message_types_by_name["QueryInflationResponse"] = _QUERYINFLATIONRESPONSE
DESCRIPTOR.message_types_by_name[
    "QueryAnnualProvisionsRequest"
] = _QUERYANNUALPROVISIONSREQUEST
DESCRIPTOR.message_types_by_name[
    "QueryAnnualProvisionsResponse"
] = _QUERYANNUALPROVISIONSRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

QueryParamsRequest = _reflection.GeneratedProtocolMessageType(
    "QueryParamsRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _QUERYPARAMSREQUEST,
        "__module__": "cosmos.mint.v1beta1.query_pb2"
        # @@protoc_insertion_point(class_scope:cosmos.mint.v1beta1.QueryParamsRequest)
    },
)
_sym_db.RegisterMessage(QueryParamsRequest)

QueryParamsResponse = _reflection.GeneratedProtocolMessageType(
    "QueryParamsResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _QUERYPARAMSRESPONSE,
        "__module__": "cosmos.mint.v1beta1.query_pb2"
        # @@protoc_insertion_point(class_scope:cosmos.mint.v1beta1.QueryParamsResponse)
    },
)
_sym_db.RegisterMessage(QueryParamsResponse)

QueryInflationRequest = _reflection.GeneratedProtocolMessageType(
    "QueryInflationRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _QUERYINFLATIONREQUEST,
        "__module__": "cosmos.mint.v1beta1.query_pb2"
        # @@protoc_insertion_point(class_scope:cosmos.mint.v1beta1.QueryInflationRequest)
    },
)
_sym_db.RegisterMessage(QueryInflationRequest)

QueryInflationResponse = _reflection.GeneratedProtocolMessageType(
    "QueryInflationResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _QUERYINFLATIONRESPONSE,
        "__module__": "cosmos.mint.v1beta1.query_pb2"
        # @@protoc_insertion_point(class_scope:cosmos.mint.v1beta1.QueryInflationResponse)
    },
)
_sym_db.RegisterMessage(QueryInflationResponse)

QueryAnnualProvisionsRequest = _reflection.GeneratedProtocolMessageType(
    "QueryAnnualProvisionsRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _QUERYANNUALPROVISIONSREQUEST,
        "__module__": "cosmos.mint.v1beta1.query_pb2"
        # @@protoc_insertion_point(class_scope:cosmos.mint.v1beta1.QueryAnnualProvisionsRequest)
    },
)
_sym_db.RegisterMessage(QueryAnnualProvisionsRequest)

QueryAnnualProvisionsResponse = _reflection.GeneratedProtocolMessageType(
    "QueryAnnualProvisionsResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _QUERYANNUALPROVISIONSRESPONSE,
        "__module__": "cosmos.mint.v1beta1.query_pb2"
        # @@protoc_insertion_point(class_scope:cosmos.mint.v1beta1.QueryAnnualProvisionsResponse)
    },
)
_sym_db.RegisterMessage(QueryAnnualProvisionsResponse)


DESCRIPTOR._options = None
_QUERYPARAMSRESPONSE.fields_by_name["params"]._options = None
_QUERYINFLATIONRESPONSE.fields_by_name["inflation"]._options = None
_QUERYANNUALPROVISIONSRESPONSE.fields_by_name["annual_provisions"]._options = None

_QUERY = _descriptor.ServiceDescriptor(
    name="Query",
    full_name="cosmos.mint.v1beta1.Query",
    file=DESCRIPTOR,
    index=0,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
    serialized_start=495,
    serialized_end=948,
    methods=[
        _descriptor.MethodDescriptor(
            name="Params",
            full_name="cosmos.mint.v1beta1.Query.Params",
            index=0,
            containing_service=None,
            input_type=_QUERYPARAMSREQUEST,
            output_type=_QUERYPARAMSRESPONSE,
            serialized_options=b"\202\323\344\223\002\035\022\033/cosmos/mint/v1beta1/params",
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.MethodDescriptor(
            name="Inflation",
            full_name="cosmos.mint.v1beta1.Query.Inflation",
            index=1,
            containing_service=None,
            input_type=_QUERYINFLATIONREQUEST,
            output_type=_QUERYINFLATIONRESPONSE,
            serialized_options=b"\202\323\344\223\002 \022\036/cosmos/mint/v1beta1/inflation",
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.MethodDescriptor(
            name="AnnualProvisions",
            full_name="cosmos.mint.v1beta1.Query.AnnualProvisions",
            index=2,
            containing_service=None,
            input_type=_QUERYANNUALPROVISIONSREQUEST,
            output_type=_QUERYANNUALPROVISIONSRESPONSE,
            serialized_options=b"\202\323\344\223\002(\022&/cosmos/mint/v1beta1/annual_provisions",
            create_key=_descriptor._internal_create_key,
        ),
    ],
)
_sym_db.RegisterServiceDescriptor(_QUERY)

DESCRIPTOR.services_by_name["Query"] = _QUERY

# @@protoc_insertion_point(module_scope)
