# scikit-learn
import os
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

MODEL_DIR = "models"
MODEL_PATH = os.path.join(MODEL_DIR, "model.pkl")
VECTORIZER_PATH = os.path.join(MODEL_DIR, "vectorizer.pkl")
ANSWERS_PATH = os.path.join(MODEL_DIR, "answers.pkl")
# =================================================
# FUNCION DE ENTRENAMIENTO PREGUNTAS Y RESPUESTAS
# =================================================
def build_and_train_model(train_pairs):
    # train_pairs lista de pares (pregunta, respuesta)
    # Ejemplo [("Hola" , "!Hola¡), ("Adios", "!Hasta Luego¡)]")]
    # Separamos las preguntas y respuestas
    questions = [q for q, _ in train_pairs] # lista de preguntas
    answers = [a for _, a in train_pairs] # lista de respuestas
    # Creamos el vectorizado, que traducira el texto a numeros 
    vectorizer=CountVectorizer()
    # Entrenamiento
    x = vectorizer.fit_transform(questions)
    # Obtenemos una lista de respuestas unicas 
    unique_answers = sorted(set(answers))
    # Crear el diccionario con las etiquetas 
    answers_to_label={a:i for i,a in enumerate(unique_answers)}
    # Creamos una lista
    y=[answers_to_label[a] for a in answers]
    # Modelo clasificacion de texto
    model = MultinomialNB()
    # Entrenar el modelo
    model.fit(x,y)

    # Crear carperta para guardar el model si no existe
    os.makedirs(MODEL_DIR, exist_ok=True)
    # Guardar los objetos entrenados
    with open(MODEL_PATH, "wb") as f:
        pickle.dump(model, f)
    with open(VECTORIZER_PATH, "wb") as f:
        pickle.dump(vectorizer,f)
    with open(ANSWERS_PATH, "wb") as f:
        pickle.dump(unique_answers,f)
    print("🆗 Modelo entrenado y guardado correctamente")
    return model,vectorizer,unique_answers

def load_model():
    """
    Carga el modelo, el vectorizado y las respuesta si existe.
    """
    if(
    os.path.exists(MODEL_PATH)
    and os.path.exists(VECTORIZER_PATH)
    and os.path.exists(ANSWERS_PATH)
    ):
        with open(MODEL_PATH, "rb") as f:
            model = pickle.load(f)
        with open(VECTORIZER_PATH, "rb") as f:
            vectorizer = pickle.load(f)
        with open(ANSWERS_PATH, "rb") as f:
            unique_answers = pickle.load(f)
        print("📁 Modelo cargado desde disco.")
        return model,vectorizer,unique_answers
    else:
        print("⚠️ No hay modelo guardado,sera nesesario entrenarlo.")
        return None,None,None
    
def predict_answer(model,vectorizer,unique_answers,user_text):
    # Convertir el texto a numeros
    x = vectorizer.transform([user_text])
    # El modelo predice la etiqueta de la respuesta 
    label = model.predict(x)[0]
    return unique_answers[label]
