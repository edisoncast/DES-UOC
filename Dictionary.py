#Creado por Jhon Edison Castro Sánchez
#Diccionario tomado de https://github.com/danielmiessler/SecLists/blob/bb915befb208fd900592bb5a25d0c5e4f869f8ea/Passwords/Leaked-Databases/rockyou.txt.tar.gz

#Se usa para generar el mismo comportamiento de openssl de linux
#https://docs.python.org/2/library/crypt.html
import crypt

#Funcion que me permite generar los hash de las palabras de 8 caracteres
#Se usa el hash dado en la PEC
#La salida es un archivo con un par de valores por linea
#la primera es el hash y al frente el valor del password en texto plano
def generateHash(filename, outputfilename, salt):
    with open(outputfilename, "w") as out:
        with open(filename,'r')as f:
            for line in f:
                Hash = crypt.crypt(line, salt)
                result = " ".join([Hash, line])
                print result
                out.write(result + "\n")

#Funcion que recibe el archivo de entrada y el de salida y llama a otra funcion
#que valida el tamaño de los strings
def DESDictionary(filename,outputFile):
    plaintext = inputText(filename, outputFile)

#Funcion que verifica cada linea y si es de 8 caracteres me genera un archivo nuevo
#Con esto ya puedo generar los hash y comparar.
def inputText(filename, outputfilename):
    with open(outputfilename, "w") as out:
        with open(filename,'r')as f:
            for line in f:
                if len(" ".join(line.split())) == 8:
                    print line
                    out.write(line)

#Llamado a las funciones

if __name__ == "__main__":
    with open('rockyou.txt','r')as f:
        text = f.read()
    DESDictionary('rockyou.txt','pec1.txt')
    salt1='tl'
    salt2='as'
    generateHash('pec1.txt','hashed1.txt', salt1)
    generateHash('pec1.txt','hashed2.txt', salt2)