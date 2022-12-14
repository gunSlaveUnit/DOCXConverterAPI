from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class MergeRequest(_message.Message):
    __slots__ = ["docs"]
    DOCS_FIELD_NUMBER: _ClassVar[int]
    docs: _containers.RepeatedScalarFieldContainer[bytes]
    def __init__(self, docs: _Optional[_Iterable[bytes]] = ...) -> None: ...

class MerrgeResponse(_message.Message):
    __slots__ = ["doc"]
    DOC_FIELD_NUMBER: _ClassVar[int]
    doc: bytes
    def __init__(self, doc: _Optional[bytes] = ...) -> None: ...
