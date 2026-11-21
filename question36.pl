
% Graph edges
edge(a,b).
edge(a,c).
edge(b,c).
edge(b,d).
edge(c,e).
edge(d,f).
edge(d,g).
edge(e,g).
edge(f,g).

% Heuristic values
heuristic(a,5).
heuristic(b,6).
heuristic(c,4).
heuristic(d,3).
heuristic(e,3).
heuristic(f,1).
heuristic(g,0).

% Best First Search
best_first(Start, Goal) :-
    heuristic(Start,H),
    search([H-Start-[Start]], [], Goal, Path),
    reverse(Path, P),
    write('Path: '), write(P).

search([], _, _, _) :- fail.

search([_-Goal-Path|_], _, Goal, Path).

search([_-Node-Path|Rest], Visited, Goal, Final) :-
    findall(H-Next-[Next|Path],
       (edge(Node,Next),
        \+ member(Next,Visited),
        heuristic(Next,H)),
       Children),
    append(Rest,Children,Open),
    keysort(Open,Sorted),
    search(Sorted,[Node|Visited],Goal,Final).
