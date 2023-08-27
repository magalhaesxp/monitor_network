import psutil


class Data_disk:

   def __init__(self):
    
    particao = psutil.disk_partitions()[0].device
    espaco_disco = psutil.disk_usage(particao)
    espaco_disco_disponivel_gb = espaco_disco.free / (1024 ** 3)
 
    self.disco_total = espaco_disco.total / (1024 ** 3) 
    self.disco_utilizado = self.disco_total - espaco_disco_disponivel_gb 
    self.perc_livre = (self.disco_total / self.disco_utilizado * 10)


    #print(f"Tamanho total da partição: {disco_total:.2f} GB")
    #print(f"Total Utilizado da partição: {disco_utilizado:.2f} GB")
    #print(f"Espaço em disco disponível no sistema: {espaco_disco_disponivel_gb:.2f} GB")
    #print(f"Pocentagem utilizado da partição: {perc_livre:.2f}%")
         

alerta = Data_disk()

if int(alerta.perc_livre) > 90:
  print("Atenção disco necessita de manutenção")
else:
  print('Disco saudável')

     