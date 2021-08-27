def permute(s):
    out = []

    if len(s) == 1:
        out = [s]

    else:
        for i,let in enumerate(s):
            print(s[:i]+s[i+1:])
            for prem in permute(s[:i]+s[i+1:]):
                out += [let+prem]

    return out

print(permute('abc'))