# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 11:02:58 2020

@author: andrebmo
"""

from collections import defaultdict
import random
import data as d


class Individual:
    
    def __init__(self):
        
       
        
        self.installation_chromosome = defaultdict(list) #Length equal to number of installations
        self.vessel_chromosome = defaultdict(list) #Length equal to number of vessel's
        self.tour_chromosome = {{}} #External dict determines day & vessel, internal dict determines order of installation visits
        
        self.T_dep = {} #The set of days that need a departure (The union of all the assigned installation patterns pi[i])
        self.N_t = {} #The set of installations that have a departure on day t
        self.V_t = {} #The set of vessels that have a departure on day t
        
        
        self.solution{{}} #External dict determines day, vessel & intallation visit, internal dict determines speeds, cost, service time, waiting time, preparation time
        
        self.number_of_supply_jobs = 0
        
        self.objective_value = None #Sum of all costs including constraint relaxations (penalized cost)
        self.diversity_value = None
        
        self.psv_pattern_feasibility = type=bool
        self.feasibility = type=bool
        
        self.rank_cost = type=int
        self.rank_diversity = type=int
        self.biased_fitness = type=int #kanskje denne ikke må være int?
        
        self.number_of_close_individuals = type=int #
        
        
    
        
        #For each subgroup of installation visits
        
            #Solve distance TSP for subgroup and keep X shortest paths
        
            #While solution without collision not found or all X paths explored:
        
                #Solve speed subproblem for subgroup with relaxed time windows
            
                #If time window collides
            
                    #Adjust speeds and keep objective value
    
                    #Try inversing direction
            
                    #If collides again
            
                        #Adjust speeds and keep objective value
                
        #Return solution given chromosomes
        
        def inherit_tour_genes(vessel type=int, day type=int, installations type=list):
            self.tour_chromosome[vessel][day].append(installations)
            self.vessel_chromosome[vessel].append(installations)
            for installation in installations:
                self.installation_chromosome[installation].append(day)
            self.number_of_supply_jobs += installations.len()

        
        def create_possible_psv_patterns():
        
        
        def get_installation_chromosome():
            return self.installation_chromosome
            
        
        def get_psv_chromosome():
            return self.psv_chromosome
        
        def get_tour_chromosome():
            return self.tour_chromosome
        
        
        def get_installation_gene(installation type=int):
            return self.installation_chromosome[installation]
        
        
        def set_installation_gene(installation type=int, pattern type=list):
            self.installation_chromosome[installation] = pattern
        
        
        def get_vessel_gene(vessel type=int):
            return self.vessel_chromosome[vessel]
        
        
        def set_vessel_gene(vessel type=int, pattern type=list):
            self.vessel_chromosome[vessel] = pattern
        
        
        def get_tour_gene(vessel type=int, day type=int):
            return self.tour_chromosome[vessel][day]
        
        
        def get_random_installation_gene(installation type=int:)
            return P_cust[i][rand.randrange(0, len(P_cust[i])-1)]
        
        
        def get_random_psv_gene(vessel type=int):
            return P_psv[v][rand.randrange(0, len(P_psv[v])-1)]


        def days_needing_departure():
            return self.T_dep        
        
        def generate_N_t(days_in_planning_horizon type=list):
            
            #iterer gjennom alle gen i installation-kromosom og sjekk om genet til installasjon i har departure på dag t 
            #hvis ja, legg til denne installasjonen i N_t
            #hvis nei, gå videre
            
            installation_chromosome = self.installation_chromosome
            
            planning_horizon = []
            
            for i in range (days_in_planning_horizon): #lag en liste med dager
                planning_horizon.append(i)
            
            for t in planning_horizon:
                for i in installation_chromosome:
                    for j in installation_chromosome[i] :
                        if installation_chromosome[i][j] == i:
                            self.N_t[i].append(i)
            
            return self.N_t
            
            
            
        
        def generate_V_t(days_in_planning_horizon type=list):
            
            #iterer gjennom alle gen i psv-kromosom og sjekk om genet til psv v har departure på dag t 
            #hvis ja, legg til denne installasjonen i N_t
            #hvis nei, gå videre
            
            psv_chromosome = self.psv_chromosome
            
            planning_horizon = []
            
            for i in range (days_in_planning_horizon): #lag en liste med dager
                planning_horizon.append(i)
            
            for t in planning_horizon:
                for v in psv_chromosome:
                    for s in psv_chromosome[v] :
                        if installation_chromosome[v][s] == v:
                            self.V_t[v].append(v)
            
            return self.V_t


        
        def get_depot_capacity(day):
            #TODO!
            pass
        
        
        def update_number_of_vessels_prepared_at_depot(randomVesselPattern type=list):
            numberOfVesselsPrepared = {} #Keep track of how many vessels are prepared at the supply depot at any day of the planning horizon
            for day in randomVesselPattern #Count the number of vessels being prepared every day to evaluate depot capacity feasibility
                numberOfVesselsPrepared[randomVesselPattern[day]]+=1
            return numberOfVesselsPrepared
        
        
        def cheapest_insertion(installation):
            #TODO!
            #Find the cheapest spot to insert an installation visit to the current individual
            pass
        
        
        def get_number_of_supply_jobs():
            return self.number_of_supply_jobs
        
        
        def get_objective_value():
            #TODO
            return self.objective_value
        
        def get_diversity_value():
            #TODO
            return self.diversity_value
        
        def educate():
            #TODO
            pass
        
        def repair(): #denne burde kanskje ligge i HGSADC
            #TODO
            pass
        
            
            
        def get_PSV_chromosome_feasibility(T_dep type=list, randomVesselPattern type=list):
            
            numberOfVesselsPrepared = {} #Keep track of how many vessels are prepared at the supply depot at any day of the planning horizon
            
            for day in randomVesselPattern #Count the number of vessels being prepared every day to evaluate depot capacity feasibility
                numberOfVesselsPrepared[randomVesselPattern[day]]+=1 
            
            if len(T_dep) != 0 or max(numberOfVesselsPrepared)>self.depot_capacity:
                self.psv_pattern_feasibility = False
                return self.psv_pattern_feasibility
            else:
                self.psv_pattern_feasibility = True
                return self.psv_pattern_feasibility

        
        def get_feasibility():
            return self.feasibility
        
        
        

        
        
        #Installations chromosome
        
        #PSV Chromosome
        
        #For each subgroup of installation visits
        
            #Solve distance TSP for subgroup and keep X shortest paths
        
            #While solution without collision not found or all X paths explored:
        
                #Solve speed subproblem for subgroup with relaxed time windows
            
                #If time window collides
            
                    #Adjust speeds and keep objective value
    
                    #Try inversing direction
            
                    #If collides again
            
                        #Adjust speeds and keep objective value