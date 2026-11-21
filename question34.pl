
% Monkey Banana Problem

monkey(at_door).
box(at_window).
banana(hanging).

can_reach_banana :-
    monkey(at_door),
    write('Monkey moves to the box'), nl,
    write('Monkey pushes the box below bananas'), nl,
    write('Monkey climbs onto the box'), nl,
    write('Monkey grabs the bananas'), nl,
    write('Monkey gets the bananas!').
