% Program 36: Best First Search.
% Sample query:
% ?- best_first_search(a, g, Path, Cost).

edge(a, b, 2).
edge(a, c, 4).
edge(b, d, 3).
edge(b, e, 1).
edge(c, f, 5).
edge(d, g, 2).
edge(e, g, 6).
edge(f, g, 1).

heuristic(a, 7).
heuristic(b, 6).
heuristic(c, 4).
heuristic(d, 2).
heuristic(e, 5).
heuristic(f, 1).
heuristic(g, 0).

best_first_search(Start, Goal, Path, Cost) :-
    heuristic(Start, H),
    best_first([[H, 0, Start, [Start]]], Goal, ReversePath, Cost),
    reverse(ReversePath, Path).

best_first([[_, Cost, Goal, Path] | _], Goal, Path, Cost).

best_first([[_, Cost, Node, Path] | Rest], Goal, FinalPath, FinalCost) :-
    findall(
        [Heuristic, NewCost, Next, [Next | Path]],
        (
            edge(Node, Next, StepCost),
            \+ member(Next, Path),
            NewCost is Cost + StepCost,
            heuristic(Next, Heuristic)
        ),
        Children
    ),
    append(Rest, Children, OpenList),
    sort(OpenList, SortedOpenList),
    best_first(SortedOpenList, Goal, FinalPath, FinalCost).
