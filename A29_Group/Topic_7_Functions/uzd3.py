def get_city_year(p_0, perc, delta , pop_target, interresults = False):
    
    perc_converted = perc * 0.01
    year = 0
    actual_population = 0
 
    while actual_population <= pop_target and year > -1:
        actual_population = p_0 + p_0 * perc_converted + delta  # we could argue here about need to round the number
        year += 1
 
        if actual_population <= p_0: # we could add an small epsilon to converge faster
            # year -= 1 # works because eventually year will go down to -1 when populatation stagnates
            year = -1
            # even easier we can just return -1 because no need to calculate further
            return -1
        p_0 = actual_population
        
        if interresults == True:
            print(f"Actual population in year {year} {actual_population}")
 
    return year
 
print(f"Target population will be reached in {get_city_year(1000, 2, 50, 1200, interresults = True)} years")

# now let's look at example where p0 is 1000, perc - 2 delta is 30 and target is 2000
print(f"Target population will be reached in {get_city_year(1000, -2, 30, 2000, interresults = True)} years")

target_reached = get_city_year(1500, 5, 100, 5000, interresults=True) 
print(f"Target population will be reached in {target_reached} years")