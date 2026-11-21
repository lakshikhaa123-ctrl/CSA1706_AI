
% Facts
fruit(apple).
fruit(banana).
fruit(mango).
fruit(grapes).
fruit(orange).

color(apple, red).
color(banana, yellow).
color(mango, yellow).
color(grapes, green).
color(orange, orange).

% Rule
fruit_color(X, Y) :-
    fruit(X),
    color(X, Y).
