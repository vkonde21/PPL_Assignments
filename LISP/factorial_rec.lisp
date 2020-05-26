(format t  "Enter a number: ")
(defvar n (read))
(defun getfact (num)
    (if (or (= num 0) (= num 1))
        1
        (* num (getfact (- num 1)))
    ) 
)

(if (>= n 0)
    (progn
         (format t "Factorial is:")
        (print (getfact n))
    )
    (format t "Enter a number greater than or equal to 0")
)

;By default, a function in LISP returns the value of the last expression evaluated as the return value.