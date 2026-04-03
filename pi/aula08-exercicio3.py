def collatz(n):
    seq_collatz = [n]
    while n != 1:
        if not n % 2:
            n = n/2
        else:
            n = (3*n)+1
        seq_collatz.append(n)
    return(seq_collatz)