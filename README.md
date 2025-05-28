# Port Scanner en Python

Este es un escáner de puertos TCP escrito en Python que permite detectar qué puertos están abiertos en una dirección IP específica, es compatible con rangos o listas de puertos.

---

## Características

- Soporte para rangos (`1-1000`) y listas de puertos (`22,80,443`)
- Gestión de señales con `Ctrl+C` para salida limpia
- Colores en la salida con `termcolor` (opcional)

---

### Dependencia opcional:
 [`termcolor`](https://pypi.org/project/termcolor/) para salida con colores:
 
  ```bash
  pip install termcolor
  ```
![image](https://github.com/user-attachments/assets/e1e220b1-ce07-43a7-92c1-cf2510238423)

##  Uso
```bash
python3 port_scanner.py -t <IP> -p <PUERTOS>
```
Argumentos obligatorios:

- `-t, --target:` Dirección IP del objetivo (por ejemplo: 192.168.1.1)

- `-p, --port:` Puertos a escanear.

Puedes usar:

- Un rango: 1-1000

- Una lista separada por comas: 22,80,443

- Un único puerto: 80

--- 
### Si estás en Linux, puedes hacer el script ejecutable:

```bash
chmod +x port_scanner.py
./port_scanner.py -t <IP> -p <PUERTOS>
```
