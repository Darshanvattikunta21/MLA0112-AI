% Program 29: Planets database.
% Sample queries:
% ?- planet_info(earth, Type, Position, Moons).
% ?- gas_giant(Planet).
% ?- has_moons(Planet).

planet(mercury, terrestrial, 1, 0).
planet(venus, terrestrial, 2, 0).
planet(earth, terrestrial, 3, 1).
planet(mars, terrestrial, 4, 2).
planet(jupiter, gas_giant, 5, 95).
planet(saturn, gas_giant, 6, 146).
planet(uranus, ice_giant, 7, 28).
planet(neptune, ice_giant, 8, 16).

planet_info(Name, Type, Position, Moons) :-
    planet(Name, Type, Position, Moons).

inner_planet(Name) :-
    planet(Name, terrestrial, Position, _),
    Position =< 4.

outer_planet(Name) :-
    planet(Name, _, Position, _),
    Position > 4.

gas_giant(Name) :-
    planet(Name, gas_giant, _, _).

has_moons(Name) :-
    planet(Name, _, _, Moons),
    Moons > 0.
