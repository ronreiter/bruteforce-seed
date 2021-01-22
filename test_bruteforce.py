from bruteforce import find_correct_seed

# test based on:
# seed: "account peanut ghost bless crucial enact horse source spread gentle floor write cook fall rail inhale strong lounge cliff play glow pipe symptom enjoy"
# segwit address: "bc1qcrz2vwkdkzqedzvsdm9fswh3l3cua30580tapj"

address_to_find = "bc1qcrz2vwkdkzqedzvsdm9fswh3l3cua30580tapj"
original = "account peanut ghost bless crucial enact horse source spread gentle floor write cook fall rail inhale strong lounge cliff play glow pipe symptom enjoy"
words = "account account ghost bless crucial enact horse source spread gentle floor write cook fall rail inhale strong lounge cliff play glow pipe symptom enjoy"

correct_seed = find_correct_seed(words, address_to_find, "segwit")
print(correct_seed)
print(correct_seed == original)
