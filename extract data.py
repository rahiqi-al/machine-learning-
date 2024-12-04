from sqlalchemy.orm import declarative_base,sessionmaker,relationship
import pandas
from sqlalchemy import Column,Integer,ForeignKey,String,DateTime,Float,create_engine
from config.config import config
import pandas as pd






def extarct_data(prompt):
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
    print(df.info())
    print(df.head())
        


extarct_data('ali')













