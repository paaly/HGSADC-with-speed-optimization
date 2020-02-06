# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 11:02:58 2020

@author: andrebmo
"""

class Individual:
    
    def __init__(self):
        
        self.installation_chromosome = {} #Length equal to number of installations
        self.psv_chromosome = {} #Length equal to number of psv's
        self.tour_chromosome = {{}} #External dict determines day & vessel, internal dict determines order of installation visits
        
        self.solution{{}} #External dict determines day, vessel & intallation visit, internal dict determines speeds, cost, service time, waiting time, preparation time
        
        self.objective_value = None #Sum of all costs including constraint relaxations
        
        #TODO
        
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
                
        #Return solution given chromosomes
        
        def get_objective_value():
            return self.objective_value
        
        