def calcular_saldo_rankeadas(vitorias, derrotas):
    saldo_rankeadas = vitorias - derrotas
    return saldo_rankeadas

def avaliar_desempenho(saldo_rankeadas):
    if saldo_rankeadas < 10:
        return "Você é Ferro"
    elif 10 <= saldo_rankeadas <= 50:
        return "Você é Prata"
    elif 51 <= saldo_rankeadas <= 80:
        return "Você é Ouro"
    elif 81 <= saldo_rankeadas <= 100:
        return "Você é Diamante"
    elif saldo_rankeadas > 100:
        return "Você é Lendário"
    else:
        return "Você é Imortal"