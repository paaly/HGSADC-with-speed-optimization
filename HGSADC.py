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
        self.generation_size = generation_size
        self.max_iterations_without_improvement = max_iterations_without_improvement
        self.time_limit = time_limit
        
        self.number_of_days_in_planning_horizon = #TODO
        self.number_of_vessels_avaliable = #TODO
        
        self.required_visits = {}
        self.total_supply_jobs = type=int
        
        
        run()
        
        

    def run():
        
        t0 = time.time()
        feasible_population, infeasible_population = initialize_population()
        best_objective_value = float("inf")
        iterations_without_improvement = 0
        
        while iterations_without_improvement <= self.max_iterations_without_improvement and time.time() - t0 < self.time_limit:
            
            mom, dad = select_parents()
            
            child = create_child(mom, dad)
            
            child = educate(child)
            
            if child.get_feasability = False:
                child = repair(child, probability)
                
            if child.get_feasability = False:
                self.infeasible_population.append(child)
                
            else:
                self.feasible_population.append(child)
                
            if get_population_size == min_population_size + generation_size:
                self.infeasible_population, self.feasible_population = genecide(self.infeasible_population, self.feasible_population)
            
            adjust_penalty_parameters()
            
            if child.get_objective_value < best_objective_value:
                iterations_without_improvement = 0
            else:
                iterations_without_improvement += 1
                
            if iterations_without_improvement == iterations_before_diversification:
                feasible_population, infeasible_population = diversify_population(feasible_population, infeasible_population)
            
        return get_best_feasible_individual(feasible_population)
            
    
    def get_population_size:
        return self.feasible_population.size() + self.infeasible_population_size()
    
    
    
    def is_generation_full:
        if get_population_size = self.generation_size + self.min_population_size:
            return True
        elif get_population_size < self.generation_size + self.min_population_size:
            return False
        else:
            raise ValueError()
    
    
    
    def get_best_feasible_individual(feasible_population):
        #TODO!
        pass
    
    
    ############################### INITIATE POPULATION ###############################
    
    
    
    def initiate_population:
        pass
    
    
    ############################### SELECT PARENTS ###############################
    
    
    def select_parents:
        mom = find_parent()
        dad = find_parent()
        return mom, dad
    
    
    
    def find_parent:
        candidate_1 = find_mating_candidate()
        candidate_2 = find_mating_candidate()
        if candidate_1.get_objective_value() > candidate_2.get_objective_value():
            return candidate_1
        else:
            return candidate_2
        
    
    
    def find_mating_candidate:
        size = get_population_size
        lucky_individual = random.randint(0,size)
        if lucky_individual < self.feasible_population.len():
            return self.feasible_population[lucky_individual]
        else:
            return self.infeasible_population[lucky_individual - self.feasible_population.len()]
        
        
        
    ############################### CROSSOVER ###############################
        
    
    
    def create_child(mom type=ind, dad type=ind):
        
        child = type(Individual)
        
        
        # STEP 0: INHERITANCE RULE
        
        
        inheritance_set_1, inheritance_set_2, inheritance_set_mix = create_inheritence_rules()
        
        
        #STEP 1: INHERIT DATA FROM MOM
        
        
        for value_pair in inheritance_set_1:
            
            vessel, day = decouple_value_pair(value_pair)
            
            child.inherit_genes(vessel, day, mom.get_tour_gene(vessel, day))
            
        for value_pair in inheritance_set_mix:
            
            vessel, day = decouple_value_pair(value_pair)
            
            mom_tour_gene = mom.get_tour_gene[vessel][day]
            length = mom_tour_gene.length()
            
            cutting_point_1 = random.randint(0, length)
            cutting_point_2 = random.randint(0, length)
            
            if cutting_point_1 < cutting_point_2:
                inherited_genes = mom_tour_gene[cutting_point_1:cutting_point_2-1]
                child.inherit_genes(vessel,day,inherited_genes)
                
            elif cutting_point_1 > cutting_point_2:
                inherited_genes = mom_tour_gene[:cutting_point_1-1] + mom_tour_gene[cutting_point_2:]
                child.inherit_genes(vessel,day,inherited_genes)
            
            
        #STEP 2: INHERIT DATA FROM DADDY
        
        
        inheritance_set_2_and_mix = inheritance_set_2 + inheritance_set_mix
        
        random.shuffle(inheritance_set_2_and_mix)
        
        for value_pair in inheritance_set_2_and_mix:
            
            vessel, day = decouple_value_pair(value_pair)
            
            for installation in dad.get_tour_gene(vessel, day):
                
                if day not in child.get_installation_gene(installation) and legal_pattern(child.get_installation_gene(installation), day) #TODO! Make legal pattern function
                   
                    if day in child.get_vessel_gene(vessel):
                       
                       child.inherit_tour_genes(vessel, day, installation)
                   
                    elif child.get_depot_capacity(day):
                   
                        child.inherit_tour_genes(vessel, day, installation)
        
        
        #STEP 3: COMPLETE INSTALLATION SERVICES
        
        
        while child.get_number_of_supply_jobs < self.total_supply_jobs:
            
            unsatisfied_installations = get_unsatisfied_installations()
            
            random.shuffle(unsatisfied_installations)
            
            insertions = get_feasible_insertion(unsatisfied_installations[0])
            
            if insertions.len() = 0:
                
                child = create_child(mom, dad)
                
            else:
                
                child.cheapest_insertion(insertions)
        
    
    
    def decouple_value_pair(value_pair):
        return value_pair[0], value_pair[1]
        
    
    
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
        vessel = math.floor(index / self.number_of_days_in_planning_horizon)
        day = index - vessel * self.number_of_vessels_avaliable
        value_pair = [vessel, day]
        return value_pair
        
    
    
    def legal_pattern(installations, new_installation):
        #TODO
        pass
    
    
    
    def get_unsatisfied_installations:
        #TODO
        pass
    
    
    
    def get_feasible_insertion:
        #TODO!
        pass
    
    
    
    ############################### EDUCATION ###############################
           
    
    
    def educate:
        #TODO!
        pass
    
    
    
    ############################### DIVERSIFY POPULATION ###############################
    
    def diversify_population(feasible_population, infeasible_population):
        #TODO!
        pass
    
    ############################### EVALUATION ###############################
    
    
    
    def evaluate_individual(individual type=ind):
        value = 0
        
        #TODO!
        
        return value
    
    
    
    def 
    
    
    
    def adjust_penalty_parameters:
        #TODO!
        pass
    
    
            
            
            
            
            
            
            
        


