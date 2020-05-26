happy(albert).
happy(alice).
happy(bob).
happy(bill).
with_albert(alice).

runs(albert):-
    happy(albert).

dances(alice) :-
    happy(alice),    
    with_albert(alice).                            %comma means and

does_alice_dance :-
    dances(alice), 
    write('When alice is happy').