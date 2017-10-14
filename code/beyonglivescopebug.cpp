Poly_t::Term temp_term; //a bug becuase temp_term's expected live scope is beflow for loop
for (j = 0; j < blockSize; j += 1) {
  for (size_t k = 0; k < vars.size(); k++) {
    temp_term.key.push_back(make_pair(vars[k], Z[j * varNum + k]));
  }
  temp_term.cf = X[ijtok(j + 1, i + 1, blockSize)];

  p1->add_term(temp_term);
}
