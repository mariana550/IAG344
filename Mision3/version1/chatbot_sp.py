# scikit-learn
# =================================================
# LIBRERIAS 
# =================================================
from xml.parsers.expat import model
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
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
    return model,vectorizer,unique_answers
# =================================================
# Funcion predict_answer
# =================================================
def predict_answer(model,vectorizer,unique_answers,user_text):
    # Convertir el texto a numeros
    x = vectorizer.transform([user_text])
    # El modelo predice la etiqueta de la respuesta 
    label = model.predict(x)[0]
    return unique_answers[label]
# =================================================
# PROGRAMA PRINCIPAL
# =================================================
if __name__ == "__main__":
    training_data = [
        ("Hola", "!Hola¡ ¿En que puedo ayudarte?"),
        ("Buenos días", "Buenos días. Es un gusto atenderte. ¿Cómo puedo ayudarte?"),
        ("Buenas tardes", "Buenas tardes. ¿En qué puedo asistirte?"),
        ("Buenas noches", "Buenas noches. Estoy aquí para ayudarte."),
        ("¿Qué haces?", "Soy un asistente virtual diseñado para brindar información y apoyo."),
        ("¿Quién eres?", "Soy el asistente virtual de la empresa, disponible para ayudarte."),
        ("Necesito ayuda", "Con gusto. Por favor indícame en qué puedo ayudarte."),
        ("Quiero información", "Claro, dime qué información necesitas."),
        ("Gracias", "Con mucho gusto. Estoy aquí para servirte."),
        ("Adiós", "Gracias por contactarnos. Que tengas un excelente día.")
    ]
    # Entrenar el modelo con la lista 
    model,vectorizer,unique_answers = build_and_train_model(training_data)
    # Mostrar un mensaje inicial al usuario
    print("Chatbot supervisado listo,Escribe Salir para terminar. \n")
    while True:
        # Pedimos una frase al usuario
        user = input("Tú: ").strip()
        if user.lower() in{"salir","exit","quit"}:
            print("Bot: !Hasta pronto¡")
            break
        response = predict_answer(model,vectorizer,unique_answers,user)
        print("Bot:",response)



