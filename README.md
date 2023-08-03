# Liquirizia.Serializer.Implements.FormUrlEncoded
폼 데이터 형식으로 통신하기 위한 직렬화 및 비직렬화 도구

## 사용법
```python
from Liquirizia.Serializer import SerializerHelper
import Liquirizia.Serializer.Implements.FormUrlEncoded

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
```

## 개선사항
* [ ] Form-UrlEncoder 를 사용하기 위한 객체 구현 및 객체를 통한 사용 방법 변경