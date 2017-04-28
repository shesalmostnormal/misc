#! /usr/bin/env python
#coding:utf-8

"""
The objective of this program is to calculate the 4-vector
and the missing partcle rest mass. 
"""

from __future__ import division, print_function
from ROOT import TLorentzVector

nEvents = 0 # Number of events
proton = TLorentzVector(0,0,0,0.938) # 4-vector for proton at rest

# Creates the Ntuple
ntuple = TNtuple("ntuple", "Invariant Masses", 
                 "combo1:combo2:combo3:combo4:combo5:combo6:combo7:combo8")
#Opens up the root file
root_file = TFile("particle_graphs.root", "RECREATE") 

with open("n3pi.dat", "r") as data:
    
    for x in data:

        # Line for each event
        i  = x.split()
        val = int(i[0])

        # Event found in 10 events
        if val == 4:
            if nEvents < 10:
                
                # 4-vectors
                photon = TLorentzVector()
                pi_m = TLorentzVector()
                pi_p1 = TLorentzVector()
                pi_p2 = TLorentzVector()
                m_p = TLorentzVector() # Missing
                n = TLorentzVector() # Neutron
	        photon_BOOL = False
                pi_m_BOOL = False
                pi_p1_BOOL = False
                pi_p2_BOOL = False
                
                nEvents += 1
            else:
                break
            
        elif val == 1: # 4-vector for photon
            photon.SetPxPyPzE(float(i[2]), float(i[3]), float(i[4]), float(i[5]))
            photon_BOOL = True
                
        elif val == 8: # First/second 4-vector for pi-plus
            if pi_p1_BOOL == False:
                pi_p1.SetPxPyPzE(float(i[2]), float(i[3]), float(i[4]), float(i[5]))
                pi_p1_BOOL = True
            else:
                pi_p2.SetPxPyPzE(float(i[2]), float(i[3]), float(i[4]), float(i[5]))
              pi_p2_BOOL = True
                                    
        elif val == 9: # pi-minus 4-vector
            pi_m.SetPxPyPzE(float(i[2]), float(i[3]), float(i[4]), float(i[5]))
            pi_m_BOOL = True

        if photon_BOOL == True and pi_p1_BOOL == True and pi_p2_BOOL == True and pi_m_BOOL == True: # rest mass of the missing particle
	    m_p = photon + proton - (pi_p1 + pi_p2 + pi_m)
            rm = m_p.Mag()
            n = photon + proton - (pi_p1 + pi_p2 + pi_m) # Neutron 4-vector
            n_rm = n.Mag() # Neutron rest mass

	    print ("Missing Particle Mass (GeV/c^2):", rm)
            print ("Number of Events:", nEvents)
            
            # 4-vectors

            combo1 = n + pi_p1 + pi_p2 + pi_m
            combo2 = pi_p1 + pi_p2 + pi_m
            combo3 = pi_p1 + pi_m
            combo4 = pi_p2 + pi_m
            combo5 = pi_p1 + pi_p2
            combo6 = n + pi_p1
            combo7 = n + pi_p2
            combo8 = n + pi_m

            # Ntuple combinations
            ntuple.Fill(combo1.Mag(), combo2.Mag(), combo3.Mag(), combo4.Mag(), combo5.Mag(), combo6.Mag(), combo7.Mag(), combo8.Mag())

cc = TCanvas("cc","Mass Invariants",10,10,800,600)
cc.Divide(2,4)

# Plotting
cc.cd(1)
ntuple.Draw("combo1")
cc.cd(2)
ntuple.Draw("combo2")
cc.cd(3)
ntuple.Draw("combo3")
cc.cd(4)
ntuple.Draw("combo4")
cc.cd(5)
ntuple.Draw("combo5")
cc.cd(6)
ntuple.Draw("combo6")
cc.cd(7)
ntuple.Draw("combo7")
cc.cd(8)
ntuple.Draw("combo8")

# File writing
root_file.Write()
root_file.Close()
