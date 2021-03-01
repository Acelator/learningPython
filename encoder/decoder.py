import dic


# Decode a set value
def decode(value: str, method: int or str):
    decoded_value = map(decoder, value)
    joined = "".join(map(str, list(decoded_value)))
    print(joined)


# It returns the original value
def decoder(item):
    return dic.inverseDefaultValue.get(item)
