# MCOC2020-P2-G8
# Entrega 4

1. Escoja 5 barras interesantes del reticulado (identificadas por sus nodos) y manualmente realice el rediseño, buscando minimizar el peso de la barra y cumplir con FU < 1.0 pero cerca a 1.0 comparando con los resultados de su programa. <br>
 
  - R.
    - Barra: 3, nodos 0-8
    - Barra: 6, nodos 1-5
    - Barra: 11, nodos 2-5
    - Barra: 23, nodos 5-8
    - Barra: 24, nodos 5-9
   
  Para realizar manualmente el rediseño se utilizó una planilla excel, la cual contenía todas las variables y parámetros necesarios. La idea fue ir analizando de qué manera afectaba la variación de los parámetros “R” y “t” dentro del modelo, con los que se fue iterando para obtener el mayor valor del FU de cada barra, respetando las condiciones de tracción y compresión. 
  
  Los resultados para las distintas barras fueron:
  - Barra Nº3:
  ![Captura de Pantalla 2020-10-13 a la(s) 23 23 12](https://user-images.githubusercontent.com/69252038/95936058-1488a400-0dab-11eb-8943-253bacb034b3.png)
  - Barra Nº6, Nº11, Nº23, Nº24:
  ![Captura de Pantalla 2020-10-13 a la(s) 23 29 10](https://user-images.githubusercontent.com/69252038/95936428-efe0fc00-0dab-11eb-9c7d-13e2aae29887.png)
  
  - En resumen:
  
  ![Captura de Pantalla 2020-10-13 a la(s) 23 31 02](https://user-images.githubusercontent.com/69252038/95936528-2b7bc600-0dac-11eb-92c9-760f9f282f39.png)
  
  Podemos notar que los numeros de FU son pequeños y distintos a los valores obtenidos por el programa, esto se debe a que elegimos las barras con menores cargas dentro del reticulado para disminuir en mayor cantidad el peso total de la estructura. Además, consideramos valores minimos para los parametros R y t, siendo 1cm y 1mm, respectivamente, para aferrarnos un poco a un caso real de estructura, y solo se pueda aumentar o disminuir su magnitud en 1cm o 1mm. Un ejemplo es que el radio de las barras no podia ser 3.5 cm, puede ser o 3cm o 4cm. 
  
![alt text](https://github.com/EduardoGM98/MCOC2020-P2-G8/blob/master/5barras%20caso1FINAL.png)
![alt text](https://github.com/EduardoGM98/MCOC2020-P2-G8/blob/master/5barras%20caso2.png)

 Los valores del programa consideraron valores intermedios, esto quiere decir que no se consideraron las limitaciones definidas anteriormente para los valores de R y t. Por lo tanto el radio si podia encontrarse en valores decimales al igual que el espesor de esta. Es por eso que los valores de FU entregados por el programa son bastante mas cercanos a 1.

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
  
  Para rediseñar nos centramos en que se cumplan las siguientes condiciones: FU < 1 pero siendo cercano a 1, lambda < 300 y que Fn*sigma < Fu <br>
  En relacion con los desplazamientos nodales, los del modelo original son los siguienes: <br>
  [0.0
,-0.0001103099784649426
,-0.00011030997846494263
,0.0
,-5.954476607643114e-05
,-0.00011590512712154298
,-5.9544766076431144e-05
,0.0
,-0.00010783378797162111
,-0.00010783378797162112
,0.0] para cada nodo.<br>

  


4. Comente respecto de la nueva distribución de F U del reticulado y el peso del mismo. ¿Qué cambios globales se pueden hacer para mejorar aún más el costo (peso del acero) del mismo?

  - R. Para poder seguir disminuyendo el peso del reticulado se podría utilizar otro tipo de acero que sea menos denso que el que estamos utilizando pero que también pueda soportar las solicitaciones. 
