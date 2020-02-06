# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 11:38:50 2020

@author: andrebmo
"""

import time
from Population import Population as pop

#### HDSADC ####


class HGSADC:
    
    def __init__(self, population_size, max_iterations_without_improvement, time_limit):
        
        self.population_size = population_size
        self.max_iterations_without_improvement = max_iterations_without_improvement
        self.time_limit = time_limit
        
        
        run()
        
        

    def run():
        
        t0 = time.time()
        current_population = pop.initialize_population()
        iterations_without_improvement = 0
        
        while iterations_without_improvement <= self.max_iterations_without_improvement and time.time() - t0 < self.time_limit:
            
            pop.evaluate_population(current_population)
            
            #Select Parents
            
            #Create offspring
            
            #Educate Child
            
            #If child is infeasable
                
                #insert into infeasible subpopulation
            
                #repair with prob p
            
            #If chils is feasible
            
                #Insert child into feasible subpopulation
            
            #if maximum subpopulation size is reached
            
                #select survivors
            
            #If best solution not improved for iterations_before_diversification iterations then
            
                #Diversify population
            
            #Adjust penalty parameters for infeasability
            
            #if number of iterations = k * 
            
            
            
            
            
            
            
        


