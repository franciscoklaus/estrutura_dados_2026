from Lista import ArrayList

array = ArrayList()
array.insert("Ana")
print(array.LEN)
array.insert("Bia")
print(array.LEN)
array.insert("Clara")
print(array.LEN)

#array.show()


def _helper(campo: any) -> None:
    if isinstance(campo, dict):
        matricula = campo.get("value",'desconhecido')
        return matricula
    return campo


print(_helper({"value": 1234}))

print(_helper(1234))
