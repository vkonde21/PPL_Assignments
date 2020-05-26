(format t "Enter a number:")
(defvar no (read))
(defun fact(n)
(defvar num 1)
(defvar x)
(if (>= n 0)
    (progn 
        (format t "Factorial is:")
        (if (or (= n 0) (= n 1))
            (print 1)
            (progn
                (loop for x from 1 to n
                do (setq num (* num x))
                )
                (print num)
            )
        )
    )
    
    (format t "Enter a number greater than or equal to 0")
)
)

(fact no)

;progn is used for multiple statements inside if
