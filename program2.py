import random

words = [
    {"spanish": "Hola", "english": "Hello"},
    {"spanish": "Adiós", "english": "Goodbye"},
    {"spanish": "Por favor", "english": "Please"},
    {"spanish": "Gracias", "english": "Thank you"},
    {"spanish": "Lo siento", "english": "Sorry"},
    {"spanish": "Sí", "english": "Yes"},
    {"spanish": "No", "english": "No"},
    {"spanish": "¿Cómo estás?", "english": "How are you?"},
    {"spanish": "Bien", "english": "Well"},
    {"spanish": "Mal", "english": "Bad"},
    {"spanish": "¿Qué tal?", "english": "How's it going?"},
    {"spanish": "Buenos días", "english": "Good morning"},
    {"spanish": "Buenas tardes", "english": "Good afternoon"},
    {"spanish": "Buenas noches", "english": "Good night"},
    {"spanish": "Hasta luego", "english": "See you later"},
    {"spanish": "Hasta mañana", "english": "See you tomorrow"},
    {"spanish": "Te quiero", "english": "I love you"},
    {"spanish": "Perdón", "english": "Excuse me"},
    {"spanish": "Salud", "english": "Bless you"},
    {"spanish": "¿Cuánto cuesta?", "english": "How much does it cost?"},
    {"spanish": "¿Dónde está?", "english": "Where is it?"},
    {"spanish": "Baño", "english": "Bathroom"},
    {"spanish": "Agua", "english": "Water"},
    {"spanish": "Comida", "english": "Food"},
    {"spanish": "Casa", "english": "House"},
    {"spanish": "Escuela", "english": "School"},
    {"spanish": "Amigo", "english": "Friend"},
    {"spanish": "Familia", "english": "Family"},
    {"spanish": "Trabajo", "english": "Work"},
    {"spanish": "Feliz", "english": "Happy"},
    {"spanish": "Triste", "english": "Sad"},
    {"spanish": "Enfermo", "english": "Sick"},
    {"spanish": "Cansado", "english": "Tired"},
    {"spanish": "Dinero", "english": "Money"},
    {"spanish": "Coche", "english": "Car"},
    {"spanish": "Autobús", "english": "Bus"},
    {"spanish": "Tren", "english": "Train"},
    {"spanish": "Avión", "english": "Airplane"},
    {"spanish": "Bicicleta", "english": "Bicycle"},
    {"spanish": "Libro", "english": "Book"},
    {"spanish": "Música", "english": "Music"},
    {"spanish": "Película", "english": "Movie"},
    {"spanish": "Deporte", "english": "Sport"},
    {"spanish": "Jugar", "english": "Play"},
    {"spanish": "Correr", "english": "Run"},
    {"spanish": "el", "english": "the"},
    {"spanish": "de", "english": "of/from"},
    {"spanish": "que", "english": "that/which"},
    {"spanish": "y", "english": "and"},
    {"spanish": "a", "english": "to/at"},
    {"spanish": "en", "english": "in/on"},
    {"spanish": "un", "english": "a/an"},
    {"spanish": "ser", "english": "to be"},
    {"spanish": "se", "english": "oneself/itself"},
    {"spanish": "no", "english": "no/not"},
    {"spanish": "haber", "english": "to have (auxiliary)"},
    {"spanish": "por", "english": "for/by"},
    {"spanish": "con", "english": "with"},
    {"spanish": "su", "english": "his/her/your/their"},
    {"spanish": "para", "english": "for/to"},
    {"spanish": "como", "english": "like/as"},
    {"spanish": "estar", "english": "to be"},
    {"spanish": "tener", "english": "to have"},
    {"spanish": "le", "english": "him/her/you (indirect object)"},
    {"spanish": "lo", "english": "it/him/you (direct object)"},
    {"spanish": "hacer", "english": "to do/make"},
    {"spanish": "todo", "english": "all/everything"},
    {"spanish": "pero", "english": "but"},
    {"spanish": "más", "english": "more"},
    {"spanish": "o", "english": "or"},
    {"spanish": "poder", "english": "to be able/can"},
    {"spanish": "decir", "english": "to say/tell"},
    {"spanish": "este", "english": "this"},
    {"spanish": "ir", "english": "to go"},
    {"spanish": "otro", "english": "other/another"},
    {"spanish": "ese", "english": "that"},
    {"spanish": "la", "english": "the"},
    {"spanish": "me", "english": "me/myself"},
    {"spanish": "si", "english": "if/whether"},
    {"spanish": "ya", "english": "already/now"},
    {"spanish": "ver", "english": "to see"},
    {"spanish": "porque", "english": "because"},
    {"spanish": "dar", "english": "to give"},
    {"spanish": "cuando", "english": "when"},
    {"spanish": "él", "english": "he/him"},
    {"spanish": "muy", "english": "very"},
    {"spanish": "sin", "english": "without"},
    {"spanish": "vez", "english": "time/occasion"},
    {"spanish": "mucho", "english": "much/a lot"},
    {"spanish": "saber", "english": "to know"},
    {"spanish": "qué", "english": "what"},
    {"spanish": "sobre", "english": "about/on"},
    {"spanish": "mi", "english": "my"},
    {"spanish": "alguno", "english": "some/any"},
    {"spanish": "mismo", "english": "same"},
    {"spanish": "yo", "english": "I"},
    {"spanish": "también", "english": "also/too"},
    {"spanish": "hasta", "english": "until"},
    {"spanish": "año", "english": "year"},
    {"spanish": "dos", "english": "two"},
    {"spanish": "querer", "english": "to want"},
    {"spanish": "entre", "english": "between/among"},
    {"spanish": "así", "english": "thus/so"},
    {"spanish": "primero", "english": "first"},
    {"spanish": "desde", "english": "from/since"},
    {"spanish": "grande", "english": "big"},
    {"spanish": "nos", "english": "us"},
    {"spanish": "llegar", "english": "to arrive"},
    {"spanish": "pasar", "english": "to pass"},
    {"spanish": "tiempo", "english": "time"},
    {"spanish": "ella", "english": "she/her"},
    {"spanish": "sí", "english": "yes"},
    {"spanish": "día", "english": "day"},

]


def quiz_user(words):
    """Quiz the user with words."""
    random.shuffle(words) 
    score = 0

    for word in words:
        print(f"What is the English translation of '{word['spanish']}'?")
        user_answer = input("Your answer: ").strip().lower()
        correct_answer = word['english'].lower()

        if user_answer == correct_answer:
            print("Correct papi!\n")
            score += 1
        else:
            print(f"Wrong MF ! The correct answer is '{word['english']}'.\n")

    print(f"Quiz complete! Your score: {score}/{len(words)}")

def main():
    print("Welcome to the Language Learning Flashcards App!")
    input("Press Enter to start the quiz...")
    quiz_user(words)

if __name__ == "__main__":
    main()