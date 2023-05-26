import 'dart:io';
import 'dart:math';

void main() {
  List<int> Lista1 = LA(10, 10, 20);
  print('Primera lista : $Lista1');
  List<int> Lista2 = LA(10, 10, 20);
  print('Segunda lista: $Lista2');
  List<int> Lista3 = ingresarListaPorTeclado(5);
  print('Ingrese una lista: $Lista3');
  List<int> listaConcatenada = [];
  listaConcatenada.addAll(Lista1);
  listaConcatenada.addAll(Lista2);
  listaConcatenada.addAll(Lista3);

  print('Lista concatenada: $listaConcatenada');
  listaConcatenada.sort();
}
List<int> LA(int Elem, int Min, int Max) {
  Random Aleatorio = Random();
  List<int> lista = [];
  for (int i = 0; i < Elem; i++) {
    int elemento = Aleatorio.nextInt(Max - Min + 1) + Min;
    lista.add(elemento);
  }
  return lista;
}
List<int> ingresarListaPorTeclado(int Elem) {
  List<int> lista = [];
  for (int i = 0; i < Elem; i++) {
    stdout.write('Ingrese el elemento ${i + 1}: ');
    String input = stdin.readLineSync()!;
    int elemento = int.parse(input);
    lista.add(elemento);
  }
  return lista;
}

