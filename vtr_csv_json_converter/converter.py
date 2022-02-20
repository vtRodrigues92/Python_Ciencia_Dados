import csv, json
import os
import shutil
import logging
import click

data = {}



### Inserindo mensagem de log no programa ###

logging.basicConfig(
    level='DEBUG', format="'%(asctime)s - %(name)s - %(levelname)s - %(message)s'"
)
logger = logging.getLogger('vtr_csv_json_converter')


### Inserindo os comandos do programa no prompt ###

@click.command()
@click.option("--input", "-i", default = './', help="Caminho onde ler os arquivos para conversão.", type=str)
@click.option("--output", "-o", default = './', help="Caminho onde os arquivos convertidos serão salvos.", type=str)
@click.option("--delimiter", "-d", default=",", help="Separador usado para dividir os arquivos. Para o delimitador ' | ', usar com aspas duplas.", type=str)
@click.option("--prefix", "-prefix", prompt = True, default = 'file',
              help = "Prefixo usado para preceder o nome do arquivo convertido salvo no disco."
                     " O sufixo será nome do arquivo csv. ex: (prefixo)_(nome do arquivo csv).json")



def converter(input: str = "./", output: str = "./", delimiter: str = ',', prefix: str = None):

    for p in [os.path.abspath(input), os.path.abspath(output)]:
        if not (os.path.isfile(p) or os.path.isdir(p)):
            raise(TypeError("Caminho ou nome de arquivo inválido"))
            break
    
    input_path = os.listdir(input)
    output_path = os.listdir(output)
    arqjson = prefix
    logger.info("Input Path: %s",os.path.abspath(input))
    logger.info("Output Path: %s",os.path.abspath(output))


    ###Encontrando arquivo csv###
    for file_csv in input_path:
        if file_csv.endswith(".csv"):
            logger.info("Lendo Arquivo Único: " + file_csv)
        else:
            continue


    ###Lendo arquivo csv###
        path_complete_input = os.path.abspath(input) + "\\" + file_csv
        path_complete_output = os.path.abspath(output) 
             
        with open(path_complete_input) as fcsv:
            csvReader = csv.DictReader(fcsv, delimiter=delimiter)


    ###Escrevendo dados para o arquivo Json###
            with open(arqjson, "w") as fjson:
                for row in csvReader:
                    fjson.write(json.dumps(row, indent=4))
        
        new_name = arqjson + "_" + os.path.splitext(file_csv)[0] + ".json"
        os.rename(arqjson, new_name)
        shutil.move(new_name, path_complete_output)
        logger.info("Salvando arquivo " + new_name + " no diretório " + path_complete_output)
        
    logger.info("Todos os arquivos lidos para o caminho determinado.")

converter()


