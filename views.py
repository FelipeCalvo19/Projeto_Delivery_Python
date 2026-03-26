from datetime import datetime

horas = datetime.now().hour

def saudaçao_horario (Horas):
    horario = datetime.now().hour
    momento = "nenhum"
    if 6 <= horario < 12:
        momento = "Dia"
    elif 12 <= horario < 18:
        momento = "Tarde"
    elif 19 <= horario < 23:
        momento = "Noite"
    else: 
        momento = "madrugada"
    return momento

def criar_linhas(Divisor):
    """Multiplicação de strings para criar separadores visuais dinâmicos."""
    return Divisor * 30

def boas_vindas(Nome):
    """Retorna saudação. Exemplo de uso de f-strings para interpolação."""
    return f"Bom {saudaçao_horario(horas)} {Nome}!! tudo bem?"

def despedidas(Nome):
    return f"Obrigado por pedir conosco {Nome}! Tenha um ótimo {saudaçao_horario(horas)}!"

def conversor_valor(Valor, cifra):
    """Formatação de moeda usando .2f para garantir duas casas decimais."""
    return f"{cifra}{Valor:.2f}"