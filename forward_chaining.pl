% Program 38: Forward chaining.
% Sample query:
% ?- forward_chain([has_fever, has_cough], Facts).

rule([has_fever, has_cough], possible_flu).
rule([possible_flu, has_body_pain], flu).
rule([has_fever, has_rash], measles).
rule([flu], needs_rest).
rule([measles], consult_doctor).

subset_list([], _).

subset_list([Head | Tail], List) :-
    member(Head, List),
    subset_list(Tail, List).

infer(Facts, NewFact) :-
    rule(Conditions, NewFact),
    subset_list(Conditions, Facts),
    \+ member(NewFact, Facts).

forward_chain(Facts, FinalFacts) :-
    infer(Facts, NewFact),
    forward_chain([NewFact | Facts], FinalFacts).

forward_chain(Facts, Facts).

prove_forward(InitialFacts, Goal) :-
    forward_chain(InitialFacts, FinalFacts),
    member(Goal, FinalFacts).
