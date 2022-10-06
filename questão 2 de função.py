def problema_macaco(a_sorrindo, b_sorrindo):
    if (a_sorrindo and b_sorrindo) or (not a_sorrindo and not b_sorrindo):
        return True
    else:
        return False

print(problema_macaco(True, True))
print(problema_macaco(False, False))
print(problema_macaco(True, False))
