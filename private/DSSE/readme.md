# SSE database building

PRF -> Hmacsha256
Enc(K2, id) -> Hmacsha256(K2, randomness) xor id

cd ./buildIndex
python ./index.py test1w
python ./searchtoken.py <searchword>