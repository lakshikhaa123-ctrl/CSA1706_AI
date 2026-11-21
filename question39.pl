
% Facts
fact(fever).
fact(cough).

% Rules
disease(flu) :-
    fact(fever),
    fact(cough).

disease(cold) :-
    fact(cough),
    fact(sneezing).

% Backward chaining
diagnosis(X) :-
    disease(X).
