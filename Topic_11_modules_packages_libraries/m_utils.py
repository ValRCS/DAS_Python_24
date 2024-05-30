# 1. Reizinājumu summa
# Izmantojot standarta bibliotekas math sadaļu,
# Atrodiet funkciju kura sarēķina kādas virknes visu elementu reizinājumu (product)
# Importējiet uz izsauciet to pa tiešo.
# 1.b Uzrakstiet savu funkciju sum_prod(seq_a, seq_b) kas
# atgriež divu virknju reizinājumu summu
# sum_prod([2,3],[5,10,2]) == 106
# bonuss: uzrakstiet funkciju, kas atgriež neierobežota skaita virknju reizinājumu summu, t.i. katra virkne tiek sareizināta savā starpa un tad rezultāts sasummēts
import math
def sum_prod(seq_a, seq_b):
    return math.prod(seq_a) + math.prod(seq_b)

def sum_prod_unlimited(*args):
    # so the next code will go through all arguments and multiply them together
    # return sum([math.prod(arg) for arg in args])
    # we could do this without list comprehension
    result = 0
    for arg in args:
        # result += math.prod(arg) # this is good but two operations in one line
        # we could it separate
        product = math.prod(arg) # no name collision with built-in function
        result += product
    return result

# let's write some tests that use main guard

if __name__ == "__main__":
    print("Running tests")
    assert(sum_prod([2,3],[5,10,2]) == 106) # 106
    assert(sum_prod_unlimited([2,3],[5,10,2],[2,3],[5,10,2]) == 212) # 424
    assert(sum_prod_unlimited([2,3],[5,10,2],[2,3],[5,10,2],[2,3],[1,0,5]) == 218) # 636
    # TODO add more tests
    print("All tests passed")
