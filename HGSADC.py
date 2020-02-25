# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 11:38:50 2020

@author: andrebmo
"""

import time
import data as d
from Population import Population as pop
from Individual import Individual as ind


#### HDSADC ####


class HGSADC:
    
    def __init__(self, min_population_size, generation_size, max_iterations_without_improvement, time_limit):
        
        
        
#------------------------ Inputs -------------------------------        
        self.min_population_size = min_population_size #my
        self.generation_size = generation_size #lambda
        self.max_iterations_without_improvement = max_iterations_without_improvement
        self.time_limit = time_limit
        
        
        
#------------------------ Time -------------------------------
        self.Planning_Horizon = d.Planning_Horizon #Set of days in planning horizon
        self.number_of_days_in_planning_horizon = len(d.Planning_Horizon)
        
        
        
#------------------------ Installations -------------------------------
        self.Insts = d.Insts #Set of installations, including supply depot as element 0.
        
        self.required_visits = {}
        self.total_supply_jobs = type=int
        
        self.depot_capacity = d.depot_capacity #Må sjekke hva vi hadde her i fjor
        
        
#------------------------ Vessels -------------------------------   
        self.Vessels = d.Vessels #Set of vessels in fleet
        self.number_of_vessels_avaliable = #TODO

        
#------------------------ Populations -------------------------------        
        self.feasible_population = {} 
        self.infeasible_population = {} 
        
        self.total_population = self.feasible_population + self.infeasible_population
        
        self.last_hundred_iterations = {i: None for i in range(99)} #preallokerer en liste med de 100 siste iterasjonene. Oppdateres i hovedalgoritmen. 
        
        self.target_ratio_of_naturally_feasible_individuals = d.target_ratio_of_naturally_feasible_individuals
        
        self.elite_individuals = d.elite_individuals #Number of individuals wanted to survive to the next generation 
        
        self.genocide_ratio = d.genocide_ratio 
        
        self.best_solution_from_each_population = {}

#------------------------ Probabilities -------------------------------        
        self.probability_of_education_initial_population = type=float #SETT VERDI
        self.probability_of_repair_initial_population = type=float #SETT VERDI        
 
    
#------------------------ Penalties -------------------------------    
        self.penalty_duration = d.penalty_duration
        self.penalty_capacity = d.penalty_capacity
        self.penalty_installationsVisited = d.penalty_installationsVisited
        
        self.repair_penalty_factor_increase = d.repair_penalty_factor_increase
        
        self.penalty_increase_factor = d.penalty_increase_factor
        self.penalty_decrease_factor = d.penalty_decrease_factor
        
       
#------------------------ Diversification -------------------------------       
        
        self.nClosest = d.nClosest
        self.hammingDistances={} #liste med lister av hamming distanse til naboen for hvert individ         

        
#------------------------ Other -------------------------------       
        
        self.K_init = d.K_init
        self.K_div = d.K_div

    
    

        
        
        run()

        
        

    def run():
        
        t0 = time.time()
        feasible_population, infeasible_population = initiate_population()
        best_objective_value = float("inf")
        iterations_without_improvement = 0
        iteration = 0

        
        while iterations_without_improvement <= self.max_iterations_without_improvement and time.time() - t0 < self.time_limit:
            
            mom, dad = select_parents()
            
            child = create_child(mom, dad)
            
            child = educate(child)
            
            if child.get_feasibility = False:
                child = repair(child, probability)
                
            if child.get_feasibility = False:
                self.infeasible_population.append(child)
                
            else:
                self.feasible_population.append(child)
                
            if get_population_size() == min_population_size + generation_size:
                self.infeasible_population, self.feasible_population = genocide(self.infeasible_population, self.feasible_population)
            
            if iteration%100 = 99   #For hver hundrede iterasjon, oppdater penalty parameters 
                adjust_penalty_parameters()
            
            if child.get_objective_value < best_objective_value:
                iterations_without_improvement = 0
            else:
                iterations_without_improvement += 1
                
            if iterations_without_improvement == iterations_before_diversification:
                feasible_population, infeasible_population = diversify_population(feasible_population, infeasible_population, K_div, min_population_size)
                
            iteration+=1
            
            self.last_hundred_iterations[iteration%100] = child #Oppdaterer fortløpende listen med de 100 siste individene
            
        return get_best_feasible_individual(feasible_population)
            
            
            #Select Parents
            
            #Create offspring
            
            #Educate Child
            
            #If child is infeasible
                
                #insert into infeasible subpopulation
            
                #repair with prob p
            
            #If chils is feasible
            
                #Insert child into feasible subpopulation
            
            #if maximum subpopulation size is reached
            
                #select survivors
            
            #If best solution not improved for iterations_before_diversification iterations then
            
                #Diversify population
            
            #Adjust penalty parameters for infeasibility
            
            #if number of iterations = k * 
 
         
            
    def get_population_size():
        return len(self.feasible_population) + len(self.infeasible_population)


    def is_generation_full():
        if get_population_size() = self.generation_size + self.min_population_size:
            return True
        elif get_population_size() < self.generation_size + self.min_population_size:
            return False
        else:
            raise ValueError()
            

    def get_best_feasible_individual():
        current_best = self.feasible_population[0]
        
        for i in self.feasible_population:
            if i.get_biased_fitness() < current_best.get_biased_fitness()
                current_best =  self.feasible_population[i]
        
        return current_best
    
    
    
    ############################### INITIATE POPULATION ###############################

    
    def create_installation_pattern(creature type=ind):
        #Initiate Population STEP 1: SELECT RANDOM INSTALLATION PATTERN
        for i in Insts: #installation set
            person.installation_chromosome[i] = get_random_installation_gene(i) #Pick random installation pattern
            
        return creature
                


    def create_psv_pattern(creature type=ind):
        #Initiate Population STEP 2: CREATE PSV PATTERN 

        T_dep = creature.days_needing_departure() 
        installation_chromosome = creature.get_installation_chromosome()
        
        
        for i in range(len(installation_chromosome)-1): #Create set of departure days for the individual, T.dep
            installation_gene = get_installation_gene(i)
            for j in range(len(installation_gene)-1):
            if installation_gene[j] not in T_dep
                T_dep.append(installation_gene[j])#Add departure day to T_dep if it's not already there
        
        for v in Vessels: #set of vessels
            randomVesselPattern = get_random_vessel_gene(v) #Pick random PSV pattern
            restart = True  #Restart: must make sure that the PSV pattern chosen at least contains one day in T_dep(s)
            while restart = True:
                for departureDay in randomVesselPattern:
                    if day in T_dep: 
                        creature.psv_chromosome[v] = randomVesselPattern #Assign pattern
                        T_dep.remove(departureDay) #Remove departure day from T_dep
                        restart = False
                        break
                    else randomVesselPattern = get_random_psv_gene(v) #Pick random PSV pattern
            
            psv_pattern_feasibility = get_psv_pattern_feasibility(T_dep, randomVesselPattern)
            
            if psv_pattern_feasibility == True:
                creature.psv_pattern 
                creature.T_dep = T_dep    
                return creature
            else: 
                create_psv_pattern(self, creature)

    
    def create_tour_chromosome(self, creature type=ind):    
            #Initiate Population STEP 3: CREATE TOUR CHROMOSOME
        
        N_t = creature.generate_N_t(T)
        V_t = creature.generate_V_t(T)
        
        randomNum_edu = random.random() #Genererer en float mellom [0.0, 1.0)
        randomNum_rep = random.random()
            
        if randomNum_edu < self.probability_of_education_initial_population:
                creature.educate() #Done in this class
                
        if creature.get_feasibility() == False:
            if randomNum_rep < self.probability_of_repair_initial_population:
            creature = repair(creature)         #tror det er bedre å legge repair som hjelpefunksjon i denne klassen enn å ha den i Individual 
            
        if creature.get_feasibility() == False:
            self.infeasible_population.append(creature)
           
        else: self.feasible_population.append(creature)
        
        return creature

            
        
    
    def initiate_population(K_init type=int):
        
        my = self.min_population_size #minimum number of individuals in subpopulation
        initial_population_size = K_init*my #initial population size
        
        individualsCreated = 0
        
        while individualsCreated < initial_population_size:
            creature = ind()
        
            creature = create_installation_pattern(creature)
        
            creature = create_psv_pattern(creature)
            
            creature = create_tour_chromosome(creature)
            
            individualsCreated += 1
        
            

        
    ############################### SELECT PARENTS ###############################
    
    
    def select_parents():
        mom = find_parent()
        dad = find_parent()
        return mom, dad
    
    
    
    def find_parent():
        candidate_1 = find_mating_candidate()
        candidate_2 = find_mating_candidate()
        if candidate_1.get_objective_value() > candidate_2.get_objective_value():
            return candidate_1
        else:
            return candidate_2
        
    
    
    def find_mating_candidate():
        size = get_population_size()
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
    
    
    
    def get_unsatisfied_installations():
        #TODO
        pass
    
    
    
    def get_feasible_insertion():
        #TODO!
        pass
    
    
    
    ############################### EDUCATION ###############################
           
    
    
    def educate():
        #TODO!
        pass
    
    
    def repair(): #denne burde kanskje ligge i HGSADC
        repair_penalty_factor_increase = self.repair_penalty_factor_increase
        if creature.get_feasibility() == False
            new_penalty_duration = self.penalty_duration * repair_penalty_factor_increase
            new_penalty_capacity = self.penalty_capacity * repair_penalty_factor_increase
            new_penalty_installationsVisited= self.penalty_installationsVisited * repair_penalty_factor_increase
            creature = creature.educate()
        
        if creature.get_feasibility() == False:
            new_penalty_duration *= repair_penalty_factor_increase
            new_penalty_capacity *= repair_penalty_factor_increase
            new_penalty_installationsVisited *= repair_penalty_factor_increase
            creature = creature.educate()
        return creature    
    
    
    ############################### DIVERSIFY POPULATION ###############################
    
    def diversify_population(feasible_population, infeasible_population):
        
        feasible_population = genocide(feasible_population, K_div, min_population_size)
        infeasible_population = genocide(infeasible_population, K_div, min_population_size)
        
        
        my = self.min_population_size #minimum number of individuals in subpopulation
        number_of_individuals_to_create = self.K_div*self.min_population_size #initial population size
        
        individualsCreated = 0
        
        while individualsCreated != number_of_individuals_to_create: #generateK_div*my new individuals
        
            creature = create_installation_pattern(creature)
        
            creature = create_psv_pattern(creature)
            
            creature = create_tour_chromosome(creature)
            
            individualsCreated += 1
        return 
    
    
    def get_hamming_distance(creature1 type=ind, creature2):
        #TODO
    
        
    def genocide(population):
        survivors_in_population = 1-self.genocide_ratio
        while len(population) > survivors_in_population:
            current_worst = 0
            
            for i in range(len(population)):
                if population[current_worst].get_objective_value < p.get_objective_value:
                    current_worst = i
            population.remove(i)
        return population
            
        
    ############################### EVALUATION/FITNESS ###############################
    
    
    
    def evaluate_individual(creature type=ind): #skal dette være biased fitness? Såfall finnes denne under
        value = 0
        
        #TODO!
        
        return value
    
    
    def get_biased_fitness(creature type=ind):
        cost_rank = creature.get_cost_rank
        diversity_rank = creature.get_diversity_rank
        number_of_elite_individuals = self.elite_individuals
        total_population_size = get_population_size()
        
        biased_fitness = cost_rank + (1 - number_of_elite_individuals/total_population_size)*rank_diversity
        creature.biased_fitness = biased_fitness
        
        return biased_fitness
    
    
    def get_cost_rank(creature type=ind):
        rank = 1
        
        for i in self.feasible_population:
            if creature.objective_value < i.get_objective_value: 
                rank += 1
                
        for i in self.infeasible_population:
            if creature.objective_value < i.get_objective_value:
                rank += 1
        
        return creature.rank_cost = rank
    

    def get_diversity_rank(creature type=ind):
        rank = 1
        
        for i in self.feasible_population:
            if creature.diversity_value < i.get_diversity_value: #må ha diversity fra hamming distance
                rank += 1
                
        for i in self.infeasible_population:
            if creature.diversity_value < i.get_diversity_value: #må ha diversity fra hamming distance
                rank += 1
        
        return creature.rank_diversity = rank
    
    
    def survivor_selection(): #fjern kloner og dårlige løsninger...
        #TODO
        
        
    
    ############################### PENALTY ADJUSTMENT ###############################
    
    
    def adjust_penalty_parameters(iterations_before_penalty_adjustment type=int):
        
        number_of_naturally_feasible_individuals_duration = 0
        number_of_naturally_feasible_individuals_capacity = 0
        number_of_naturally_feasible_individuals_installationsVisited = 0
            
        for i in self.last_hundred_iterations:
            if get_feasibility_duration(i):
                number_of_naturally_feasible_individuals_duration +=1
                    
        for i in self.last_hundred_iterations:
            if get_feasibility_capacity(i):
                number_of_naturally_feasible_individuals_capacity +=1
                    
        for i in self.last_hundred_iterations:
            if get_feasibility_installationsVisited(i):
                number_of_naturally_feasible_individuals_installationsVisited +=1
                    
        ratio_of_naturally_feasible_individuals_duration = number_of_naturally_feasible_individuals_duration/100
        ratio_of_naturally_feasible_individuals_capacity = number_of_naturally_feasible_individuals_capacity/100
        ratio_of_naturally_feasible_individuals_installationsVisited = number_of_naturally_feasible_individuals_installationsVisited/100
    
        update_penalty(self.penalty_duration, ratio_of_naturally_feasible_individuals_duration)
        update_penalty(self.penalty_capacity, ratio_of_naturally_feasible_individuals_capacity)
        update_penalty(self.penalty_installationsVisited, ratio_of_naturally_feasible_individuals_installationsVisited)
        
        return None #Denne bare oppdaterer egne penalties i objektet. Returnerer ingenting
    
    def update_penalty(penalty, ratio_of_naturally_feasible_individuals):
        if ratio_of_naturally_feasible_individuals <= self.target_ratio_of_naturally_feasible_individuals - 0.05 #legge 0.05 som en parameter lenger oppe heller?
            penalty *= penalty_increase_factor
        elif ratio_of_naturally_feasible_individuals >= self.target_ratio_of_naturally_feasible_individuals + 0.05:
            penalty *= penalty_decrease_factor
        return None #Denne bare oppdaterer egne penalties. Returnerer ingenting
    
    
    def get_feasibility_duration(creature type=ind):
        #TODO
        return



    def get_feasibility_capacity(creature type=ind):
        total_load = 0
        
        tour_chromosome = creature.get_tour_chromosome()
        for i in tour_chromosome[i][].............................
        #TODO
            
    
    
    def get_feasibility_installationsVisited(creature type=ind):
        #TODO
        return        
            
        


