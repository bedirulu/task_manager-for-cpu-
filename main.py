from rich import print 
import time
from rich.live import Live
from rich.table import Table
from rich.console import Console
from rich.progress import Progress
from rich.layout import Layout
import psutil
from rich.progress import Progress, TextColumn, BarColumn, TaskProgressColumn


console = Console()
canli_tablo = Table
                 





surec = Progress(
    TextColumn("[progress.description]{task.description}"),
    BarColumn(),
    TaskProgressColumn()
)

gorev_listesi=[]

cekirdek_sayisi = psutil.cpu_count()

for i in range(cekirdek_sayisi):
    yeni_gorev = surec.add_task(f"[red]Core {i}", total=100)
    gorev_listesi.append(yeni_gorev)



ana_ekran = Layout()
ana_ekran.split_column(
    Layout(name='ust_kisim'),
    Layout(name='alt_kisim')
)    

ana_ekran['alt_kisim'].update(surec)



with Live(ana_ekran, refresh_per_second=5 ):

    

    while True:
        canli_tablo = Table(title='Anlik CPU Degerleri')
        canli_tablo.add_column('Cekirdek',style='cyan', justify='center')
        canli_tablo.add_column('Kullanim',style='magenta', justify='center')

        kullanim= psutil.cpu_percent(interval=None , percpu=True)

        for i in range (cekirdek_sayisi):
            o_anki_gorev= gorev_listesi[i]
            o_anki_yuzde = kullanim[i]

            surec.update(o_anki_gorev, completed= o_anki_yuzde)

            canli_tablo.add_row(f'Core {i}', f'% {o_anki_yuzde}')

        ana_ekran['ust_kisim'].update(canli_tablo)

        time.sleep(0.5)



