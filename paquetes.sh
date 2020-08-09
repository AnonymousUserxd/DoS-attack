#!/usr/bin/bash

echo 'COMENZANDO INSTALACIÓN DE LOS PAQUETES NECESARIOS :V'

apt-get update && apt-get upgrade -y
pip3 install requests
pip3 install pysocks
pip3 install socks

echo '-----------------------------------------------------------------------------------'
echo 'SE HAN INSTALADO LOS PAQUETES NECESARIOS,EJECUTA LA HERRAMIENTA CON python3 DoS.py'
echo '-----------------------------------------------------------------------------------'
