import torch
import torch.nn as nn
import torch.nn.functional as F
from sklearn.metrics import classification_report, confusion_matrix


# --- 1. Definicja Sieci MLP (Multi-Layer Perceptron) ---
class SimpleMLP(nn.Module):
    def __init__(self):
        super(SimpleMLP, self).__init__()
        # MLP wymaga "spłaszczenia" obrazu na samym początku.
        # Zakładamy obraz 28x28 pikseli (np. zbiór MNIST) -> wektor 784.
        self.flatten = nn.Flatten()
        self.fc1 = nn.Linear(28 * 28, 128)  # Warstwa ukryta
        self.fc2 = nn.Linear(128, 10)  # Wyjście (10 klas cyfr)

    def forward(self, x):
        x = self.flatten(x)  # Utrata struktury przestrzennej!
        x = F.relu(self.fc1(x))  # Funkcja aktywacji
        x = self.fc2(x)
        return x


# --- 2. Definicja Sieci CNN (Convolutional Neural Network) ---
class SimpleCNN(nn.Module):
    def __init__(self):
        super(SimpleCNN, self).__init__()
        # Wejście: 1 kanał (skala szarości), 28x28 pikseli
        # Conv2d: in_channels=1, out_channels=32, kernel_size=3
        self.conv1 = nn.Conv2d(1, 32, kernel_size=3, padding=1)
        self.pool = nn.MaxPool2d(2, 2)  # Redukcja wymiaru o połowę
        self.fc1 = nn.Linear(32 * 14 * 14, 10)  # Klasyfikacja cech

    def forward(self, x):
        # Obraz zachowuje strukturę 2D podczas przechodzenia przez splot
        x = self.pool(F.relu(self.conv1(x)))
        x = x.view(-1, 32 * 14 * 14)  # Spłaszczenie dopiero na końcu
        x = self.fc1(x)
        return x


# --- 3. Symulacja oceny modelu (Metryki) ---
def calculate_metrics():
    # Symulujemy dane:
    # y_true: Rzeczywiste etykiety (np. 0=kot, 1=pies, 2=ptak)
    # y_pred: Przewidywania modelu
    y_true = [0, 1, 2, 2, 0, 1, 1, 0, 2, 0]
    y_pred = [0, 2, 2, 2, 0, 0, 1, 0, 1, 0]

    print("--- Raport Klasyfikacji (Precision, Recall, F1) ---")
    # classification_report automatycznie liczy metryki dla każdej klasy
    print(classification_report(y_true, y_pred, target_names=['Klasa 0', 'Klasa 1', 'Klasa 2']))

    print("\n--- Macierz Pomyłek (Confusion Matrix) ---")
    # Wiersze to prawda, Kolumny to przewidywania
    cm = confusion_matrix(y_true, y_pred)
    print(cm)


# Uruchomienie przykładów
if __name__ == "__main__":
    mlp_model = SimpleMLP()
    cnn_model = SimpleCNN()

    print(f"Liczba parametrów MLP: {sum(p.numel() for p in mlp_model.parameters())}")
    print(f"Liczba parametrów CNN: {sum(p.numel() for p in cnn_model.parameters())}")
    print("\n(Zauważ, że CNN może mieć mniej parametrów, a być skuteczniejsza w obrazach dzięki splotom)\n")

    calculate_metrics()