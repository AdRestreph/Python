from dataset import load_data
from model import train_model
from predict import evaluate_model


def main ():
    # Cargar datos
    (X_train, X_val, y_train, y_val), class_names = load_data()

    # Entrenar modelo
    model = train_model(X_train, y_train, X_val, y_val, len(class_names))

    # Evaluar modelo
    evaluate_model(model, X_val, y_val, class_names)

if __name__ == '__main__':
    main()