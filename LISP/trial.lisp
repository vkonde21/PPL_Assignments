(format t "Hello World ~%")
(print "What's your name")
(defvar *age* (read))
(defvar *num-2* 2)
(defvar *num-3* 2)
(if (= *age* 18)
	(format t "You can vote~%")
	(format t "You can't vote~%")
)

;;;For not operator
;(if (not (= *age* 18))
;	(format t "You can vote~%")
;	(format t "You can't vote~%")
;)

;and operator
(if (and (>= *age* 14) (<= *age* 67))
	(format t "Time for work~%")
	(format t "Work if you want~%")
)

(if (= *num* 2)
	(progn
		(setf *num-2* (* *num-2* 2))
		(setf *num-3* (* *num-3* 3))
	)
)


