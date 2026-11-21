
man(marcus).
pompeian(marcus).
ruler(caesar).

roman(X) :- pompeian(X).
person(X) :- man(X).

tries_to_assassinate(marcus, caesar).

not_loyal(X,Y) :-
    tries_to_assassinate(X,Y),
    ruler(Y).

hates(X,caesar) :-
    roman(X),
    not_loyal(X,caesar).
