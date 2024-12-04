from sqlalchemy.orm import declarative_base,sessionmaker,relationship
import pandas
from sqlalchemy import Column,Integer,ForeignKey,String,DateTime,Float,create_engine
from config.config import config
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler,StandardScaler
from sklearn.preprocessing import LabelEncoder,OneHotEncoder
from sklearn.preprocessing import MultiLabelBinarizer
from imblearn.over_sampling import SMOTE










def extarct_data(prompt='classification'):
    engine = create_engine(config.database_url)
    Base = declarative_base()
    Session = sessionmaker(bind=engine)
    session = Session()



    class AnnonceEquipement(Base):
        __tablename__ = 'annonce_equipement'
        
        annonce_id = Column(Integer, ForeignKey('annonces.id'), primary_key=True)
        equipement_id = Column(Integer, ForeignKey('equipements.id'), primary_key=True)
        
        annonce = relationship("Annonce", back_populates="equipements")
        equipement = relationship("Equipement", back_populates="annonces")

    class Annonce(Base):
        __tablename__ = 'annonces'
        
        id = Column(Integer, primary_key=True)
        title = Column(String)
        price = Column(String)  
        datetime = Column(DateTime, nullable=False)
        nb_rooms = Column(Integer)
        nb_baths = Column(Integer)
        surface_area = Column(Float)
        link = Column(String)
        city_id = Column(Integer, ForeignKey('villes.id'), nullable=False)
        
        ville = relationship("Ville", back_populates="annonces")
        equipements = relationship("AnnonceEquipement", back_populates="annonce")

    class Ville(Base):
        __tablename__ = 'villes'
        
        id = Column(Integer, primary_key=True)
        name = Column(String)
        
        annonces = relationship("Annonce", back_populates="ville")

    class Equipement(Base):
        __tablename__ = 'equipements'
        
        id = Column(Integer, primary_key=True)
        name = Column(String)
        
        annonces = relationship("AnnonceEquipement", back_populates="equipement")
    


    result = session.query(Annonce,Ville,Equipement,AnnonceEquipement).join(Ville).join(AnnonceEquipement).join(Equipement).all()


    #print(result)

    data=[]
    for obj in result:
        
        annonce,ville,equipement,aq = obj

        row = {
            config.column_annonce[0]:annonce.id,
            config.column_annonce[2]:annonce.title,
            config.column_annonce[1]:annonce.price,
            config.column_annonce[3]:annonce.datetime,
            config.column_annonce[4]:annonce.nb_rooms,
            config.column_annonce[5]:annonce.nb_baths,
            config.column_annonce[6]:annonce.surface_area,
            config.column_annonce[7]:annonce.city_id,
            config.column_ville[1]:ville.name,
            config.column_equipement[1]:equipement.name
        }
        data.append(row)
    
    df = pd.DataFrame(data)
    #print(df.info())
    #print(df.head())


    df['price']=pd.to_numeric(df['price'])
    df['jour']=df['date time'].dt.hour
    df['month']=df['date time'].dt.month
    df['year']=df['date time'].dt.year
    df.drop('date time',axis=1,inplace=True)

    def agg_remove(group):
        if len(group['id']) != 1:
            group['equipement']=','.join(group['equipement'])
            return group.drop_duplicates()
        
        return group    



    df = df.groupby('id').apply(agg_remove).reset_index(drop=True)

    list_to_remove=df['ville'].value_counts()[df['ville'].value_counts()==1].index.to_list()

    for ele in list_to_remove:
        df=df[df['ville']!= ele]

    for i in range(2):
        df[config.operation_array[i]]=np.sqrt(df[config.operation_array[i]])
    for i in range(2,4):
        df[config.operation_array[i]]=np.log1p(df[config.operation_array[i]])
    

    scaler = StandardScaler()

    for i in config.operation_array:
        df[i] = scaler.fit_transform(df[i].values.reshape(-1, 1))

    label_encoder =LabelEncoder()
    df[config.column_ville[1]]=label_encoder.fit_transform(df[config.column_ville[1]])


    df[config.column_equipement[1]]=df[config.column_equipement[1]].apply(lambda x : x.split(","))

    mlb = MultiLabelBinarizer()
    encoded_columns = mlb.fit_transform(df[config.column_equipement[1]])

    #print(encoded_columns)

    df_encoded_columns = pd.DataFrame(encoded_columns,columns=mlb.classes_).reset_index()
    df_encoded_columns['index']=df_encoded_columns['index'] + 1
    #display(df_encoded_columns)


    df=pd.merge(df,df_encoded_columns,left_on='id',right_on='index',how='inner')

    df=df[df['ville']!=13]


    if prompt.lower()=='regression':
        return df
    

    #here i commpleted the encoding newt is smote

    x = df.drop(['title','equipement','index','city id','id','ville'],axis=1)
    y=df['ville']

    #display(y.value_counts())

    smote = SMOTE(sampling_strategy='auto',random_state=42,k_neighbors=1)
    x_res,y_res = smote.fit_resample(x,y)

    #display(x_res)
    #display(y_res)

    x_res['ville'] = y_res

    return x_res







    

    





        


#df_regression = extarct_data()

#print(df_regression)
#print(df_regression.info())
















