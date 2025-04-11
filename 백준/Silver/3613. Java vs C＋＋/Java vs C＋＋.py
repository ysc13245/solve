var = input()
tokens = var.split("_")
if len(tokens) > 1:
    if not var.islower() or any(not len(token) for token in tokens):
        result = "Error!"
    else:
        result = tokens[0] + "".join(token.capitalize() for token in tokens[1:])
else:
    result = []
    
    for c in var:
        if c.isupper():
            result.append("_" + c.lower())
        else:
            result.append(c)
    result = "".join(result)
if var[0].isupper():
    result = "Error!"
print(result)
