def dormirMais(diaDeSemana, ferias):
    if diaDeSemana and not ferias:
        return False
    else:
        return True

print(dormirMais(False, False))
print(dormirMais(True, False))
print(dormirMais(False, True))
