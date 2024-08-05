dict = {}

dict.update({chr(i): "ㄱ" for i in range(ord("가"), ord("깋") + 1)})
dict.update({chr(i): "ㄴ" for i in range(ord("나"), ord("닣") + 1)})
dict.update({chr(i): "ㄷ" for i in range(ord("다"), ord("딯") + 1)})
dict.update({chr(i): "ㄹ" for i in range(ord("라"), ord("맇") + 1)})
dict.update({chr(i): "ㅁ" for i in range(ord("마"), ord("밓") + 1)})
dict.update({chr(i): "ㅂ" for i in range(ord("바"), ord("빟") + 1)})
dict.update({chr(i): "ㅅ" for i in range(ord("사"), ord("싷") + 1)})
dict.update({chr(i): "ㅇ" for i in range(ord("아"), ord("잏") + 1)})
dict.update({chr(i): "ㅈ" for i in range(ord("자"), ord("짛") + 1)})
dict.update({chr(i): "ㅊ" for i in range(ord("차"), ord("칳") + 1)})
dict.update({chr(i): "ㅋ" for i in range(ord("카"), ord("킿") + 1)})
dict.update({chr(i): "ㅌ" for i in range(ord("타"), ord("팋") + 1)})
dict.update({chr(i): "ㅍ" for i in range(ord("파"), ord("핗") + 1)})
dict.update({chr(i): "ㅎ" for i in range(ord("하"), ord("힣") + 1)})

dict.update({chr(i): "ㄲ" for i in range(ord("까"), ord("낗") + 1)})
dict.update({chr(i): "ㄸ" for i in range(ord("따"), ord("띻") + 1)})
dict.update({chr(i): "ㅃ" for i in range(ord("빠"), ord("삫") + 1)})
dict.update({chr(i): "ㅆ" for i in range(ord("싸"), ord("앃") + 1)})
dict.update({chr(i): "ㅉ" for i in range(ord("짜"), ord("찧") + 1)})

print("".join(dict[c] for c in input()))
