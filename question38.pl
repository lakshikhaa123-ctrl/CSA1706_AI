
:- dynamic known/1.

% Rules
rule([fever, cough], flu).
rule([fever, headache], malaria).

% Check conditions
check([]).
check([X|T]) :-
    known(X),
    check(T).

% Forward chaining
forward :-
    rule(Conditions, Result),
    check(Conditions),
    \+ known(Result),
    !,
    assertz(known(Result)),
    write('Inferred: '), write(Result), nl,
    forward.

forward.

% Main program
run :-
    retractall(known(_)),
    assertz(known(fever)),
    assertz(known(cough)),
    write('Initial Facts Loaded'), nl,
    forward,
    write('Forward Chaining Completed').
