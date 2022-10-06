def papagaio_falante(falando, hora):
    if falando and hora < 7 or hora > 20:
        return True
    else:
        return False
print(papagaio_falante(True, 6))
print(papagaio_falante(True, 7))
print(papagaio_falante(True, 8))
print(papagaio_falante(False, 6))
print(papagaio_falante(False, 7))
print(papagaio_falante(False, 8))
