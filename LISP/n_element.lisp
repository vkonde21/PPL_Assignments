(defvar a )
(defvar n)
(format t "Enter list: ")
(setq a (read-from-string (concatenate  'string "(" (read-line) ")")))
(format t "List is:")
(print a)
(format t "~%Enter the index in list: ")
(setq n (read))
(format t "The element is: ")
(print (nth n  a))