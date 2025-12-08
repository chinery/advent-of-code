pkg load statistics

filename = "8.txt"
% for part one: how many to connect
n = 1000;

% plotting is very very slow because it's done in real time
should_plot = true;

X = importdata(filename, ",");
D = pdist2(X, X, "euclidean");

circuit = zeros(1, size(D, 1));
next_circuit = 1;

circuit_counts = zeros(1, size(X, 1));

[_, argsort] = sort(D(:));
i = 1;

if (should_plot)
  figure;
  hold on;
  view(-144, 38);
endif

while (true)
    [min_r, min_c] = ind2sub(size(D), argsort(i));
    i += 1;

    % ignore lower triangle or equal
    if (min_r >= min_c)
        continue
    endif

    c_circuit = circuit(min_c);
    r_circuit = circuit(min_r);

    if (r_circuit > 0 && r_circuit == c_circuit)
        % ignore both already in same circuit (but decrement n)
    elseif (r_circuit > 0 && c_circuit > 0)
        % merge circuits
        circuit(circuit==c_circuit) = r_circuit;
        circuit_counts(r_circuit) += circuit_counts(c_circuit);
        circuit_counts(c_circuit) = 0;
    elseif (r_circuit == 0 && c_circuit == 0)
        circuit(min_r) = next_circuit;
        circuit(min_c) = next_circuit;
        circuit_counts(next_circuit) += 2;
        next_circuit += 1;
    elseif (r_circuit == 0)
        circuit(min_r) = c_circuit;
        circuit_counts(c_circuit) += 1;
    else
        circuit(min_c) = r_circuit;
        circuit_counts(r_circuit) += 1;
    endif

    if(should_plot)
      plot3(X([min_r, min_c], 1), X([min_r, min_c], 2), X([min_r, min_c], 3))
      drawnow();
    endif

    n -= 1;
    if (n == 0)
      top_counts = sort(circuit_counts, "descend")(1:3);
      printf("Part one: %d\n", prod(top_counts))
    endif

    if (all(circuit==circuit(1)))
      printf("Part two: %d\n", X(min_r, 1) * X(min_c, 1))
      break
    endif
endwhile


