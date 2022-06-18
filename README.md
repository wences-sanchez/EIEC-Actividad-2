# Ampliaciones para la práctica

1. Se ha incluido una label master para adaptar el Jenkinsfile al nodo local localhost:8080
2. Se ha instalado Docker y se han añadido _$USER_ y _jenkins_ al grupo docker para poder ejecutarlo sin _sudo_.
3. Se han añadido todos los stages pedidos.
4. Se ha modificado uno de los puertos usados en el script porque entraba en conflicto con uno local.


# Repo para EIEC - DevOps - UNIR

Este repositorio incluye un proyecto sencillo para demostrar los conceptos de pruebas unitarias, pruebas de servicio o de API y pruebas E2E o de GUI. El objetivo es que el alumno entienda estos conceptos, por lo que el código y la estructura del proyecto son especialmente sencillos.

El Makefile ofrece comandos para facilitar la creación de imágenes de Docker y la ejecución de las pruebas. El único requisito es tener Docker instalado. Los comandos funcionarán en MacOS y Linux. En caso de usar Windows, será necesario adaptarlos o ejecutarlos en una máquina virtual Linux con Docker instalado.
