% Program 32: Family tree relations.
% Given: Pam, Liz, Ann, Pat are female. Tom, Bob, Jim are male.
% Sample queries:
% ?- mother(Mother, bob).
% ?- father(Father, pat).
% ?- grandfather(Grandfather, jim).
% ?- grandmother(Grandmother, jim).
% ?- sister(Sister, bob).
% ?- brother(Brother, ann).

female(pam).
female(liz).
female(ann).
female(pat).

male(tom).
male(bob).
male(jim).

parent(pam, bob).
parent(tom, bob).
parent(tom, liz).
parent(bob, ann).
parent(bob, pat).
parent(pat, jim).

mother(Mother, Child) :-
    female(Mother),
    parent(Mother, Child).

father(Father, Child) :-
    male(Father),
    parent(Father, Child).

grandfather(Grandfather, Grandchild) :-
    male(Grandfather),
    parent(Grandfather, Parent),
    parent(Parent, Grandchild).

grandmother(Grandmother, Grandchild) :-
    female(Grandmother),
    parent(Grandmother, Parent),
    parent(Parent, Grandchild).

sister(Sister, Person) :-
    female(Sister),
    parent(Parent, Sister),
    parent(Parent, Person),
    Sister \= Person.

brother(Brother, Person) :-
    male(Brother),
    parent(Parent, Brother),
    parent(Parent, Person),
    Brother \= Person.
