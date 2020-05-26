flight(toronto,aircanada , london,500, 360).
flight(toronto,united , london,650, 420 ).
flight(toronto,aircanada , madrid,900, 480 ).
flight(toronto,united , madrid,950, 540 ).
flight(toronto,iberia, madrid,800, 480 ).

flight(madrid, aircanada, barcelona, 100, 60).
flight(madrid, iberia, barcelona, 120, 65).
flight(madrid, iberia, valencia, 40, 50).
flight(madrid, iberia, malaga, 50, 60).

flight(barcelona, iberia, valencia, 110, 75).
flight(barcelona, iberia, london , 220, 240).

flight(malaga, iberia, valencia, 80, 120).
flight(paris, united, toulouse, 35, 120).


airportcity(toronto, 50, 60).
airportcity(london, 75, 80).
airportcity(madrid, 75, 45).
airportcity(barcelona, 40, 30).
airportcity(valencia , 40, 20).
airportcity(malaga, 50 , 30).
airportcity(paris, 50, 60).
airportcity(toulouse, 40, 30).

% query for all flights between cities 
fligh(A, C, B, P, D) :-
    flight(A, C, B, P, D),
    write(A),
    write(' '),
    write(C),
    write(' '),
    write(B),
    write(' '),
    write(P),
    write($),
    write(' '),
    write(D),
    write(m),
    nl,
    write(B),
    write(' '),
    write(C),
    write(' '),
    write(A),
    write(' '),
    write(P),
    write($),
    write(' '),
    write(D),
    write(m),
    nl.

%query for airport cities  
airport(A, B, C):- airportcity(A, B, C),
                    write(A),
    write(' '),
    write(C),
    write($),
    write(' '),
    write(B),
    write(m),
    nl.

%query for direct flight between 2 cities
isflightexist(A, B) :- flight(A, _, B, _, _);
                        flight(B, _, A, _, _).

%query for cheap flights
and(A, C, B, P, _) :- flight(A, C, B, P, _),     %also for flight(B, C, A, P, _)
    P<400.
or(A, C, B, P, _):- and(A, C, B, P, _); and(B, C, A, P, _).
isFlightCheap(A, B) :- or(A, C, B, P, _),
write('Flight from '),
write(A),
write(' to '),
write(B),
write(' is cheap. '),
write('Airline is '),
write(C),
write(' and price is '),
write(P),
write($),
nl.

%query to check if it is possible to go in 2 flights from one city to another
istwoflight(A, B) :-
    isflightexist(A, X),
    isflightexist(X, B).

%query to check if flight is preferred or not
orcanada(A, B):- isflightcanada(A, B) ; isflightcanada(B, A).
orunited(A, B):- isflightunited(A, B); isflightunited(B, A).
isflightpreferred(A, B) :- isFlightCheap(A, B);
                           orcanada(A, B). 

%query for If there is a flight from city A to city B with United, then there is a flight from city A to city B with Air Canada.
isflightunited(A, B) :-
    flight(A, C, B, _, _),
    C==united.

isflightcanada(A, B) :-
    flight(A, C, B, _, _),
    C==aircanada.

check(A, B) :-
    (   orunited(A, B)
    ->  (   orcanada(A, B) ->
            write('There exists flight with both airlines united and air canada.')
        )
    ).
    

