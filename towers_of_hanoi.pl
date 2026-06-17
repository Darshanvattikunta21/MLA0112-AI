% Program 30: Towers of Hanoi.
% Sample query:
% ?- hanoi(3, left, right, center).

hanoi(1, Source, Destination, _) :-
    write('Move disk from '),
    write(Source),
    write(' to '),
    write(Destination),
    nl.

hanoi(Disks, Source, Destination, Auxiliary) :-
    Disks > 1,
    SmallerDisks is Disks - 1,
    hanoi(SmallerDisks, Source, Auxiliary, Destination),
    hanoi(1, Source, Destination, Auxiliary),
    hanoi(SmallerDisks, Auxiliary, Destination, Source).
