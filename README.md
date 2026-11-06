# Similitud de Textos con Markovify y TF-IDF

Proyecto en Python que genera texto sintético mediante cadenas de Markov y analiza su similitud con otros textos utilizando **TF-IDF y similitud del coseno**.

Para este experimento se utiliza la historia de *The Legend of Zelda: Ocarina of Time* como texto original y se compara el resultado con las historias de otros dos videojuegos de la franquicia.

## Objetivo

Analizar qué tan similar es un texto generado mediante cadenas de Markov respecto a su fuente original y a otros textos relacionados.

## Tecnologías utilizadas

- **Python:** lenguaje de programación.
- **Markovify:** generación de texto sintético mediante cadenas de Markov.
- **Scikit-learn:** vectorización TF-IDF y cálculo de similitud del coseno.

## Metodología

El proyecto se desarrolla en cinco etapas:

1. **Selección del texto:** se utiliza la historia de *Ocarina of Time* como corpus original.
2. **Generación sintética:** Markovify analiza las transiciones entre palabras y genera nuevas oraciones utilizando `state_size=2`.
3. **Vectorización:** se transforman los textos en vectores numéricos mediante TF-IDF, eliminando palabras vacías (*stop words*) en inglés.
4. **Cálculo de similitud:** se utiliza la similitud del coseno para medir la semejanza entre los vectores.
5. **Comparación:** el texto sintético se compara con las historias de *Ocarina of Time*, *Twilight Princess* y *Breath of the Wild*.

## Estructura del proyecto

```text
Similitud-en-Textos/
├── main.py
├── original.txt
├── synthetic.txt
├── twilight_princess.txt
├── breath_of_the_wild.txt
├── requirements.txt
├── .gitignore
└── README.md
```

## Instalación y ejecución

**1. Clonar el repositorio**

```bash
git clone https://github.com/DiosDVito/Similitud-en-Textos.git
cd Similitud-en-Textos
```

**2. Crear y activar el entorno virtual (macOS/Linux)**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

**3. Instalar las dependencias**

```bash
pip install -r requirements.txt
```

**4. Ejecutar el programa**

```bash
python main.py
```

El programa generará un nuevo texto sintético, lo guardará en `synthetic.txt` y mostrará los resultados de similitud en la terminal.

## Resultados

En una de las ejecuciones se obtuvieron los siguientes resultados:

| Texto comparado | Similitud del coseno |
|---|---|
| Ocarina of Time | 62.85 % |
| Twilight Princess | 8.75 % |
| Breath of the Wild | 5.97 % |

El texto sintético presentó mayor similitud con *Ocarina of Time*, lo cual era esperado debido a que fue generado a partir de su historia.

Las similitudes con *Twilight Princess* y *Breath of the Wild* fueron considerablemente menores, a pesar de pertenecer a la misma franquicia.

**Nota:** Los resultados pueden variar entre ejecuciones debido a la naturaleza aleatoria de Markovify.

## Conclusiones

El experimento demuestra que las cadenas de Markov permiten generar textos que conservan características del vocabulario y la estructura del corpus original.

Sin embargo, las oraciones generadas pueden presentar inconsistencias narrativas, ya que Markovify aprende patrones estadísticos sin comprender el significado de las palabras.

Por otra parte, TF-IDF y la similitud del coseno permiten cuantificar la semejanza léxica entre documentos, aunque no necesariamente reflejan su similitud semántica.

En conclusión, el proyecto muestra cómo combinar técnicas de generación de texto y procesamiento de lenguaje natural para analizar las relaciones entre diferentes documentos.

## Referencias

- [Markovify — GitHub](https://github.com/jsvine/markovify)
- [Scikit-learn — TF-IDF](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html)
- [Scikit-learn — Cosine Similarity](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.cosine_similarity.html)
- [Zelda Dungeon — Ocarina of Time Story](https://www.zeldadungeon.net/wiki/Ocarina_of_Time_Story)

## Autor

Daniel Esparza

---

*Proyecto académico de generación y análisis de similitud de textos.*