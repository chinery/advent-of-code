(setv filename "4.txt")

(with [f (open filename)]
    (setv grid (list (map (fn [x] (.strip x)) f))))

(defn paper [grid i j]
    (= (get (get grid j) i) "@"))

(defn in-range [grid i j]
    (and (<= 0 i (- (len grid) 1))
         (<= 0 j (- (len (get grid i)) 1))))

; (defn accessible [grid i j]
;     (+ (and (> i 0) (paper grid (- i 1) j))
;     ))

(defn neighbourPapers [grid i j]
    (sum (gfor di [-1 0 1]
               dj [-1 0 1]
               (and (or (!= di 0) (!= dj 0))
                    (in-range grid (+ i di) (+ j dj))
                    (paper grid (+ i di) (+ j dj))))))

(defn accessiblePaper [grid i j]
    (and (paper grid i j) 
         (< (neighbourPapers grid i j) 4)))

(print (sum (gfor i (range (len grid))
                  j (range (len (get grid i)))
                  (accessiblePaper grid i j))))