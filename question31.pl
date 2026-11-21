
% Bird Flying System

bird(parrot).
bird(eagle).
bird(pigeon).
bird(penguin).
bird(ostrich).

can_fly(parrot).
can_fly(eagle).
can_fly(pigeon).

cannot_fly(penguin).
cannot_fly(ostrich).

check_bird(Bird) :-
    can_fly(Bird),
    write(Bird),
    write(' can fly').

check_bird(Bird) :-
    cannot_fly(Bird),
    write(Bird),
    write(' cannot fly').
