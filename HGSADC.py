# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 11:38:50 2020

@author: andrebmo
"""

import time
from Individual import Individual as ind
import random
import math

#### HDSADC ####


class HGSADC:
    
    def __init__(self, min_population_size, generation_size, max_iterations_without_improvement, time_limit):
        
        self.min_population_size = min_population_size
        self.generation_size = 
        self.max_iterations_without_improvement = max_iterations_without_improvement
        self.time_limit = time_limit
        
        self.feasible_population = #TODO
        self.infeasible_population = #TODO
        
        self.number_of_days_in_planning_horizon = #TODO
        self.number_of_vessels_avaliable = #TODO
        
        
        run()
        
        

    def run():
        
        t0 = time.time()
        self.feasible_population, self.infeasible_population = initialize_population()
        iterations_without_improvement = 0
        
        while iterations_without_improvement <= self.max_iterations_without_improvement and time.time() - t0 < self.time_limit:
            
            mom, dad = select_parents()
            
            offspring = create_offspring(mom, dad)
            
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
            
    
    def get_population_size:
        return self.feasible_population.size() + self.infeasible_population_size()
    
    def is_generation_full:
        if get_population_size = self.generation_size + self.min_population_size:
            return True
        elif get_population_size < self.generation_size + self.min_population_size:
            return False
        else:
            raise ValueError()
    
    def initiate_population:
        pass
    
    def select_parents:
        mom = find_parent()
        dad = find_parent()
        return mom, dad
    
    def find_parent:
        candidate_1 = find_mating_candidate()
        candidate_2 = find_mating_candidate()
        if ind.get_objective_value(candidate_1) > ind.get_objective_value(candidate_2):
            return candidate_1
        else:
            return candidate_2
        
    def find_mating_candidate:
        size = get_population_size
        lucky_individual = random.randint(0,size)
        if lucky_individual < self.feasible_population.size():
            return self.feasible_population[lucky_individual]
        else:
            return self.infeasible_population[lucky_individual - self.feasible_population.size()]
        
    def create_offspring(mom, dad):
        
        # STEP 0: INHERITANCE RULE
        
        inheritance_set_1, inheritance_set_2, inheritance_set_mix = create_inheritence_rules()
        
        #STEP 1: INHERIT DATA FROM MOM
        
        #TODO!
        
        #STEP 2: INHERIT DATA FROM DAD
        
        #TODO!
        
        #STEP 3: COMPLETE INSTALLATION SERVICES
        
        #TODO!
        
    def create_inheritance_rules():
        
        gene_space_size = self.number_of_days_in_planning_horizon * self.number_of_vessels_avaliable
        
        n1 = random.randint(0, gene_space_size)
        n2 = random.randint(0, gene_space_size)
        
        if n2 < n1:
            temp = n1
            n1 = n2
            n2 = temp
        
        gene_set_1 = [None for a in range(0, n1)]
        gene_set_2 = [None for a in range(0, n2 - n1)]
        gene_set_mix = [None for a in range(0, gene_space_size - n2)]
        
        order = [x for x in range(0, gene_space_size)]
        random.shuffle(order)
        
        for x in range(0, gene_space_size):
            if x < n1:
                gene_set_1[x] = index_to_value_pair(order(x))
            elif x >= n1 and x < n2:
                gene_set_2[x - n1] = index_to_value_pair(order(x))
            else:
                gene_set_mix[x - n2] = index_to_value_pair(order(x))
                
        return gene_set_1, gene_set_2, gene_set_mix
        
        
    def index_to_value_pair(index):
        vessel = math.floor(index / self.number_of_vessels_avaliable)
        day = index - vessel * self.number_of_vessels_avaliable
        value_pair = [vessel, day]
        return value_pair
        
        
        
        
    def educate:
        #TODO!
        pass
    
    def add_to_population:
        #TODO!
        pass
    
    
            
            
            
            
            
            
            
        


