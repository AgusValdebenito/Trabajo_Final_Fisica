FÍSICA  
INGENIERÍA EN INFORMÁTICA  
 
 
TRABAJO FINAL INTEGRADOR  
________________________________________  
 
Título del trabajo: Modelar para Comprender:  
 
Subtítulo: Una experiencia de aprendizaje en Física basada en  
simulación computacional e Inteligencia Artificial  
en Ingeniería Informática  
 
Autor: Ruben Eduardo Gallart  
Primera Cohorte 2025 - 2026  
Lugar y fecha: Mendoza, Argentina — Marzo de 2026

2 
Resumen  
El presente Trabajo Final Integrador aborda la problemática de la baja motivación y la postergación 
sistemática de exámenes en la asignatura Física, correspondiente al segundo año de la carrera de 
Ingeniería en Informática de la Universidad de Mendoza, sed e San Rafael. Históricamente, los estudiantes 
percibían la materia como desvinculada de su campo profesional, lo que derivaba en tasas elevadas de 
postergación de la evaluación final —en algunos casos de tres a cuatro años — y en un desinterés 
generalizado durante el cursado.  
Como respuesta a este problema pedagógico, se diseñó e implementó una experiencia de aprendizaje 
basada en la modelización y simulación computacional de fenómenos físicos mediante programación en 
Python, con integración regulada de herramientas de intelige ncia artificial como asistentes de aprendizaje. 
La propuesta contempla una secuencia didáctica de cinco instancias que articula la comprensión 
conceptual de la Física con el pensamiento computacional propio de la Ingeniería en Informática.  
Los resultados de la implementación piloto durante 2025 evidencian un impacto significativo: dos 
estudiantes —pertenecientes a cohortes  2025— se presentaron a mesa de evaluación final en marzo de 
2026 con simulaciones computacionales funcionales como trabajo integrador. Este resultado constituye 
una evidencia concreta de mejora en la motivación, el compromiso académico y la reducción de los 
tiempos de acreditación. Se concluye que la integración disciplinar mediada por modelización 
computacional representa un enfoque pedagógico eficaz, ético y transferible a otros contextos de la 
educación superior en ciencias e ingeniería.  
Palabras clave  
modelización, simulación, enseñanza, motivación, integración IA. 
Indicaciones de formato  
• Fuente sugerida: Calibri 11 o Poppins 11.  
• Interlineado sugerido: 1,5.  
• Sistema de citación y referencias: APA 7.ª edición.

3 
Índice  
Tabla de contenido  
RESUMEN  ................................ ................................ ................................ ................................ ................................ .......................  2 
PALABRAS CLAVE  ................................ ................................ ................................ ................................ ................................ ..............................  2 
INDICACIONES DE FORMATO ................................ ................................ ................................ ................................ ................................ ............  2 
ÍNDICE  ................................ ................................ ................................ ................................ ................................ ............................  3 
1. INTRODUCCIÓN  ................................ ................................ ................................ ................................ ................................ ...... 5 
1.1 OBJETIVOS  ................................ ................................ ................................ ................................ ................................ ................................ ... 6 
Objetivos específicos  ................................ ................................ ................................ ................................ ................................ ...............  6 
2. MARCO CONCEPTUAL  ................................ ................................ ................................ ................................ ...........................  6 
2.1 APRENDIZAJE SIGNIFICATIVO Y CONTEXTUALIZACIÓN DISCIPLINAR  ................................ ................................ ................................ . 6 
2.2 CONSTRUCTIVISMO Y APRENDIZAJE ACTIVO  ................................ ................................ ................................ ................................ ..........  7 
2.3 MODELIZACIÓN COMO ESTRATEGIA DIDÁCTICA EN FÍSICA  ................................ ................................ ................................ .................  7 
2.4 MOTIVACIÓN , IDENTIDAD PROFESIONAL Y STEM  ................................ ................................ ................................ ...............................  7 
2.5 INTELIGENCIA ARTIFICIAL EN EDUCACIÓN : POTENCIAL Y LÍMITES  ................................ ................................ ................................ .... 8 
3. DESARROLLO DEL TRABAJO  ................................ ................................ ................................ ................................ ..............  8 
3.1 CONTEXTO DE APLICACIÓN Y DESTINATARIOS  ................................ ................................ ................................ ................................ ...... 8 
3.2 PROPÓSITO PEDAGÓGICO  ................................ ................................ ................................ ................................ ................................ ..........  9 
3.3 SECUENCIA DIDÁCTICA  ................................ ................................ ................................ ................................ ................................ ..............  9 
3.4 INTEGRACIÓN DE INTELIGENCIA ARTIFICIAL  ................................ ................................ ................................ ................................ ..... 10 
¿Para qué se utiliza la IA?  ................................ ................................ ................................ ................................ ................................ . 10 
¿En qué momento se habilita el uso de IA?  ................................ ................................ ................................ ................................  11 
¿Qué no se delega en la IA?  ................................ ................................ ................................ ................................ ...............................  11 
¿Cómo se valida el uso de IA? ................................ ................................ ................................ ................................ ...........................  11 
3.5 RECURSOS Y MATERIALES ................................ ................................ ................................ ................................ ................................ ...... 11 
4. RESULTADOS, ANÁLISIS O REFLEXIÓN  ................................ ................................ ................................ .......................  12 
4.1 PONDERACIÓN  ................................ ................................ ................................ ................................ ................................ .........................  13 
5. RESULTADOS, ANÁLISIS Y REFLEXIÓN PEDAGÓGICA  ................................ ................................ ............................  14 
5.1 DESCRIPCIÓN DE LA IMPLEMENTACIÓN PILOTO  ................................ ................................ ................................ ................................  14 
5.2 EVIDENCIAS DE IMPACTO  ................................ ................................ ................................ ................................ ................................ ...... 14 
5.3 ANÁLISIS PEDAGÓGICO  ................................ ................................ ................................ ................................ ................................ ...........  14 
5.4 VIABILIDAD Y CONDICIONES DE IMPLEMENTACIÓN  ................................ ................................ ................................ ..........................  15

4 
6. DIMENSIÓN ÉTICA Y VIABILIDAD  ................................ ................................ ................................ ................................ . 16 
6.1 IDENTIFICACIÓN DE RIESGOS Y ESTRATEGIAS DE MITIGACIÓN  ................................ ................................ ................................ ........ 16 
6.2 DECLARACIÓN DE USO RESPONSABLE DE INTELIGENCIA ARTIFICIAL  ................................ ................................ ............................  17 
7. CONCLUSIONES  ................................ ................................ ................................ ................................ ................................ .... 18 
8. REFERENCIAS BIBLIOGRÁFICAS  ................................ ................................ ................................ ................................ .... 19 
9. ANEXOS ................................ ................................ ................................ ................................ ................................ ...................  20 
ANEXO A: EJEMPLO DE SIMULACIÓN — TIRO PARABÓLICO 2D EN PYTHON  ................................ ................................ ......................  20 
ANEXO B: GUÍA DE CONSIGNAS — CLASE 1 (INTRODUCCIÓN CONCEPTUAL ) ................................ ................................ .....................  21 
ANEXO C: REGISTRO DE USO DE IA — INSTRUMENTO PARA ESTUDIANTES  ................................ ................................ ........................  21 
10. VÍNCULOS  ................................ ................................ ................................ ................................ ................................ ............  22

5 
1. Introducción  
La enseñanza de la Física en carreras de Ingeniería plantea desafíos persistentes que trascienden lo 
meramente disciplinar y alcanzan dimensiones motivacionales, identitarias y pedagógicas. En el caso 
particular de los estudiantes de Ingeniería en Informát ica, esta problemática adopta una configuración 
específica: la percepción generalizada de que los contenidos físicos no guardan relación directa con su 
futuro campo profesional genera una desconexión que se traduce en desinterés, bajo compromiso y, en 
última instancia, en la postergación sistemática de la instancia de evaluación final.  
En la asignatura Física del segundo año de la carrera de Ingeniería en Informática de la Universidad de 
Mendoza, sede San Rafael, esta dinámica ha sido observada de forma consistente durante cohortes 
sucesivas. Los estudiantes tienden a cursar la materia s in llegar a rendir el examen final, postergándolo 
durante períodos que en muchos casos se extienden entre tres y cuatro años. Esta situación no solo afecta 
el trayecto académico individual, sino que también impacta negativamente en los índices de graduació n y 
en la formación integral de los futuros ingenieros.  
Frente a este escenario, el presente Trabajo Final Integrador propone una reconfiguración del enfoque 
pedagógico de la asignatura, orientada a resignificar el aprendizaje de la Física a través de la integración 
de la modelización y simulación computacional . La hipótesis central del trabajo sostiene que cuando los 
estudiantes logran vincular los contenidos físicos con herramientas propias de su campo disciplinar —en 
este caso, la programación en Python —, se incrementa significativamente tanto la motivación c omo la 
calidad de la comprensión conceptual.  
La propuesta incorpora además el uso pedagógicamente regulado de herramientas de inteligencia artificial 
como asistentes de aprendizaje, estableciendo límites claros que garantizan que la IA potencie el proceso 
cognitivo del estudiante sin sustituirlo. Est a decisión pedagógica responde a una reflexión ética 
fundamentada sobre el rol que deben desempeñar las tecnologías emergentes en los procesos de 
enseñanza y evaluación.  
El trabajo se estructura en seis secciones principales. Tras esta introducción, se presenta el marco 
conceptual que fundamenta la propuesta; luego se describe en detalle el desarrollo de la experiencia de 
aprendizaje, incluyendo la secuencia didáctica y lo s criterios de evaluación; posteriormente se exponen 
los resultados obtenidos y la reflexión pedagógica derivada; a continuación, se desarrolla la dimensión 
ética del proyecto; y finalmente se presentan las conclusiones, las referencias bibliográficas y lo s anexos 
correspondientes.

6 
1.1 Objetivos  
Objetivo general  
Diseñar e implementar una experiencia de aprendizaje que integre modelización computacional e 
inteligencia artificial para mejorar la motivación y la comprensión conceptual de los estudiantes de Física 
en la carrera de Ingeniería en Informática de la Unive rsidad de Mendoza, sede San Rafael.  
Objetivos específicos  
• Desarrollar una secuencia didáctica articulada en cinco instancias que integre contenidos de Física 
con herramientas de programación en Python.  
• Diseñar e implementar una rúbrica de evaluación analítica que contemple la corrección del 
modelo físico, la calidad del código y la profundidad del análisis crítico.  
• Incorporar el uso regulado y éticamente fundamentado de herramientas de inteligencia artificial 
como asistentes de aprendizaje.  
• Sistematizar y analizar los resultados de la implementación piloto realizada durante el segundo 
semestre de 2025.  
• Identificar los riesgos éticos de la propuesta y definir estrategias concretas de mitigación.  
2. Marco conceptual  
El presente trabajo se fundamenta en una convergencia de perspectivas teóricas provenientes de la 
didáctica de las ciencias, la psicología educativa, la teoría del aprendizaje y los estudios sobre integración 
de tecnología en educación. A continuación, se desarrollan los ejes conceptuales que articulan y justifican 
las decisiones pedagógicas de la propuesta.  
2.1 Aprendizaje significativo y contextualización disciplinar  
La teoría del aprendizaje significativo, desarrollada por David Ausubel (1968), sostiene que el conocimiento 
se construye de manera duradera cuando los nuevos contenidos se integran de forma sustantiva con los 
saberes previos del aprendiz. En este marco, l a clave del aprendizaje no reside en la mera transmisión de 
información, sino en la capacidad de establecer conexiones relevantes entre los contenidos nuevos y el 
contexto cognitivo y experiencial del estudiante.  
En el caso de los estudiantes de Ingeniería en Informática, la programación constituye precisamente ese 
dominio de conocimiento familiar y significativo que puede funcionar como "anclaje" para los conceptos 
físicos. Al vincular fenómenos como el tiro parab ólico o el movimiento oscilatorio con su representación 
algorítmica en Python, los estudiantes no solo comprenden la Física: la resignifican desde su propia 
identidad disciplinar.

7 
Ausubel (1968) afirmó que el factor más importante que influye en el aprendizaje es lo que el alumno ya 
sabe; averígüese esto y enséñese en consecuencia (citado en Moreira, 2000).  
2.2 Constructivismo y aprendizaje activo  
Desde la perspectiva constructivista —representada por autores como Jean Piaget (1970) y Lev Vygotsky 
(1978)—, el aprendizaje es un proceso activo en el cual el sujeto no reproduce conocimientos,  sino que los 
construye a partir de la interacción con problemas, herramientas y contextos. Esta visión implica que la 
comprensión genuina requiere de experiencias en las que el estudiante deba operar sobre la realidad, 
tomar decisiones y verificar sus hip ótesis.  
La modelización computacional se inscribe plenamente en esta lógica. Desarrollar una simulación implica 
representar matemáticamente un fenómeno, traducir esa representación a código funcional, ejecutar el 
modelo, observar su comportamiento y ajustarlo segú n los resultados obtenidos. Este ciclo —que se puede 
equiparar a la metodología científica — promueve una comprensión activa y profunda que difícilmente se 
alcanza mediante la resolución de ejercicios convencionales.  
Vygotsky aporta además el concepto de Zona de Desarrollo Próximo (ZDP), que describe la distancia entre 
lo que un estudiante puede lograr de forma autónoma y lo que puede lograr con apoyo adecuado. En esta 
propuesta, tanto el docente como las herramientas de inteligencia artificial cumplen el rol de andamiaje, 
guiando al estudiante hacia niveles de comprensión que difícilmente alcanzaría sin ese acompañamiento.  
2.3 Modelización como estrategia didáctica en Física  
En el ámbito específico de la enseñanza de la Física, la modelización ha sido reconocida como una 
estrategia central para el desarrollo del pensamiento científico. David Hestenes (1987), en su trabajo 
pionero sobre la instrucción basada en modelos, argumen tó que la Física es fundamentalmente una 
ciencia de modelos y que enseñarla de manera efectiva requiere que los estudiantes aprendan no solo los 
contenidos conceptuales sino también los procesos de modelización.  
Modelar implica un conjunto de operaciones cognitivas complejas: identificar variables relevantes de un 
fenómeno, establecer relaciones cuantitativas entre ellas, formular ecuaciones que las representen, 
implementar esas ecuaciones en un sistema computacio nal, verificar la validez del modelo mediante 
comparación con datos o comportamientos esperados y analizar críticamente los resultados. Este proceso 
no solo permite comprender fenómenos específicos, sino también desarrollar habilidades epistémicas 
transfer ibles a otros dominios del conocimiento científico e ingenieril.  
2.4 Motivación, identidad profesional y STEM  
La literatura sobre motivación en contextos STEM  (ciencias, tecnología, ingeniería y matemáticas) señala 
de manera consistente que la percepción de relevancia y la identidad disciplinar son factores 
determinantes del compromiso estudiantil. Cuando los estudiantes no logran visualizar la utilidad de una

8 
asignatura en relación con su campo profesional, tienden a priorizar otras materias y a postergar la 
evaluación (Eccles et al., 1983; Wigfield & Eccles, 2000).  
En carreras como Ingeniería en Informática, esta dinámica es especialmente pronunciada en asignaturas 
consideradas "básicas" como la Física. La integración de herramientas de programación en el aprendizaje 
de la Física tiene el potencial de modificar esa p ercepción, mostrando de manera concreta y práctica cómo 
los principios físicos son relevantes para el desarrollo de sistemas computacionales, simulaciones, 
videojuegos, robótica y una multiplicidad de aplicaciones tecnológicas.  
2.5 Inteligencia artificial en educación: potencial y límites  
La incorporación de herramientas de inteligencia artificial en el ámbito educativo abre posibilidades 
pedagógicas significativas, pero también plantea desafíos éticos y epistemológicos que deben ser 
abordados con rigor. Holmes, Bialik y Fadel (2019) distin guen entre usos de la IA que potencian el 
aprendizaje —cuando se utilizan para facilitar la exploración, la retroalimentación y la metacognición — y 
usos que lo obstaculizan —cuando sustituyen el esfuerzo cognitivo del estudiante o generan ilusiones de 
comp rensión.  
En el marco de esta propuesta, la IA se concibe como un asistente de aprendizaje y no como un sustituto 
del proceso de modelización. Los estudiantes pueden consultar herramientas de IA para explorar 
explicaciones conceptuales, verificar fragmentos de códig o, sugerir alternativas de implementación o 
discutir posibles modelos. Sin embargo, la programación de la simulación, la interpretación de los 
resultados y la defensa oral del trabajo son responsabilidad exclusiva del estudiante.  
Esta distinción es crucial tanto pedagógica como éticamente: garantiza que la evaluación mida 
comprensión genuina y no ejecución mecánica mediada por tecnología.  
3. Desarrollo del trabajo  
3.1 Contexto de aplicación y destinatarios  
La propuesta se implementa en la asignatura Física correspondiente al segundo año de la carrera de 
Ingeniería en Informática de la Universidad de Mendoza, sede San Rafael. La asignatura se dicta durante 
el segundo semestre del año académico, con una carga horaria de tres horas semanales distribuidas en 
una clase por semana.  
El grupo destinatario está conformado por aproximadamente 20 estudiantes por cohorte. Un rasgo 
distintivo del grupo es que sus integrantes cuentan con formación básica en programación adquirida en 
asignaturas previas de la carrera, lo que los dota de las h erramientas técnicas necesarias para abordar la 
modelización computacional sin requerir una capacitación paralela en programación básica.

9 
En cuanto a la disponibilidad de recursos tecnológicos, los estudiantes disponen de notebooks personales 
con conectividad a internet, lo que permite la instalación y uso de Python con sus bibliotecas científicas 
(NumPy, Matplotlib) sin depender de infraest ructura institucional específica. Esta condición favorece la 
viabilidad real de la propuesta y facilita su continuidad más allá del espacio áulico.  
3.2 Propósito pedagógico  
El propósito central de la propuesta es fortalecer la motivación y la comprensión conceptual de los 
estudiantes mediante la integración de la modelización computacional como puente entre Física e 
Informática. Este propósito se concreta en tres dimensiones interrelacionadas:  
Resignificación disciplinar: mostrar de manera práctica y concreta que la Física es relevante para el campo 
profesional de la Ingeniería en Informática.  
Comprensión profunda: promover un aprendizaje que vaya más allá de la memorización de fórmulas y 
algoritmos de resolución, hacia la comprensión de los principios físicos subyacentes.  
Desarrollo de competencias transversales: cultivar habilidades de modelización, pensamiento crítico y 
argumentación científica que resultan transferibles a múltiples contextos profesionales.  
3.3 Secuencia didáctica  
La secuencia didáctica se organiza en cinco instancias de tres horas cada una, diseñadas para guiar al 
estudiante desde la comprensión conceptual del fenómeno físico hasta la presentación y defensa de una 
simulación computacional funcional. La propuesta es  lo suficientemente flexible para aplicarse a distintos 
fenómenos del programa de la asignatura —movimiento uniformemente acelerado, tiro parabólico, 
oscilaciones, etc. —, siendo la elección del fenómeno específico responsabilidad del estudiante.  
 
Instancia  Título  Actividades principales  Producto esperado  
Clase 1 (3 h)  Introducción 
conceptual  Presentación del fenómeno físico 
elegido  
Discusión guiada sobre variables, 
condiciones y comportamiento esperado  
Exploración inicial con IA para clarificar 
conceptos  
Identificación de ecuaciones relevantes  Descripción del fenómeno 
y listado de variables con 
su significado físico  
Clase 2 (3 h)  Modelización 
matemática  Formulación de ecuaciones diferenciales 
o algebraicas del modelo  
Análisis dimensional y consistencia del 
modelo  
Definición de condiciones iniciales y 
valores de parámetros  Modelo matemático 
documentado con 
ecuaciones y justificación 
física

10 
Comparación del modelo con casos 
conocidos o datos experimentales  
Clase 3 (3 h)  Implementación 
en Python  Traducción del modelo matemático a 
código Python  
Uso de bibliotecas NumPy y Matplotlib 
para cálculo y visualización  
IA habilitada para consultas puntuales 
sobre sintaxis y errores  
Andamiaje docente diferenciado según 
nivel de programación  Código Python funcional 
con comentarios 
explicativos  
Clase 4 (3 h)  Simulación y 
análisis crítico  Ejecución del modelo y visualización de 
resultados  
Variación de parámetros y análisis del 
impacto en el comportamiento del 
sistema  
Identificación de limitaciones del modelo 
y posibles mejoras  
Redacción del análisis crítico de 
resultados  Informe de análisis con 
gráficos generados por la 
simulación  
Clase 5 (3 h)  Presentación y 
defensa oral  Exposición oral del fenómeno, modelo y 
simulación (15 min por grupo)  
Defensa ante preguntas del docente 
sobre decisiones de modelización  
Autoevaluación mediante rúbrica  
Retroalimentación grupal y reflexión 
sobre el proceso  Presentación oral y 
simulación funcional 
demostrable  
 
3.4 Integración de Inteligencia Artificial  
La integración de la IA en esta propuesta responde a una decisión pedagógica explícita y fundamentada: 
la IA actúa como asistente de aprendizaje que potencia el proceso cognitivo del estudiante, sin sustituirlo 
en las operaciones que requieren comprensión conceptual genuina.  
¿Para qué se utiliza la IA?  
• Exploración conceptual: los estudiantes pueden consultar a la IA para obtener explicaciones 
alternativas de conceptos físicos, aclarar dudas terminológicas o explorar analogías que faciliten 
la comprensión.  
• Verificación de fragmentos de código: la IA puede identificar errores de sintaxis o sugerir 
correcciones puntuales en porciones de código ya desarrollado por el estudiante.  
• Sugerencias de visualización: la IA puede orientar sobre cómo representar gráficamente los 
resultados de la simulación usando Matplotlib.

11 
• Retroalimentación formativa: durante el proceso de desarrollo, los estudiantes pueden usar la IA 
para obtener una primera evaluación de la coherencia física de su modelo.  
¿En qué momento se habilita el uso de IA?  
• Clase 1: se habilita para exploración conceptual inicial y clarificación de dudas sobre el fenómeno 
físico elegido.  
• Clase 3: se habilita de forma acotada para consultas sobre sintaxis de Python y resolución de 
errores puntuales. No se permite solicitar a la IA que genere el código completo de la simulación.  
• Clase 4: se habilita para revisar la coherencia del análisis crítico elaborado por el estudiante.  
¿Qué no se delega en la IA?  
• La programación completa de la simulación: el código debe ser desarrollado íntegramente por el 
estudiante.  
• La interpretación de resultados: el análisis crítico de los resultados de la simulación es 
responsabilidad exclusiva del estudiante.  
• La defensa oral: la presentación y defensa ante el docente no admite ningún tipo de asistencia de 
IA. 
¿Cómo se valida el uso de IA?  
Los estudiantes deben incluir en su entrega final un registro de los prompts utilizados con IA, indicando en 
qué momento de la tarea los emplearon y qué tipo de asistencia obtuvieron. El docente revisa estos 
registros durante la defensa oral, realizando pr eguntas específicas orientadas a verificar que el estudiante 
comprende y puede explicar cada decisión tomada en el modelo y en el código.  
3.5 Recursos y materiales  
La implementación de la propuesta requiere los siguientes recursos:  
 
Recurso  Descripción  
Python 3.x  Lenguaje de programación con bibliotecas NumPy (cálculo numérico) y Matplotlib 
(visualización gráfica). Instalación gratuita mediante Anaconda o pip.  
Herramientas de IA  Claude (Anthropic) o ChatGPT (OpenAI ) en versión gratuita. Se accede desde el 
navegador sin instalación adicional.  
Guía de trabajo  Documento de consignas elaborado por el docente para cada instancia, disponible 
en la plataforma institucional.  
Rúbrica de 
evaluación  Instrumento analítico con tres dimensiones y cuatro niveles de desempeño, 
compartido con los estudiantes desde la primera clase.

12 
Plataforma 
institucional  Entorno virtual de la Universidad de Mendoza para publicación de materiales, 
entrega de trabajos y comunicación con el docente.  
 
4. Resultados, análisis o reflexión  
La evaluación de la propuesta se realiza mediante una rúbrica analítica que contempla tres dimensiones 
fundamentales para valorar la calidad del trabajo de modelización: la corrección del modelo físico, la 
calidad del código desarrollado y la profundidad d el análisis crítico de los resultados. Esta estructura de 
evaluación permite distinguir con claridad entre comprensión conceptual genuina y ejecución mecánica 
de procedimientos.  
La rúbrica fue diseñada para cumplir una función tanto evaluativa como formativa: se comparte con los 
estudiantes desde el inicio de la experiencia, de modo que puedan utilizarla como guía de trabajo y 
autoevaluación a lo largo del proceso. La defensa oral  constituye además un componente evaluativo 
obligatorio que permite al docente verificar la comprensión individual y detectar posibles usos indebidos 
de IA.  
 
Dimensión  Nivel Inicial (1)  En desarrollo (2)  Avanzado (3)  Experto (4)  
1. Corrección 
del modelo 
físico ¿El 
fenómeno 
está 
correctamente 
representado?  El modelo presenta 
errores 
conceptuales que 
comprometen su 
validez. Las 
ecuaciones son 
incorrectas o están 
incompletas.  El modelo es 
parcialmente 
correcto. Hay 
algunas 
inconsistencias 
conceptuales o 
errores en la 
formulación de 
algunas relaciones.  El modelo es 
correcto en sus 
aspectos 
principales. Las 
ecuaciones son 
válidas y las 
condiciones 
iniciales están bien 
definidas.  El modelo es 
riguroso y 
fundamentado. Se 
justifican las 
simplificaciones 
adoptadas, se 
verifican los 
resultados y se 
identifican los 
límites de validez 
del modelo.  
2. Calidad del 
código Python 
¿El código es 
funcional, El código no es 
funcional o 
presenta errores El código es 
funcional de forma 
básica pero carece 
de estructura, 
comentarios o es El código es 
funcional, tiene 
estructura clara y 
cuenta con El código es 
eficiente, modular, 
bien documentado 
y reproducible. 
Incluye manejo de

13 
legible y 
reproducible?  que impiden su 
ejecución.  difícil de 
interpretar.  comentarios que 
facilitan su lectura.  casos límite y 
produce 
visualizaciones de 
alta calidad.  
3. Análisis 
crítico de 
resultados ¿El 
estudiante 
interpreta la 
simulación en 
términos 
físicos?  El estudiante no 
analiza los 
resultados o se 
limita a describir 
que el programa 
"funcionó".  El estudiante 
describe los 
resultados 
obtenidos sin 
interpretar su 
significado físico.  El estudiante 
interpreta los 
resultados en 
términos físicos y 
los compara con el 
comportamiento 
esperado.  El estudiante 
realiza un análisis 
profundo: compara 
con datos reales, 
identifica 
limitaciones del 
modelo, propone 
mejoras y 
generaliza 
conclusiones a 
otros fenómenos.  
 
Nota: La defensa oral es un componente evaluativo obligatorio. Un resultado Experto requiere que el estudiante 
pueda explicar y justificar oralmente cada decisión tomada en el modelo y en el código, sin apoyo de apuntes ni 
herramientas digitales durante la  defensa.  
 
4.1 Ponderación  
La calificación final de la experiencia se obtiene de la siguiente ponderación:  
 
Componente  Peso  Puntaje máx.  
Rúbrica: Modelo físico  30% 4 pts.  
Rúbrica: Código Python  30% 4 pts.  
Rúbrica: Análisis crítico  25% 4 pts.  
Defensa oral  15% 4 pts.

14 
La aprobación de la experiencia requiere un mínimo de 2 puntos en cada dimensión de la rúbrica. Un 
resultado Insuficiente en la defensa oral implica la no aprobación, independientemente del puntaje 
obtenido en las demás dimensiones.  
5. Resultados, Análisis y Reflexión Pedagógica  
5.1 Descripción de la implementación piloto  
Durante el segundo semestre del año 2025 se llevó a cabo la primera implementación piloto de la 
propuesta con el grupo de estudiantes de Física de segundo año de Ingeniería en Informática de la 
Universidad de Mendoza, sede San Rafael. La experiencia se des arrolló en el marco regular de la 
asignatura, integrando la modelización computacional como estrategia didáctica complementaria al 
cursado convencional.  
Los estudiantes seleccionaron de forma autónoma el fenómeno físico a modelizar, dentro del programa 
de la asignatura. La elección más frecuente fue el tiro parabólico bidimensional, un fenómeno que combina 
conceptos de cinemática, vectores y movimiento ace lerado, y que admite una representación 
computacional relativamente accesible sin sacrificar rigor físico.  
5.2 Evidencias de impacto  
El indicador más significativo del impacto de la experiencia piloto es el siguiente: en marzo de 2026, dos 
estudiantes pertenecientes a la cohorte 2025 se presentaron a la mesa de examen final de la asignatura 
Física, presentando como trabajo integrador un a simulación computacional funcional del tiro parabólico 
bidimensional programada en Python.  
Este resultado adquiere su plena dimensión cuando se lo contrasta con el comportamiento histórico de 
las cohortes anteriores. En las cohortes 2024 y previas, ningún estudiante había rendido el examen final 
de Física en los primeros meses posteriores al cur sado; la postergación de al menos un año  era la norma. 
El hecho de que estos dos estudiantes no solo completaran el cursado sino que también se presentaran a 
examen en el primer llamado disponible representa un cambio sustancial en el patrón histórico de l a 
asignatura.  
5.3 Análisis pedagógico  
Los resultados obtenidos permiten identificar al menos tres factores que contribuyeron al cambio 
observado:  
• Resignificación de la asignatura: al vincular los contenidos físicos con herramientas de 
programación, los estudiantes percibieron la Física como parte de su campo profesional y no como

15 
una asignatura ajena. Esta resignificación modificó su disposición hacia el aprendizaje y hacia la 
evaluación.  
• Motivación intrínseca generada por el producto: el desarrollo de una simulación funcional —
visible, interactiva y verificable — funcionó como motivador intrínseco. Los estudiantes podían 
observar en tiempo real el comportamiento del sistema que habían model ado, lo que generaba 
una sensación de logro y competencia.  
• Andamiaje apropiado: la combinación de acompañamiento docente y asistencia regulada de IA 
permitió que estudiantes con distintos niveles de conocimiento previo avanzaran 
progresivamente en la tarea, sin generar dependencia ni frustración.  
 
Desde una perspectiva crítica, la experiencia también permitió identificar áreas de mejora para futuras 
implementaciones. Entre ellas, la necesidad de diseñar estrategias de acompañamiento diferenciadas para 
los estudiantes con menor dominio de Python, y l a conveniencia de documentar de forma más sistemática 
el proceso de trabajo de cada estudiante —incluyendo los prompts utilizados con IA — para poder analizar 
con mayor detalle la relación entre el uso de herramientas digitales y el aprendizaje efectivo.  
5.4 Viabilidad y condiciones de implementación  
La propuesta es viable en el contexto descrito por las siguientes razones:  
 
Condición  Estado en el contexto de implementación  
Equipamiento tecnológico  Los estudiantes disponen de notebooks personales. No se requiere 
laboratorio de informática institucional.  
Conocimientos previos de 
programación  Los estudiantes de Ingeniería en Informática tienen formación básica 
en programación, adquirida en asignaturas previas de la carrera.  
Acceso a herramientas de IA  Las versiones gratuitas de Claude y ChatGPT son accesibles sin costo. Se 
accede desde el navegador estándar.  
Carga horaria  La secuencia de cinco clases de 3 horas (15 horas en total) es 
compatible con la planificación anual de la asignatura.  
Respaldo institucional  La propuesta se desarrolla en el marco regular de la asignatura, sin 
requerir aprobaciones extraordinarias. La plataforma virtual 
institucional está disponible para la distribución de materiales.

16 
Plan de contingencia  
• Si un estudiante no dispone de notebook: se coordina el uso de la sala de informática de la 
institución o se trabaja en grupos de dos.  
• Si la IA genera errores o información incorrecta: el docente señala la discrepancia como 
oportunidad de aprendizaje, reforzando la importancia de la validación crítica de las fuentes.  
• Si un estudiante tiene muy bajos conocimientos de Python: se le asigna un fenómeno físico de 
menor complejidad computacional y se intensifica el acompañamiento docente en la Clase 3.  
6. Dimensión Ética y Viabilidad  
La integración de inteligencia artificial en contextos educativos implica asumir responsabilidades 
profesionales que van más allá de la mera selección de herramientas tecnológicas. Esta sección identifica 
los riesgos específicos de la propuesta, describe l as estrategias de mitigación adoptadas y presenta la 
declaración formal de uso responsable de IA.  
6.1 Identificación de riesgos y estrategias de mitigación  
•  
Riesgo  Descripción  Estrategia de mitigación  
Uso indebido de IA : 
código generado 
íntegramente por IA 
sin comprensión del 
proceso  Un estudiante podría solicitar a la IA 
la generación completa del código 
de simulación y entregarlo como 
propio, sin haber atravesado el 
proceso de modelización y 
programación.  Defensa oral obligatoria: el estudiante 
debe explicar y justificar cada línea del 
código ante el docente sin apoyo de 
herramientas. Registro obligatorio de 
prompts utilizados. Preguntas 
orientadas a decisiones de diseño del 
modelo que solo quien lo desarro lló 
puede responder.  
Errores conceptuales 
generados por IA  La IA  puede generar explicaciones 
físicamente incorrectas o 
simplificadas que el estudiante no 
esté en condiciones de identificar 
como erróneas, consolidando 
concepciones equivocadas.  Validación docente sistemática de los 
modelos físicos. Actividad de clase 4 
orientada explícitamente a la 
verificación crítica de resultados. 
Fomento de la cultura de contrastación 
con fuentes académicas fiables.  
Dependencia cognitiva 
excesiva de la IA  El uso frecuente de IA puede generar 
una dependencia que erosione la La IA se habilita únicamente en 
momentos específicos de la secuencia.

17 
capacidad del estudiante para 
resolver problemas de forma 
autónoma.  Las actividades de clase están 
diseñadas para requerir 
argumentación, toma de decisiones y 
verificación independiente. La rúbrica 
valora explícitamente el análisis crítico 
autónomo.  
Desigualdad por 
diferencias en 
conocimientos previos 
de Python  Los estudiantes tienen distintos 
niveles de dominio de Python, lo que 
puede generar disparidades en el 
proceso de implementación 
computacional.  Andamiaje docente diferenciado: 
asignación de fenómenos de mayor o 
menor complejidad computacional 
según el nivel del estudiante. Trabajo 
en parejas permitido en la clase 3 para 
estudiantes con menor dominio 
técnico.  
Privacidad de datos  El uso de herramientas de IA 
externas implica que los prompts  
ingresados son procesados por 
servidores externos, lo que podría 
comprometer la privacidad de 
información institucional o personal.  Se instruye explícitamente a los 
estudiantes para que no incluyan datos 
personales, calificaciones u otra 
información sensible en sus consultas a 
la IA. Se trabaja exclusivamente con 
datos fictilcios o del dominio público.  
•  
6.2 Declaración de uso responsable de Inteligencia Artificial  
En este proyecto se utilizó inteligencia artificial (Claude, Anthropic) como herramienta de apoyo en las siguientes 
etapas: (1) exploración de explicaciones conceptuales alternativas durante la fase de introducción al fenómeno 
físico; (2) verificación punt ual de fragmentos de código Python durante la implementación; y (3) 
retroalimentación sobre la coherencia física del modelo durante la fase de análisis crítico. Todas las producciones 
—el código de simulación, el modelo matemático, el análisis de resultado s y la presentación oral — fueron 
desarrolladas por los estudiantes bajo supervisión docente. No se delegaron en la IA decisiones evaluativas ni 
criterios pedagógicos. El docente revisó sistemáticamente el registro de prompts de cada estudiante durante la 
defensa oral, utilizándolo como insumo para verificar la comprensión genuina del trabajo presentado

18 
7. Conclusiones  
El presente Trabajo Final Integrador demuestra que la integración de la modelización y simulación 
computacional en la enseñanza de la Física permite resignificar la asignatura en el contexto de la Ingeniería 
en Informática, generando un impacto positivo y medible en la motivación, el compromiso y los resultados 
académicos de los estudiantes.  
La experiencia piloto implementada durante 2025 produjo un resultado concreto y significativo: dos 
estudiantes que históricamente habrían postergado la evaluación final durante años se presentaron a 
examen en el primer llamado disponible tras la implementa ción de la propuesta, evidenciando un cambio 
sustancial en su relación con la asignatura. Este resultado valida la hipótesis central del trabajo: vincular 
los contenidos físicos con herramientas propias del campo disciplinar de los estudiantes incrementa l a 
motivación y la calidad del aprendizaje.  
La propuesta se distingue por tres características que le otorgan solidez pedagógica y potencial de 
transferencia. En primer lugar, la articulación entre teoría y práctica a través de la modelización: los 
estudiantes no solo aprenden conceptos físicos, sin o que los operacionalizan mediante programación, 
desarrollando simultáneamente competencias disciplinares y computacionales. En segundo lugar, el uso 
pedagógicamente regulado de la IA: la propuesta no prohíbe ni ignora las herramientas de inteligencia 
artificial, sino que las integra de forma explícita, ética y con límites claramente definidos, preparando a los 
estudiantes para una práctica profesional que inevitablemente involucrará estas tecnologías. En tercer 
lugar, el instrumento de evaluación analítico : la rúbrica diseñada permite distinguir con precisión entre 
comprensión conceptual genuina y ejecución mecánica, garantizando la validez y equidad del proceso 
evaluativo.  
En cuanto a las limitaciones del trabajo, la principal es el reducido tamaño de la muestra de la experiencia 
piloto, que impide afirmar con certeza estadística la generalidad de los resultados. Asimismo, la 
sistematización de la experiencia 2025 requiere m ayor profundidad documental para poder analizar con 
rigor el proceso de trabajo de cada estudiante y la relación específica entre el uso de IA y el aprendizaje 
efectivo.  
De cara a futuras implementaciones, se identifican las siguientes proyecciones: ampliar la propuesta a 
otros fenómenos del programa de Física; desarrollar un protocolo de documentación más detallado del 
proceso de modelización de cada estudiante; explorar la posibilidad de articular la experiencia con otras 
asignaturas de la carrera que utilicen simulación computacional; y diseñar un instrumento de seguimiento 
del impacto a largo plazo en el trayecto académico de los estudiantes.  
El trabajo contribuye, en suma, a la construcción de evidencia sobre estrategias pedagógicas eficaces para 
la enseñanza de la Física en carreras de ingeniería, un campo en el que la investigación didáctica continúa 
siendo una necesidad urgente y un espacio  fértil para la innovación fundamentada.

19 
8. Referencias bibliográficas  
Ausubel, D. P. (1968).  Psicología educativa: Un enfoque cognitivo . Holt, Rinehart and Winston.  
Hestenes, D. (1987).  Hacia una teoría de la modelización en la enseñanza de la física. American 
Journal of Physics , 55(5), 440 –454.  
Holmes, W., Bialik, M., & Fadel, C. (2019).  Inteligencia artificial en educación: Promesas e 
implicancias para la enseñanza y el aprendizaje . Center for Curriculum Redesign.  
Moreira, M. A. (2000).  Aprendizaje significativo: teoría y práctica . Visor.  
Piaget, J. (1970).  La ciencia de la educación y la psicología del niño . Viking Press.  
Vygotsky, L. S. (1978).  El desarrollo de los procesos psicológicos superiores en la sociedad . 
Harvard University Press.  
Wigfield, A., & Eccles, J. S. (2000).  Teoría expectativa -valor de la motivación de logro. 
Contemporary Educational Psychology , 25(1), 68 –81

20 
9. Anexos  
Anexo A: Ejemplo de simulación — Tiro parabólico 2D en Python  
A continuación,  se presenta un ejemplo representativo del tipo de código que desarrollan los estudiantes 
en la Clase 3 de la secuencia didáctica. Este código corresponde a una simulación del tiro parabólico 
bidimensional.  
 
import numpy as np  
import matplotlib.pyplot as plt  
# Parámetros iniciales  
v0 = 20       # velocidad inicial (m/s)  
theta = 45    # ángulo de lanzamiento (grados)  
g = 9.8       # aceleración gravitacional (m/s²)  
# Conversión y componentes de velocidad  
rad = np.radians(theta)  
vx = v0 * np.cos(rad)  
vy = v0 * np.sin(rad)  
# Tiempo de vuelo y vectores  
t_total = 2 * vy / g  
t = np.linspace(0, t_total, 500)  
x = vx * t  
y = vy * t - 0.5 * g * t**2  
# Visualización  
plt.plot(x, y)  
plt.title('Tiro parabólico 2D')  
plt.xlabel('Distancia horizontal (m)')  
plt.ylabel('Altura (m)')  
 
El estudiante deberá además presentar: (1) la justificación física de cada línea de código; (2) el análisis del 
comportamiento de la simulación al variar los parámetros v0 y theta; (3) la comparación de los resultados 
con el valor teórico del alcance máxim o y la altura máxima; y (4) las limitaciones del modelo (sin resistencia 
del aire, proyectil puntual, etc.).

21 
Anexo B: Guía de consignas — Clase 1 (Introducción conceptual)  
Las siguientes consignas orientan el trabajo de los estudiantes durante la primera instancia de la secuencia 
didáctica:  
 
1. Elegí un fenómeno físico del programa de la asignatura que te resulte interesante para modelizar. 
Justifica  brevemente por qué lo elegiste.  
2. Describí el fenómeno con tus propias palabras: ¿qué sucede?, ¿qué variables intervienen?, ¿cuáles 
son las condiciones en las que ocurre?  
3. ¿Qué leyes físicas gobiernan el fenómeno? Identifica  las ecuaciones relevantes.  
4. Si pudieras representar el fenómeno en una pantalla de computadora, ¿qué deberías mostrar? 
¿Cómo visualizarías el movimiento o el cambio de las variables a lo largo del tiempo?  
5. Fórmula  al menos dos preguntas que te gustaría poder responder con la simulación que vas a 
desarrollar.  
 
Anexo C: Registro de uso de IA — Instrumento para estudiantes  
Los estudiantes deben completar el siguiente registro al finalizar cada clase en la que utilizaron 
herramientas de IA:  
 
Clase  Prompt utilizado 
(resumen)  Respuesta obtenida (síntesis)  ¿Cómo lo utilizaste? ¿Qué 
modificaste?  
1    
3    
4

22 
10. Vínculos  
• Acceso a Driver:  
https://drive.google.com/drive/folders/1SWq0ZwEBaiOyNS5BBHcuSLNm2wqCYQsS?usp=sharing  
 
Allí se podrá tener acceso a los Links que a continuación se exponen : 
 
• Registro audiovisual – Experiencia estudiantil  
Tiro parabólico.mp4  
https://drive.google.com/file/d/1eObxI9E165_j_dCTZuxOXhgdptqTZ9ue/view?usp=drive_link  
 
El presente registro audiovisual documenta la experiencia de estudiantes que cursaron la 
asignatura durante el segundo semestre del año 2025 y se presentaron a rendir el examen final 
en la mesa de marzo de 2026.  
En el video, los estudiantes —actualmente cursando tercer año de la carrera — relatan su 
experiencia en relación con la propuesta de trabajo basada en modelización y simulación 
computacional, destacando su impacto en la comprensión de los contenidos y en la  posibilidad de 
rendir la asignatura en tiempos significativamente menores a los observados en cohortes 
anteriores.  
Se sugiere reproducir el material con un nivel de volumen adecuado para una correcta apreciación 
del testimonio.  
 
• Física y C ódigo en la Universidad de Mendoza. Integrando la Ing.mp4  
https://drive.google.com/file/d/1EtgBAKbGJ37oqpKZ7T8FmtbIXxSxzd7r/view?usp=sharing&t=32
.273  
 
• Trabajo Final integrador de Física  (Notion)  
https://www.notion.so/Trabajo -Final -integrador -de-F-sica-
28758282c15a805185e6fd9f6a7420f1?source=copy_link#28758282c15a81eeb112c815f61ebe70  
 
• Trabajo Final integrador de Física  (PDF)  
https://drive.google.com/file/d/1o3d -_lijtLdDTXBYubT5xuML5JT56JTt/view?usp=drive_link  
 
• Trabajo Final Integrador (pptx)

23 
https://docs.google.com/presentation/d/1q1m6 -
wTOQp2sUTpsX_NR6vGQcWHpCr6v/edit?usp=drive_link&ouid=115926001473758061875&rtpo
f=true&sd=true  
• TFI-Mapa Mental (pgn)  
https://drive.google.com/file/d/1swErKrE1R39UEzJWA3W1P5mnOwNuJAfG/view?usp=drive_lin
k 
 
• Fisica -del Papel al Codigo (mp4)  
https://drive.google.com/file/d/101Y2Z80T4i7JRf2PM6JLhKb2sdqkgMF3/view?usp=drive_link  
 
• Física y Codigo en la Universidad de Mendoza (podscat)  
https://drive.google.com/file/d/1EtgBAKbGJ37oqpKZ7T8FmtbIXxSxzd7r/view?usp=drive_link  
 
• TFI (gitmind)  
https://gitmind.com/app/docs/mktnsc74  
NOTA:  
Dentro del repositorio co mpartido en Google Drive se incluye un archivo ejecutable correspondiente al 
trabajo desarrollado por los estudiantes en el marco de su evaluación final.  
Al momento de su descarga, es posible que el sistema operativo o el navegador emitan advertencias 
relacionadas con análisis de seguridad o potencial riesgo. Estas notificaciones responden a las 
características propias del archivo ejecutable y no implican l a presencia de contenido malicioso.  
El archivo no representa riesgo alguno para el equipo. Su ejecución permite acceder a una simulación 
interactiva en la que es posible realizar distintos ensayos modificando variables tales como velocidad 
inicial, ángulo de lanzamiento y condiciones de vien to, así como analizar las representaciones gráficas 
generadas a partir de dichas simulaciones.