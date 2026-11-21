
% Towers of Hanoi

hanoi(1, A, C, _) :-
    write('Move disk from '),
    write(A),
    write(' to '),
    write(C),
    nl.

hanoi(N, A, C, B) :-
    N > 1,
    N1 is N - 1,
    hanoi(N1, A, B, C),
    hanoi(1, A, C, B),
    hanoi(N1, B, C, A).
