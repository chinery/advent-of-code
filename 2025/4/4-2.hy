(setv filename "4.txt")

(with [f (open filename)]
    (setv grid (list (map (fn [x] (.strip x)) f))))

(defn paper [grid i j]
    (= (get (get grid i) j) "@"))

(defn in-range [grid i j]
    (and (<= 0 i (- (len grid) 1))
         (<= 0 j (- (len (get grid i)) 1))))

(defn neighbourPapers [grid i j]
    (sum (gfor di [-1 0 1]
               dj [-1 0 1]
               (and (or (!= di 0) (!= dj 0))
                    (in-range grid (+ i di) (+ j dj))
                    (paper grid (+ i di) (+ j dj))))))

(defn accessiblePaper [grid i j]
    (and (paper grid i j) 
         (< (neighbourPapers grid i j) 4)))

(defn remove-if-accessible* [grid i j]
    (let [old (paper grid i j)
        accessible (accessiblePaper grid i j)
        new (if (or (not old) accessible) "." "@")]
        [new accessible]))

; I'm confused why this isn't built in, internet says it is...
(defn first [x] (get x 0))

; honestly gave up trying to write (defn rest ...)
(defn second [x] (get x 1))

(defn step [grid]
    (let [rows
            (lfor i (range (len grid))
                (list 
                    (lfor j (range (len (get grid i)))
                        (remove-if-accessible* grid i j))))]

    (setv new-grid  (lfor row rows (lfor cell row (first cell))))
    (setv changed   (sum (lfor row rows cell row (second cell))))
    [new-grid changed]))

(defn simulate* [grid changed total]
    (if (and (= changed 0) (!= total 0))
        total 
        (let [[new-grid new-changed] (step grid)]
             (simulate* new-grid new-changed (+ total new-changed)))))

(defn simulate [grid]
    (simulate* grid 0 0))

(print (simulate grid))