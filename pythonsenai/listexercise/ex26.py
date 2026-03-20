def calcular_media(notas):
    total = sum(notas)
    media = total / len(notas)
    return media


def verificar_situacao(media):
    if media >= 7:
        return "Aprovado"
    else:
        return "Reprovado"
    
notas = [7.5, 8.8, 6.5, 9.8]
media = calcular_media(notas)
situacao = verificar_situacao(media)
print("A média é:", media)
print("A situação é:", situacao)


