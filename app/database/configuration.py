from sqlalchemy import create_engine, event
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine import Engine

#conexion BD
#nombreBD
dataBaseName = "gestionbd"
#UsuarioBd
userName = "root"
#ContraseñaUsuario
userPassword = ""
#PuertoDeConexion
conexionPort = "3306"

#servidorConexion
conexionServer = "localhost"

#creando la conexion
connetionToDataBase = f"mysql+mysqlconnector://{userName}:{userPassword}@{conexionServer}:{conexionPort}/{dataBaseName}"

engine=create_engine(connetionToDataBase)
sessionLocal=sessionmaker(autocommit=False,autoflush=False, bind=engine)