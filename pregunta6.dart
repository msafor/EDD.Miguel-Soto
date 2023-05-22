import 'dart:math';

void main() {
  List<int> a = [4, 3, 2, 2, 1];
  List<int> b = [-3, 2, 8, 0, 1];

  List<int> c = [];
  for (int i = 0; i < a.length; i++) {
    c.add(a[i] * b[i]);
  }

  Random aleatorio = Random();
  for (int i = 0; i < 5; i++) {
    int numeroaleatorio = aleatorio.nextInt(5) + 1;
    c.add(-numeroaleatorio);
  }

  c.sort((a, b) => b.compareTo(a));

  print(c);
}