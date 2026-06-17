% Facts (Database)
person(alice, dob(15, may, 1998)).
person(bob, dob(23, august, 2001)).
person(charlie, dob(05, december, 1995)).

% Query examples:
% To find Alice's DOB: ?- person(alice, DOB).
% To find who was born in 2001: ?- person(Name, dob(_, _, 2001)).