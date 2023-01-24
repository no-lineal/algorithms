# Anatoly Karatsuba (1960)

def KaratsubaMultiply(x, y):

    if len(str(x)) == 1 or len(str(y)) == 1:

        return x * y

    else:

        n = max( len(str(x)), len(str(y)) ) # maximum order of magnitude
        n_by_2 = n // 2 # to get the pairs 

        # step 1 <- rewrite x and y
        a = x // 10**(n_by_2) # floor
        b = x % 10**(n_by_2) # modulus
        c = y // 10**(n_by_2) # floor
        d = y % 10**(n_by_2) # modulus

        # ste 2 <- computing ac
        ac = KaratsubaMultiply( a, c )

        # step 3 <- computing bd
        bd = KaratsubaMultiply( b, d )

        # step 4 <- computing ad + bc
        ad_bc = KaratsubaMultiply( a, d ) + KaratsubaMultiply( b, c )

        # step 5 <- result
        result = (ac * 10**( 2 * n_by_2 )) + (ad_bc * 10**(n_by_2)) + bd

        return result

x = 1234
y = 5678

print(f'result: {KaratsubaMultiply(x, y)}')