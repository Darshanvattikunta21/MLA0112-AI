% Program 35: Fruit and color using backtracking.
% Sample queries:
% ?- fruit_color(Fruit, red).
% ?- print_all_fruits.

fruit_color(apple, red).
fruit_color(banana, yellow).
fruit_color(grapes, green).
fruit_color(orange, orange).
fruit_color(mango, yellow).
fruit_color(strawberry, red).
fruit_color(guava, green).

same_color(Fruit1, Fruit2) :-
    fruit_color(Fruit1, Color),
    fruit_color(Fruit2, Color),
    Fruit1 \= Fruit2.

print_all_fruits :-
    fruit_color(Fruit, Color),
    write(Fruit),
    write(' is '),
    write(Color),
    nl,
    fail.

print_all_fruits.
