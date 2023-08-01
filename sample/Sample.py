# -*- coding: utf-8 -*-

from Liquirizia.Serializer import SerializerHelper
import Liquirizia.Serializer.Implements.FormUrlEncoded


if __name__ == '__main__':

	_ = {
		'a': True,
		'b': 0,
		'c': 0.0,
		'd': 'String',
		'e': [1,2,3],
		'f': (1,2,3),
	}
	encoded = SerializerHelper.Encode(_, format='application/x-www-form-urlencoded', charset='utf-8')
	decoded = SerializerHelper.Decode(encoded, format='application/x-www-form-urlencoded', charset='utf-8')
	print(encoded, decoded)

	# TODO : Support DataModelObject
