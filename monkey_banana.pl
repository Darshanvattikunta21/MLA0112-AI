% Program 34: Monkey banana problem.
% Sample query:
% ?- can_get_banana(state(at_door, on_floor, at_window, has_not)).

move(state(at_door, on_floor, Box, Has),
     walk(at_window),
     state(at_window, on_floor, Box, Has)).

move(state(at_window, on_floor, at_window, Has),
     push_box(center),
     state(center, on_floor, center, Has)).

move(state(center, on_floor, center, Has),
     climb,
     state(center, on_box, center, Has)).

move(state(center, on_box, center, has_not),
     grasp,
     state(center, on_box, center, has)).

can_get_banana(state(_, _, _, has)).

can_get_banana(State) :-
    move(State, _, NextState),
    can_get_banana(NextState).

solution(state(_, _, _, has), []).

solution(State, [Action | Actions]) :-
    move(State, Action, NextState),
    solution(NextState, Actions).
