# Sistema de Monitoramento Espacial - Global Solution
import random

# Estrutura dos módulos da missão
modulos = [
    {"nome": "Painéis Solares", "temp": 25, "energia": 95, "status": "OK"},
    {"nome": "Sistema de Suporte à Vida", "temp": 30, "energia": 80, "status": "OK"},
    {"nome": "Comunicações", "temp": 85, "energia": 40, "status": "CRÍTICO"}
]

def analisar_missao(lista_modulos):
    print("--- RELATÓRIO DE MONITORAMENTO ESPACIAL ---")
    for mod in lista_modulos:
        print(f"\nMódulo: {mod['nome']}")
        # Lógica de Alerta
        if mod['temp'] > 80:
            print(f"[ALERTA] Temperatura alta em {mod['nome']}! Ativando resfriamento.")
        
        if mod['energia'] < 50:
            print(f"[ALERTA] Energia baixa em {mod['nome']}! Otimizando consumo.")
            
        print(f"Status: {mod['status']} | Temp: {mod['temp']}°C | Energia: {mod['energia']}%")

analisar_missao(modulos)
