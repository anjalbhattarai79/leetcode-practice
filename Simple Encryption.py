'''
encrypt("012345", 1)  =>  "135024"
encrypt("012345", 2)  =>  "135024"  ->  "304152"
encrypt("012345", 3)  =>  "135024"  ->  "304152"  ->  "012345"

'''
def decrypt(text, n):
    if not text or n <= 0:
        return text

    length = len(text)

    for _ in range(n):
        mid = length // 2
        odd = text[:mid]
        even = text[mid:]

        result = []
        o = e = 0

        for i in range(length):
            if i % 2 == 1:
                result.append(odd[o])
                o += 1
            else:
                result.append(even[e])
                e += 1

        text = "".join(result)

    return text

def encrypt(text, n):
    if not text or n <= 0:
        return text

    for _ in range(n):
        odd = ""
        even = ""
        for i, ch in enumerate(text):
            if i % 2 == 1:
                odd += ch
            else:
                even += ch
        text = odd + even

    return text

