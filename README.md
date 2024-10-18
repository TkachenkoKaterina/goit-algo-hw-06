# Завдання 1

## Результати

- Кількість вершин: 6
- Кількість ребер: 8
- Ступені вершин: {'Station A': 2, 'Station B': 3, 'Station C': 3, 'Station D': 4, 'Station E': 2, 'Station F': 2}

### Висновки

- У створеному графі транспортної мережі умовного міста міститься **6 станцій** (вершин) та **8 шляхів** (ребер) між ними.
- **Найбільш з'єднаною станцією** є "Station D", яка має ступінь 4, що означає, що вона сполучена з 4 іншими станціями. Це робить її важливим транспортним вузлом у мережі.
- **Середній ступінь вершини** в мережі складає приблизно 2-4, що показує наявність достатньої кількості прямих шляхів для зв'язку між станціями.
- Граф відображає з'єднання між станціями таким чином, що кожна станція сполучена хоча б із двома іншими станціями, що робить мережу добре пов'язаною.
- Візуалізація графу допомогла краще зрозуміти структуру транспортної мережі та визначити ключові вузли, такі як "Station D", що мають стратегічне значення для всієї мережі.

Таким чином, транспортна мережа, представлена у вигляді графу, дозволяє легко аналізувати сполучення між станціями та виявляти важливі вузли для ефективного функціонування міської інфраструктури.

# Завдання 2

## Результати

- Шлях за допомогою DFS: ['Station A', 'Station B', 'Station C', 'Station D', 'Station E', 'Station F']
- Шлях за допомогою BFS: ['Station A', 'Station B', 'Station C', 'Station F']


### Порівняння результатів

- **DFS** заглиблюється в граф і знаходить шлях через більшу кількість вершин: `Station A -> Station B -> Station C -> Station D -> Station E -> Station F`.
- **BFS** знаходить найкоротший шлях, що проходить через меншу кількість вершин: `Station A -> Station B -> Station C -> Station F`.

### Висновки:

- **DFS**: Цей алгоритм шукає шлях у глибину, тому він досліджує всі можливі шляхи, заглиблюючись у граф, що призводить до довшого шляху.
- **BFS**: Цей алгоритм шукає шлях у ширину і гарантує знаходження найкоротшого шляху, оскільки досліджує всі вершини на поточному рівні перед тим, як заглибитися у наступний рівень.

BFS показав себе як більш оптимальний алгоритм для знаходження найкоротшого шляху в даній транспортній мережі.

# Завдання 3

## Результати

- Ребра графа з вагами:
- (Station A, Station B) -> вага: 5
- (Station A, Station D) -> вага: 9
- (Station B, Station C) -> вага: 3
- (Station B, Station D) -> вага: 7
- (Station C, Station D) -> вага: 4
- (Station C, Station F) -> вага: 8
- (Station D, Station E) -> вага: 2
- (Station E, Station F) -> вага: 6

- Найкоротші шляхи від Station A:
- До Station A: шлях ['Station A'], відстань 0
- До Station B: шлях ['Station A', 'Station B'], відстань 5
- До Station C: шлях ['Station A', 'Station B', 'Station C'], відстань 8
- До Station D: шлях ['Station A', 'Station D'], відстань 9
- До Station E: шлях ['Station A', 'Station D', 'Station E'], відстань 11
- До Station F: шлях ['Station A', 'Station B', 'Station C', 'Station F'], відстань 16

### Висновки:

- Алгоритм Дейкстри успішно знаходить найкоротший шлях від однієї станції до всіх інших, враховуючи ваги ребер.
- Виведені шляхи та їхні відстані демонструють мінімальні витрати шляху з урахуванням ваг між станціями.