
% Family Tree

% Facts
father(kumar, arun).
father(arun, ravi).
father(kumar, priya).

mother(lakshmi, arun).
mother(priya, ravi).

% Rules
parent(X, Y) :-
    father(X, Y).

parent(X, Y) :-
    mother(X, Y).

grandfather(X, Y) :-
    father(X, Z),
    parent(Z, Y).

brother(X, Y) :-
    father(Z, X),
    father(Z, Y),
    X \= Y.
