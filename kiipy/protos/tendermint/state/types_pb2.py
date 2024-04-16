# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tendermint/state/types.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from tendermint.abci import types_pb2 as tendermint_dot_abci_dot_types__pb2
from tendermint.types import types_pb2 as tendermint_dot_types_dot_types__pb2
from tendermint.types import validator_pb2 as tendermint_dot_types_dot_validator__pb2
from tendermint.types import params_pb2 as tendermint_dot_types_dot_params__pb2
from tendermint.version import types_pb2 as tendermint_dot_version_dot_types__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1ctendermint/state/types.proto\x12\x10tendermint.state\x1a\x14gogoproto/gogo.proto\x1a\x1btendermint/abci/types.proto\x1a\x1ctendermint/types/types.proto\x1a tendermint/types/validator.proto\x1a\x1dtendermint/types/params.proto\x1a\x1etendermint/version/types.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\xb8\x01\n\rABCIResponses\x12\x37\n\x0b\x64\x65liver_txs\x18\x01 \x03(\x0b\x32\".tendermint.abci.ResponseDeliverTx\x12\x34\n\tend_block\x18\x02 \x01(\x0b\x32!.tendermint.abci.ResponseEndBlock\x12\x38\n\x0b\x62\x65gin_block\x18\x03 \x01(\x0b\x32#.tendermint.abci.ResponseBeginBlock\"d\n\x0eValidatorsInfo\x12\x35\n\rvalidator_set\x18\x01 \x01(\x0b\x32\x1e.tendermint.types.ValidatorSet\x12\x1b\n\x13last_height_changed\x18\x02 \x01(\x03\"u\n\x13\x43onsensusParamsInfo\x12\x41\n\x10\x63onsensus_params\x18\x01 \x01(\x0b\x32!.tendermint.types.ConsensusParamsB\x04\xc8\xde\x1f\x00\x12\x1b\n\x13last_height_changed\x18\x02 \x01(\x03\"S\n\x07Version\x12\x36\n\tconsensus\x18\x01 \x01(\x0b\x32\x1d.tendermint.version.ConsensusB\x04\xc8\xde\x1f\x00\x12\x10\n\x08software\x18\x02 \x01(\t\"\xfd\x04\n\x05State\x12\x30\n\x07version\x18\x01 \x01(\x0b\x32\x19.tendermint.state.VersionB\x04\xc8\xde\x1f\x00\x12\x1d\n\x08\x63hain_id\x18\x02 \x01(\tB\x0b\xe2\xde\x1f\x07\x43hainID\x12\x16\n\x0einitial_height\x18\x0e \x01(\x03\x12\x19\n\x11last_block_height\x18\x03 \x01(\x03\x12\x45\n\rlast_block_id\x18\x04 \x01(\x0b\x32\x19.tendermint.types.BlockIDB\x13\xc8\xde\x1f\x00\xe2\xde\x1f\x0bLastBlockID\x12=\n\x0flast_block_time\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x08\xc8\xde\x1f\x00\x90\xdf\x1f\x01\x12\x37\n\x0fnext_validators\x18\x06 \x01(\x0b\x32\x1e.tendermint.types.ValidatorSet\x12\x32\n\nvalidators\x18\x07 \x01(\x0b\x32\x1e.tendermint.types.ValidatorSet\x12\x37\n\x0flast_validators\x18\x08 \x01(\x0b\x32\x1e.tendermint.types.ValidatorSet\x12&\n\x1elast_height_validators_changed\x18\t \x01(\x03\x12\x41\n\x10\x63onsensus_params\x18\n \x01(\x0b\x32!.tendermint.types.ConsensusParamsB\x04\xc8\xde\x1f\x00\x12,\n$last_height_consensus_params_changed\x18\x0b \x01(\x03\x12\x19\n\x11last_results_hash\x18\x0c \x01(\x0c\x12\x10\n\x08\x61pp_hash\x18\r \x01(\x0c\x42\x39Z7github.com/tendermint/tendermint/proto/tendermint/stateb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'tendermint.state.types_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z7github.com/tendermint/tendermint/proto/tendermint/state'
  _CONSENSUSPARAMSINFO.fields_by_name['consensus_params']._options = None
  _CONSENSUSPARAMSINFO.fields_by_name['consensus_params']._serialized_options = b'\310\336\037\000'
  _VERSION.fields_by_name['consensus']._options = None
  _VERSION.fields_by_name['consensus']._serialized_options = b'\310\336\037\000'
  _STATE.fields_by_name['version']._options = None
  _STATE.fields_by_name['version']._serialized_options = b'\310\336\037\000'
  _STATE.fields_by_name['chain_id']._options = None
  _STATE.fields_by_name['chain_id']._serialized_options = b'\342\336\037\007ChainID'
  _STATE.fields_by_name['last_block_id']._options = None
  _STATE.fields_by_name['last_block_id']._serialized_options = b'\310\336\037\000\342\336\037\013LastBlockID'
  _STATE.fields_by_name['last_block_time']._options = None
  _STATE.fields_by_name['last_block_time']._serialized_options = b'\310\336\037\000\220\337\037\001'
  _STATE.fields_by_name['consensus_params']._options = None
  _STATE.fields_by_name['consensus_params']._serialized_options = b'\310\336\037\000'
  _globals['_ABCIRESPONSES']._serialized_start=262
  _globals['_ABCIRESPONSES']._serialized_end=446
  _globals['_VALIDATORSINFO']._serialized_start=448
  _globals['_VALIDATORSINFO']._serialized_end=548
  _globals['_CONSENSUSPARAMSINFO']._serialized_start=550
  _globals['_CONSENSUSPARAMSINFO']._serialized_end=667
  _globals['_VERSION']._serialized_start=669
  _globals['_VERSION']._serialized_end=752
  _globals['_STATE']._serialized_start=755
  _globals['_STATE']._serialized_end=1392
# @@protoc_insertion_point(module_scope)