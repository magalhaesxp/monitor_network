import psutil

class memory:
    
    def __init__(self):
        memoria = psutil.virtual_memory()
        self.memoria_total = memoria.total / (1024 ** 3)
        self.memoria_dispo = memoria.available / (1024 ** 3)
        self.memoria_utili = memoria.used / (1024 ** 3)
    

alerta = memory()
#print(f"Memoria total: {alerta.memoria_total:.2f} GB")
#print(f"Memoria livre: {alerta.memoria_dispo:.2f} GB")
#print(f"Memoria em uso: {alerta.memoria_utili:.2f} GB")

perc_util = ((alerta.memoria_utili / alerta.memoria_total) * 100)

#print(f"Percentual de memória Utilizada: {perc_util:.2f}%")

if perc_util < 85:
    print('Memória Saudável')
else:
    print('Atenção o memória disponível baixa, por favor verifique')


