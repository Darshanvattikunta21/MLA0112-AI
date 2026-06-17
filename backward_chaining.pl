% Program 39: Backward chaining.
% Sample queries:
% ?- prove_backward(flu, [has_fever, has_cough, has_body_pain]).
% ?- prove_backward(needs_rest, [has_fever, has_cough, has_body_pain]).

rule(possible_flu, [has_fever, has_cough]).
rule(flu, [possible_flu, has_body_pain]).
rule(measles, [has_fever, has_rash]).
rule(needs_rest, [flu]).
rule(consult_doctor, [measles]).

prove_backward(Goal, Facts) :-
    member(Goal, Facts).

prove_backward(Goal, Facts) :-
    rule(Goal, Conditions),
    prove_all(Conditions, Facts).

prove_all([], _).

prove_all([Condition | Rest], Facts) :-
    prove_backward(Condition, Facts),
    prove_all(Rest, Facts).
