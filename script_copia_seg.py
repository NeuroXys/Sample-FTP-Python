import tarfile
import os
import datetime
import ftplib
import smtplib
from email.message import EmailMessage


#Nombre del tar
fecha = datetime.datetime.now().strftime("%Y%m%d--%M-%S")
zip = "backup" + fecha + ".zip"

#Nos movemos al directorio del que deseamos hacer la copia de seguridad
os.chdir(r"USER-DIRECTORY")
directorio = os.getcwd() + "\\"
print()
print("Directorio actual: " , directorio)

#Listamos los archivos del directorio
contenido = os.listdir(directorio)

#Creamos el tar
print()
print("Creando archivo tar...")
with tarfile.open(zip, "w") as tar:
    for archivo in contenido:
        tar.add(archivo)

#Listamos el contenido del tar
print()
print("Contenido del tar:")
tar = tarfile.open(zip, "r")
for item in tar:
    print(item.name + ": " + str(item.size) + " bytes")

tar.close()

#Nos conectamos al servidor FTP
servidor = "IP"
usuario = "USER"
contraseña = "PASSWORD"
rutaDestino = "ROOT DIRECTORY"
print()
print("Conectando al servidor FTP...")
ftp = FTP_TLS(servidor, usuario, contraseña)
ftp.cwd(rutaDestino)
#Comprobamos que nos hemos conectado correctamente, listando el contenido del directorio
print("Contenido del directorio:")
ftp.retrlines('LIST')

#Comprobamos que el directorio no está lleno
listaZips = ftp.nlst()
count = 0
for archivo in listaZips:
    count += 1
    if count >= 10:
        print("El directorio está lleno. Borrando el archivo más antiguo...")
        ftp.delete(listaZips[0])

#Subimos el tar al servidor FTP
print()
print("Subiendo el tar al servidor FTP...")
f = open(zip, 'rb')
ftp.cwd(rutaDestino)
#open(zip, 'wb')
ftp.storbinary('STOR ' + zip, f)
f.close()
print("Contenido del directorio:")
ftp.retrlines('LIST')
ftp.quit()

#Comprobamos que el archivo se ha subido correctamente
for archivo in listaZips:
    if archivo == zip:
        print("El archivo se ha subido correctamente")
        ftp.quit()
        exit()

#Borramos el tar local
os.remove(zip)


#Enviamos un correo de notificación
print()
print("Enviando correo de notificación...")
asunto = "Copia de seguridad realizada"
remitente = "MAIL"
destinatario = "MAIL"
email_smtp = "smtp.gmail.com"
contraseña = "DEVICE MAIL PASSWORD"
mensaje = EmailMessage()
mensaje['Subject'] = asunto
mensaje['From'] = remitente
mensaje['To'] = destinatario
mensaje.set_content("Copia de seguridad realizada correctamente")
servidor = smtplib.SMTP(email_smtp, '587')
servidor.ehlo()
servidor.starttls()
servidor.login(remitente, contraseña)
servidor.send_message(mensaje)
servidor.quit()
print("Correo enviado correctamente")