
(define palindrom?
  (lambda (li)
    (equal? li (reverse li))))

(define list '(1 2 3))

(define list2 '(2 4 6))

(define merge-lists
    (lambda (l1 l2)
      (if (null? l1)
          l2
          (if (null? l2)
              l1
              (if (< (car l1) (car l2))
                  (cons (car l1) (merge-lists (cdr l1) l2))
                  (cons (car l2) (merge-lists (cdr l2) l1)))))))
