# -*- coding: utf-8 -*-

from .Encoder import Encoder
from .Decoder import Decoder

from Liquirizia.Serializer import SerializerHelper

__all__ = (
	'Encoder',
	'Decoder',
)


SerializerHelper.Set('application/x-www-form-urlencoded', Encoder, Decoder)
SerializerHelper.Set('application/x-www-form', Encoder, Decoder)
SerializerHelper.Set('form-urlencoded', Encoder, Decoder)
SerializerHelper.Set('form', Encoder, Decoder)
