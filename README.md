# Simulador de Máquinas de Turing

Aplicación de escritorio en **Python** con **PyQt6** que simula, paso a paso, dos máquinas de Turing definidas: una que calcula el **máximo entre 0 y un número binario de 8 bits** y otra de **dos cintas** que reconoce **palíndromos binarios**. Se desarrolló como proyecto final de la materia **Teoría de la Computación** (3.er semestre de Ingeniería en Computación, Universidad Tecnológica de la Mixteca).

## Tabla de contenido

- [Máquinas incluidas](#máquinas-incluidas)
- [Cómo se usa](#cómo-se-usa)
- [Instalación y ejecución](#instalación-y-ejecución)
- [Ejecutable para Windows](#ejecutable-para-windows)
- [Estructura del repositorio](#estructura-del-repositorio)
- [Equipo](#equipo)
- [Autoría](#autoría)

## Máquinas incluidas

### Máquina Max (una cinta)

Recibe una cadena binaria de **8 bits** interpretada en complemento a dos y deja en la cinta **max(0, n)**:

| Estado | Lee | Acción |
|--------|-----|--------|
| `q0` | `1` (bit de signo: negativo) | escribe `0`, pasa a `q1` |
| `q0` | `0` (positivo) | pasa a `q2` |
| `q1` | `0`/`1` | escribe `0` y avanza (pone toda la cadena en cero) |
| `q2` | `0`/`1` | avanza sin modificar |
| `q1`/`q2` | `B` (blanco) | pasa a `q3` (estado final) |

Si la entrada tiene menos de 8 caracteres, la aplicación la completa con ceros a la izquierda y avisa al usuario.

### Máquina de palíndromos binarios (dos cintas)

Acepta únicamente las cadenas de `0` y `1` que se leen igual al derecho y al revés. Recorre la entrada hasta el final, la copia **invertida** en la segunda cinta mientras regresa, rebobina la segunda cinta y compara ambas símbolo a símbolo. Si llega a `q4` la cadena es un palíndromo; si en algún paso no hay transición definida, se rechaza. La función de transición `δ` está definida como un diccionario `(estado, símbolo cinta 1, símbolo cinta 2) → (nuevo estado, escritura 1, movimiento 1, escritura 2, movimiento 2)` sobre la clase genérica `TwoTapeTM`.

## Cómo se usa

1. En la ventana principal elige la máquina (**Max** o **Pal**); al pasar el cursor sobre cada botón se muestra su descripción.
2. Escribe la cadena de entrada y confirma.
3. En la ventana de simulación pulsa **Siguiente Paso** para avanzar una transición a la vez. Se muestran las cintas, la posición del cabezal, el estado actual y el número de pasos; al terminar, la máquina indica si llegó al estado final (y, en la de palíndromos, si la cadena se acepta o se rechaza).

## Instalación y ejecución

Requiere **Python 3.12 o superior** (por la sintaxis de f-strings que se usa en `Max.py`).

```bash
git clone https://github.com/Utemitas/DefinedTuringMachinesSimulator.git
cd DefinedTuringMachinesSimulator
python -m venv venv
source venv/bin/activate        # En Windows: venv\Scripts\activate
pip install PyQt6
python src/main.py
```

La interfaz usa las fuentes **Segoe Script** y **Consolas** de Windows; en otros sistemas Qt las sustituye por una fuente parecida.

## Ejecutable para Windows

La carpeta `dist/` contiene el programa empaquetado con **PyInstaller**, que se puede abrir sin instalar Python. Para generarlo de nuevo:

```bash
pip install pyinstaller
pyinstaller Maquinas_de_Turing.spec
```

## Estructura del repositorio

```
DefinedTuringMachinesSimulator/
├── src/
│   ├── main.py                  # Ventana principal (selección de máquina)
│   ├── input.py                 # Ventana de entrada y validación de la cadena
│   ├── Max.py                   # Máquina Max y su ventana de simulación
│   ├── TwoTapeTM.py             # Clase genérica de máquina de Turing de dos cintas
│   ├── Binary_PalindromesTM.py  # Función δ de la máquina de palíndromos binarios
│   ├── Palindromes.py           # Ventana de simulación paso a paso (dos cintas)
│   ├── creditos.py              # Ventana de créditos
│   └── assets/icons/            # Iconos de la interfaz
├── dist/                        # Ejecutables para Windows (PyInstaller)
├── Maquinas_de_Turing.spec      # Configuración de PyInstaller
├── setup.py / pyproject.toml    # Metadatos del paquete
└── requirements.txt
```

## Equipo

Proyecto de los alumnos del grupo **302-B** de la Universidad Tecnológica de la Mixteca:

- Esteban de Jesús Santiago Torres
- Kiran Isaac Hernandez Flores
- Oscar Jasiel Velasco Garcia
- Irving Damian Alvarez Olivera
- Luis Angel Sanchez Aguilar
- Miguel Angel Soriano Martinez
- Haniel Lopez Osorio
- Cesar Zaid Martinez

Agradecimientos especiales al **Dr. Raul Cruz Garcia** por los conocimientos adquiridos en su clase.

## Autoría

El diseño de las máquinas y el código de la aplicación son obra del equipo listado arriba, organizado en GitHub dentro de **Utemitas**. La documentación (este README) se redactó con ayuda de Claude (IA).
