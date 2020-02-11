# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 11:02:58 2020

@author: andrebmo
"""

from collections import defaultdict

class Individual:
    
    def __init__(self):
        
        self.installation_chromosome = defaultdict(list) #Length equal to number of installations
        self.vessel_chromosome = defaultdict(list) #Length equal to number of vessel's
        self.tour_chromosome = {{}} #External dict determines day & vessel, internal dict determines order of installation visits
        
        self.solution{{}} #External dict determines day, vessel & intallation visit, internal dict determines speeds, cost, service time, waiting time, preparation time
        
        self.number_of_supply_jobs = 0
        
        self.objective_value = None #Sum of all costs including constraint relaxations
        
        self.feasability = type=bool
        
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
    
        
        
        def get_installation_gene(installation type=int):
            return self.installation_chromosome[installation]
        
        
        
        def get_vessel_gene(vessel type=int):
            return self.vessel_chromosome[vessel]
        
        
        
        def get_tour_gene(vessel type=int, day type=int):
            return self.tour_chromosome[vessel][day]
        
        
        
        def get_depot_capacity(day):
            #TODO!
            pass
        
        
        
        def cheapest_insertion(installation):
            #TODO!
            #Find the cheapest spot to insert an installation visit to the current individual
            pass
        
        
        
        def get_number_of_supply_jobs():
            return self.number_of_supply_jobs
        
       
        
        def get_objective_value():
            return self.objective_value
        
        
        
        def educate():
            #TODO!
            pass
        
        def set_objective_value(value):
            self.objective_value = value
            
            
            
        def get_feasability():
            return self.feasability
            
        
        