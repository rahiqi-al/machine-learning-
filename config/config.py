import yaml 
from dotenv import load_dotenv
import os




load_dotenv()

class config():


    with open('config/config.yml','r') as file :
        config_data = yaml.load(file,Loader=yaml.FullLoader)


    
    column_annonce = config_data['COLUMN_DATAFRAMAE']['annonce']
    column_equipement = config_data['COLUMN_DATAFRAMAE']['equipement']
    column_annonce_equipement = config_data['COLUMN_DATAFRAMAE']['annonce_equipement']
    column_ville = config_data['COLUMN_DATAFRAMAE']['ville']
    operation_array = config_data['COLUMN_DATAFRAMAE']['operation array']


    database_url=os.getenv('DATABASE_URL')


config=config()

print(config.operation_array)
print(config.column_annonce,config.column_annonce_equipement,config.column_equipement,config.column_ville)


    

