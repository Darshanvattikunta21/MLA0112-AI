% Program 31: Check whether a particular bird can fly.
% Sample queries:
% ?- can_fly(eagle).
% ?- cannot_fly(ostrich).

bird(eagle).
bird(sparrow).
bird(parrot).
bird(penguin).
bird(ostrich).
bird(kiwi).

has_wings(eagle).
has_wings(sparrow).
has_wings(parrot).
has_wings(penguin).
has_wings(ostrich).
has_wings(kiwi).

flightless(penguin).
flightless(ostrich).
flightless(kiwi).

can_fly(Bird) :-
    bird(Bird),
    has_wings(Bird),
    \+ flightless(Bird).

cannot_fly(Bird) :-
    bird(Bird),
    \+ can_fly(Bird).

print_flight_status(Bird) :-
    can_fly(Bird),
    write(Bird),
    write(' can fly.'),
    nl.

print_flight_status(Bird) :-
    cannot_fly(Bird),
    write(Bird),
    write(' cannot fly.'),
    nl.
