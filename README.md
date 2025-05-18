# Evaluación Comparativa: Virtualización Completa vs Contenerización con Docker

## 1. Panorama General

Las tecnologías de aislamiento de entornos han evolucionado significativamente en las últimas décadas. Entre las más relevantes hoy en día se encuentran las **máquinas virtuales (VMs)** y los **contenedores Docker**. Ambas se utilizan para ejecutar aplicaciones en entornos separados del sistema principal, pero lo hacen de formas muy diferentes.

Las **VMs** virtualizan hardware completo y operan sistemas operativos independientes.
Los **contenedores**, en cambio, aprovechan el kernel del sistema anfitrión, lo que permite un entorno más ligero y con menor sobrecarga.

Este informe presenta un estudio práctico donde se implementó una misma aplicación web desarrollada con Flask en ambos entornos, con el objetivo de comparar su rendimiento bajo condiciones similares de prueba.

---

## 2. Entorno de Evaluación

### 2.1 Plataforma de Pruebas (Host Físico)

**Modelo del equipo:**  
**Procesador:**  
**Memoria RAM instalada:**  
**Sistema operativo anfitrión:**  

### 2.2 Entorno Virtualizado

**Hipervisor empleado:** VirtualBox  
**Sistema operativo invitado:** Ubuntu  
**Configuración de CPU:** 3 núcleos asignados  
**Memoria RAM:** 3 GB (modo dinámico)  
**Software de pruebas:** Python 3, Flask  

### 2.3 Contenedor Docker

**Imagen base utilizada:** python:3.10-slim  
**Aplicación desplegada:** Servidor Flask simple para pruebas de latencia

---

## 3. Instrumentación y Métricas

Se desarrolló un script de benchmarking en Python que simula una carga real al enviar solicitudes HTTP a una ruta expuesta por la aplicación Flask durante un intervalo continuo de 60 segundos. Las métricas recolectadas incluyen:

Latencia de cada solicitud HTTP  
Uso promedio, máximo y mínimo de CPU  
Uso promedio, máximo y mínimo de memoria RAM  
Espacio ocupado por el entorno en disco  
Total de peticiones procesadas exitosamente  
Estimación del tráfico de red generado  

Todos los datos se registraron en archivos .csv y fueron utilizados posteriormente para generar gráficos comparativos y realizar un análisis visual del comportamiento de ambas plataformas.

---

## 4. Resultados

Los resultados de la prueba están disponibles en formato gráfico en la carpeta /results/ del repositorio. Los indicadores que se compararon visualmente incluyen:

Latencia media, máxima y mínima por entorno  
Consumo de CPU a lo largo del tiempo  
Evolución del uso de memoria RAM durante la carga  
Espacio ocupado por Docker y la VM  
Número de solicitudes procesadas en el mismo tiempo  
Tráfico de red estimado  

Estos datos permiten identificar claramente las diferencias de eficiencia entre ambos enfoques.

---

## 5. Análisis Comparativo

### Docker

**Ventajas:**

Inicio rápido y bajo consumo de recursos  
Excelente portabilidad entre entornos  
Escalable y fácil de integrar en pipelines de CI/CD  
Ideal para aplicaciones ligeras o microservicios  

**Desventajas:**

Aislamiento más superficial  
Dificultades al trabajar con interfaces gráficas o sistemas operativos complejos  

---

### Máquina Virtual

**Ventajas:**

Entorno completamente aislado del host  
Permite emulación precisa de sistemas heterogéneos  
Mayor control sobre la configuración del entorno  

**Desventajas:**

Consumo considerable de RAM y CPU  
Mayor latencia de arranque y más compleja administración  
Menor eficiencia en tareas pequeñas o repetitivas  

---

## 6. Conclusión

Ambas tecnologías son herramientas poderosas, y su elección debe responder al contexto del proyecto. Docker destaca en escenarios donde la rapidez, el bajo consumo de recursos y la portabilidad son críticos, como en microservicios o pruebas automatizadas.

En contraste, las máquinas virtuales son más apropiadas para entornos que requieren aislamiento completo, simulación de diferentes sistemas operativos o una separación estricta de recursos.

Lejos de ser excluyentes, Docker y las VM pueden coexistir e incluso complementarse, dependiendo de las necesidades de despliegue y pruebas.
