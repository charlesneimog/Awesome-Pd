import os
import json
import re
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction import text

custom_stopwords = set(text.ENGLISH_STOP_WORDS).union({
    "object", "outputs", "used", "primarily", "library", "feature"
})

def clear_text(txt: str) -> str:
    """Normaliza texto: minúsculas e remove caracteres especiais."""
    tokens = re.sub(r"[^a-z0-9 ]", " ", txt.lower()).split()
    return " ".join([t for t in tokens if t not in custom_stopwords])

def jaccard(a, b):
    """Similaridade de Jaccard entre duas listas de categorias."""
    sa, sb = set(a), set(b)
    return len(sa & sb) / len(sa | sb) if sa | sb else 0


def update_similarity():
    base_dir = os.path.dirname(__file__)
    input_dir = os.path.join(base_dir, "../docs/objects_raw")
    output_dir = os.path.join(base_dir, "../docs/objects_raw/")

    # garantir que a pasta "related" exista
    os.makedirs(output_dir, exist_ok=True)

    # 1. Carregar todos os JSONs
    objetos = []
    arquivos = [f for f in os.listdir(input_dir) if f.endswith(".json")]
    for file in arquivos:
        json_file = os.path.join(input_dir, file)
        with open(json_file, "r", encoding="utf-8") as f:
            data = json.load(f)
            data["__file__"] = file
            data["desc_limpa"] = clear_text(data.get("description", ""))
            objetos.append(data)

    if not objetos:
        print("No JSON found.")
        return

    # 2. TF-IDF nas descrições
    docs = [o["desc_limpa"] for o in objetos]
    vectorizer = TfidfVectorizer(stop_words="english")
    tfidf_matrix = vectorizer.fit_transform(docs)

    # 3. Similaridade de descrições (cosine)
    sim_descricoes = cosine_similarity(tfidf_matrix)

    # 4. Similaridade de categorias (jaccard)
    sim_categorias = np.zeros((len(objetos), len(objetos)))
    for i in range(len(objetos)):
        for j in range(len(objetos)):
            sim_categorias[i, j] = jaccard(objetos[i].get("categories", []),
                                           objetos[j].get("categories", []))

    # 5. Combinar scores
    alpha, beta = 0.7, 0.3
    sim_total = alpha * sim_descricoes + beta * sim_categorias

    # 6. Gerar arquivos na pasta "related"
    for i, obj in enumerate(objetos):
        scores = sim_total[i]
        indices = scores.argsort()[::-1]  # ordena decrescente
        recomendados = [j for j in indices if j != i][:4]  # top 5

        obj["similar"] = [objetos[j]["title"] for j in recomendados]

        # salvar no output_dir
        out_file = os.path.join(output_dir, obj["__file__"])

        obj.pop("__file__", None)
        obj.pop("desc_limpa", None)

        with open(out_file, "w", encoding="utf-8") as f:
            json.dump(obj, f, indent=4, ensure_ascii=False)


if __name__ == "__main__":
    update_similarity()

