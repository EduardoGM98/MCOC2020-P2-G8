# MCOC2020-P2-G8
# Entrega 4

1. Escoja 5 barras interesantes del reticulado (identificadas por sus nodos) y manualmente realice el rediseño, buscando minimizar el peso de la barra y cumplir con FU < 1.0 pero cerca a 1.0 comparando con los resultados de su programa. <br>

![alt text](https://github.com/EduardoGM98/MCOC2020-P2-G8/blob/master/5barras%20caso2.png) 
  - R.
    - Barra: 3, nodos 0-8
    - Barra: 6, nodos 1-5
    - Barra: 11, nodos 2-5
    - Barra: 23, nodos 5-8
    - Barra: 24, nodos 5-9
   
  Para realizar manualmente el rediseño se utilizó una planilla excel, la cual contenía todas las variables y parámetros necesarios. La idea fue ir analizando de qué manera afectaba la variación de los parámetros “R” y “t” dentro del modelo, con los que se fue iterando para obtener el mayor valor del FU de cada barra, respetando las condiciones de tracción y compresión. 

2. Explique en detalle su función de rediseño de cada barra. Si existen supuestos importantes, declararlos ahora.

  - R. Hicimos 4 supuesto importantes: FU > 0.95, FU <= 1, landa < 300, Fn x ϕ >= Fu. Podemos entender el factor de utilidad como un indicador de cuánta tensión soporta cada barra, este factor es la división entre la fuerza última y la fuerza nominal reducida. Este factor no debe ser mayor a 1 ya que de lo contrario no sería una estructura segura, pero lo óptimo (para aprovechar al máximo los recursos) es que sea un valor cercano a 1. Por otro lado, la esbeltez (lambda) se define como el largo de la barra dividido por el radio de giro de la barra. Este valor debe superar 300 ya que de esta forma se puede controlar el diseño de elementos que soportan muy poca carga. <br>
  ![alt text](https://github.com/EduardoGM98/MCOC2020-P2-G8/blob/master/landa.png)
3. Mostrar los nuevos factores de utilización, fuerzas en las barras y deformada para cada combinación de carga. Para esto, graficando todo lo pedido y explicando sus criterios de rediseño. ¿Cual es el desplazamiento vertical máximo en los nodos del tablero del reticulado antes y después de los cambios?

  - R. 
  
  Tensiones caso 1, 1,4D
  
  ![alt text](https://github.com/EduardoGM98/MCOC2020-P2-G8/blob/master/Tensiones_caso_1.png)
  
  Tensiones caso 2, 1,2D x 1,6L
  
  ![alt text](https://github.com/EduardoGM98/MCOC2020-P2-G8/blob/master/Tensiones_caso_2.png)
  
  ![alt text](https://github.com/EduardoGM98/MCOC2020-P2-G8/blob/master/FU_caso_1.png)
  ![alt text](https://github.com/EduardoGM98/MCOC2020-P2-G8/blob/master/FU_caso_2.png)
  
  Para rediseñar nos centramos en que se cumplan las siguientes condiciones: FU < 1 pero siendo cercano a 1, lambda < 300 y que Fn*sigma < Fu


4. Comente respecto de la nueva distribución de F U del reticulado y el peso del mismo. ¿Qué cambios globales se pueden hacer para mejorar aún más el costo (peso del acero) del mismo?

  - R. Para poder seguir disminuyendo el peso del reticulado se podría utilizar otro tipo de acero que sea menos denso que el que estamos utilizando pero que también pueda soportar las solicitaciones. 
