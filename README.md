# Cifrado y descifrado con Python para los API de Pagos con Tarjetas de Banco Mercantil

## Instalar los requerimientos

`pip install -r requirements.txt`

#

## Crear un archivo llamado `.env`

Agregar la `clave de cifrado` proporcionada por Banco Mercantil

```
ENCRYPTION_KEY=X0X0X0X0X0X0X0X0X0X0X0X0X
```

#

## Usar el script para cifrar un mensaje

### Parámetros
- modo: string 'e'
- mensaje: string

### Comando:
```
python AesCipher.py e 1234
```

### Respuesta:

```
+WF8heuk635xQdclWotJqQ==
```
#

## Usar el script para descifrar un mensaje

### Parámetros
- modo: string 'd'
- mensaje: string cifrado

### Comando:
```
python AesCipher.py d +WF8heuk635xQdclWotJqQ==
```
### Respuesta:

```
1234
```