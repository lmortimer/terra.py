"""ibc connection module message types."""

from __future__ import annotations

from typing import Optional, Any, List

import attr
from terra_proto.ibc.core.channel.v1 import (
    MsgChannelOpenInit as MsgChannelOpenInit_pb,
    MsgChannelOpenTry as MsgChannelOpenTry_pb,
    MsgChannelOpenAck as MsgChannelOpenAck_pb,
    MsgChannelOpenConfirm as MsgChannelOpenConfirm_pb,
    MsgChannelCloseInit as MsgChannelCloseInit_pb,
    MsgChannelCloseConfirm as MsgChannelCloseConfirm_pb,
    MsgRecvPacket as MsgRecvPacket_pb,
    MsgAcknowledgement as MsgAcknowledgement_pb,
    MsgTimeout as MsgTimeout_pb
)
from betterproto.lib.google.protobuf import Any as Any_pb

from terra_sdk.core.ibc.data.client import Height
from terra_sdk.core.ibc.data.channel import Channel, Packet
from terra_sdk.core.msg import Msg

__all__ = [
    "MsgChannelOpenInit", "MsgChannelOpenTry", "MsgChannelOpenAck", "MsgChannelOpenConfirm",
    "MsgChannelCloseInit", "MsgChannelCloseConfirm",
    "MsgRecvPacket", "MsgTimeout", "MsgAcknowledgement"
]


@attr.s
class MsgChannelOpenInit(Msg):
    """
    MsgChannelOpenInit defines an sdk.Msg to initialize a channel handshake. It
    is called by a relayer on Chain A.
    """

    type_url = "/ibc.core.channel.v1.MsgChannelOpenInit"
    """"""

    port_id: str = attr.ib()
    channel: Channel = attr.ib()
    signer: str = attr.ib()

    def to_amino(self):
        raise Exception("Amino not supported")

    @classmethod
    def from_data(cls, data: dict) -> MsgChannelOpenInit:
        return cls(
            port_id=data["port_id"],
            channel=Channel.from_data(data["port_id"]),
            signer=data["signer"]
        )

    def to_proto(self) -> MsgChannelOpenInit_pb:
        return MsgChannelOpenInit_pb(
            port_id=self.port_id,
            channel=self.channel.to_proto(),
            signer=self.signer
        )


@attr.s
class MsgChannelOpenTry(Msg):
    """
    MsgChannelOpenInit defines a msg sent by a Relayer to try to open a channel
    on Chain B.
    """

    type_url = "/ibc.core.channel.v1.MsgChannelOpenTry"
    """"""

    port_id: str = attr.ib()
    previous_channel_id: str = attr.ib()
    channel: Channel = attr.ib()
    counterparty_version: str = attr.ib()
    proof_init: bytes = attr.ib()
    proof_height: Height = attr.ib()
    signer: str = attr.ib()

    def to_amino(self):
        raise Exception("Amino not supported")

    @classmethod
    def from_data(cls, data: dict) -> MsgChannelOpenTry:
        return cls(
            port_id=data["port_id"],
            previous_channel_id=data["previous_channel_id"],
            channel=Channel.from_data(data["channel"]),
            counterparty_version=data["counterparty_version"],
            proof_init=data["proof_init"],
            proof_height=Height.from_data(data["proof_height"]),
            signer=data["signer"]
        )

    def to_proto(self) -> MsgChannelOpenTry_pb:
        return MsgChannelOpenTry_pb(
            port_id=self.port_id,
            previous_channel_id=self.previous_channel_id,
            channel=self.channel.to_proto(),
            counterparty_version=self.counterparty_version,
            proof_init=self.proof_init,
            proof_height=self.proof_height.to_proto(),
            signer=self.signer
        )


@attr.s
class MsgChannelOpenAck(Msg):
    """
    MsgChannelOpenAck defines a msg sent by a Relayer to Chain A to acknowledge
    the change of channel state to TRYOPEN on Chain B.
    """

    type_url = "/ibc.core.channel.v1.MsgChannelOpenAck"
    """"""

    port_id: str = attr.ib()
    channel_id: str = attr.ib()
    counterparty_channel_id: str = attr.ib()
    counterparty_version: str = attr.ib()
    proof_try: bytes = attr.ib()
    proof_height: Height = attr.ib()
    signer: str = attr.ib()

    def to_amino(self):
        raise Exception("Amino not supported")

    @classmethod
    def from_data(cls, data: dict) -> MsgChannelOpenAck:
        return cls(
            port_id=data["port_id"],
            channel_id=data["channel_id"],
            counterparty_channel_id=data["counterparty_channel_id"],
            counterparty_version=data["counterparty_version"],
            proof_try=data["proof_try"],
            proof_height=Height.from_data(data["proof_height"]),
            signer=data["signer"]
        )

    def to_proto(self) -> MsgChannelOpenAck_pb:
        return MsgChannelOpenAck_pb(
            port_id=self.port_id,
            channel_id=self.channel_id,
            counterparty_channel_id=self.counterparty_channel_id,
            counterparty_version=self.counterparty_version,
            proof_try=self.proof_try,
            proof_height=self.proof_height.to_proto(),
            signer=self.signer
        )


@attr.s
class MsgChannelOpenConfirm(Msg):
    """
    MsgChannelOpenConfirm defines a msg sent by a Relayer to Chain B to
    acknowledge the change of channel state to OPEN on Chain A.
    """

    type_url = "/ibc.core.channel.v1.MsgChannelOpenConfirm"
    """"""

    port_id: str = attr.ib()
    channel_id: str = attr.ib()
    proof_ack: bytes = attr.ib()
    proof_height: Height = attr.ib()
    signer: str = attr.ib()

    def to_amino(self):
        raise Exception("Amino not supported")

    @classmethod
    def from_data(cls, data: dict) -> MsgChannelOpenConfirm:
        return cls(
            port_id=data["port_id"],
            channel_id=data["channel_id"],
            proof_ack=data["proof_ack"],
            proof_height=Height.from_data(data["proof_height"]),
            signer=data["signer"]
        )

    def to_proto(self) -> MsgChannelOpenConfirm_pb:
        return MsgChannelOpenConfirm_pb(
            port_id=self.port_id,
            channel_id=self.channel_id,
            proof_ack=self.proof_ack,
            proof_height=self.proof_height.to_proto(),
            signer=self.signer
        )


@attr.s
class MsgChannelCloseInit(Msg):
    """
    """

    type_url = "/ibc.core.channel.v1.MsgChannelCloseInit"
    """"""

    port_id: str = attr.ib()
    channel_id: str = attr.ib()
    signer: str = attr.ib()

    def to_amino(self):
        raise Exception("Amino not supported")

    @classmethod
    def from_data(cls, data: dict) -> MsgChannelCloseInit:
        return cls(
            port_id=data["port_id"],
            channel_id=data["channel_id"],
            signer=data["signer"]
        )

    def to_proto(self) -> MsgChannelCloseInit_pb:
        return MsgChannelCloseInit_pb(
            port_id=self.port_id,
            channel_id=self.channel_id,
            signer=self.signer
        )


@attr.s
class MsgChannelCloseConfirm(Msg):
    """
    MsgChannelCloseConfirm defines a msg sent by a Relayer to Chain B to
    acknowledge the change of channel state to CLOSED on Chain A.
    """

    type_url = "/ibc.core.channel.v1.MsgChannelCloseConfirm"
    """"""

    port_id: str = attr.ib()
    channel_id: str = attr.ib()
    proof_init: bytes = attr.ib()
    proof_height: Height = attr.ib()
    signer: str = attr.ib()

    def to_amino(self):
        raise Exception("Amino not supported")

    @classmethod
    def from_data(cls, data: dict) -> MsgChannelCloseConfirm:
        return cls(
            port_id=data["port_id"],
            channel_id=data["channel_id"],
            proof_init=data["proof_init"],
            proof_height=Height.from_data(data["proof_height"]),
            signer=data["signer"]
        )

    def to_proto(self) -> MsgChannelCloseConfirm_pb:
        return MsgChannelCloseConfirm_pb(
            port_id=self.port_id,
            channel_id=self.channel_id,
            proof_init=self.proof_init,
            proof_height=self.proof_height.to_proto(),
            signer=self.signer
        )


@attr.s
class MsgRecvPacket(Msg):
    """
    MsgRecvPacket receives incoming IBC packet
    """

    type_url = "/ibc.core.channel.v1.MsgRecvPacket"
    """"""

    packet: Packet = attr.ib()
    proof_commitment: bytes = attr.ib()
    proof_height: Height = attr.ib()
    signer: str = attr.ib()

    def to_amino(self):
        raise Exception("Amino not supported")

    @classmethod
    def from_data(cls, data: dict) -> MsgRecvPacket:
        return cls(
            packet=Packet.from_data(data["packet"]),
            proof_commitment=data["proof_commitment"],
            proof_height=Height.from_data(data["proof_height"]),
            signer=data["signer"]
        )

    def to_proto(self) -> MsgRecvPacket_pb:
        return MsgRecvPacket_pb(
            packet=self.packet.to_proto(),
            proof_commitment=self.proof_commitment,
            proof_height=self.proof_height.to_proto(),
            signer=self.signer
        )


@attr.s
class MsgTimeout(Msg):
    """
    MsgTimeout receives timed-out packet
    """

    type_url = "/ibc.core.channel.v1.MsgTimeout"
    """"""

    packet: Packet = attr.ib()
    proof_unreceived: bytes = attr.ib()
    proof_height: Height = attr.ib()
    next_sequence_recv: int = attr.ib(converter=int)
    signer: str = attr.ib()

    def to_amino(self):
        raise Exception("Amino not supported")

    @classmethod
    def from_data(cls, data: dict) -> MsgTimeout:
        return cls(
            packet=Packet.from_data(data["packet"]),
            proof_unreceived=data["proof_unreceived"],
            proof_height=Height.from_data(data["proof_height"]),
            next_sequence_recv=data["next_sequence_recv"],
            signer=data["signer"]
        )

    def to_proto(self) -> MsgTimeout_pb:
        return MsgTimeout_pb(
            packet=self.packet.to_proto(),
            proof_unreceived=self.proof_unreceived,
            proof_height=self.proof_height.to_proto(),
            next_sequence_recv=self.next_sequence_recv,
            signer=self.signer
        )

@attr.s
class MsgAcknowledgement(Msg):
    """
    MsgAcknowledgement receives incoming IBC acknowledgement
    """

    type_url = "/ibc.core.channel.v1.MsgAcknowledgement"
    """"""

    packet: Packet = attr.ib()
    acknowledgement: bytes = attr.ib()
    proof_acked: bytes = attr.ib()
    proof_height: Height = attr.ib()
    signer: str = attr.ib()

    def to_amino(self):
        raise Exception("Amino not supported")

    @classmethod
    def from_data(cls, data: dict) -> MsgAcknowledgement:
        return cls(
            packet=Packet.from_data(data["packet"]),
            acknowledgement=data["acknowledgement"],
            proof_acked=data["proof_acked"],
            proof_height=Height.from_data(data["proof_height"]),
            signer=data["signer"]
        )

    def to_proto(self) -> MsgAcknowledgement_pb:
        return MsgAcknowledgement_pb(
            packet=self.packet.to_proto(),
            acknowledgement=self.acknowledgement,
            proof_acked=self.proof_acked,
            proof_height=self.proof_height.to_proto(),
            signer=self.signer
        )



