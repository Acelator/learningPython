import dic


def decode(value: str, method: int or str):
    decoded_value = map(decoder, value)
    joined = "".join(map(str, list(decoded_value)))
    print(joined)


def decoder(item):
    return dic.inverseDefaultValue.get(item)
