# This script performs the data prep for the Frascati Manual analyses

# Importing required modules

import pandas as pd

# Creating a reference table for the journals and categories

FM_ref_tab = {'Acoustics':2, 'Actuators':2, 'Adm. Sci.':5, 'Aerospace':2, 'Agriculture':4, 'AgriEngineering':4,
              'Agronomy':4, 'Algorithms':1, 'Animals':4, 'Antibiotics':3, 'Antibodies':3, 'Antioxidants':3,
              'Appl. Sci.':2, 'Appl. Syst. Innov.':2, 'Arts':6, 'Atmosphere':1, 'Atoms':1, 'Axioms':1, 'Batteries':2,
              'Behav. Sci.':5, 'Beverages':2, 'Big Data Cogn. Comput.':2, 'Bioengineering':2, 'Biology':1,
              'Biomedicines':3, 'Biomimetics':1, 'Biomolecules':1, 'Biosensors':2, 'Brain Sci.':3, 'Buildings':2,
              'C':1, 'Cancers':3, 'Catalysts':1, 'Cells':1, 'Ceramics':2, 'Challenges':5, 'ChemEngineering':2,
              'Chemistry':1, 'Chemosensors':2, 'Children':3, 'Chromatography':1, 'Clean Technol.':2, 'Climate':1,
              'Clocks &amp; Sleep':3, 'Coatings':2, 'Colloids Interfaces':2, 'Computation':1, 'Computers':2,
              'Condens. Matter':1, 'Corros. Mater. Degrad.':2, 'Cosmetics':3, 'Cryptography':1, 'Crystals':1,
              'Dairy':4, 'Data':1, 'Dent. J.':3, 'Designs':2, 'Diagnostics':3, 'Diseases':3, 'Diversity':1,
              'Drones':2, 'Econometrics':5, 'Economies':5, 'Educ. Sci.':5, 'Electronics':2, 'Energies':1,
              'Entropy':1, 'Environments':1, 'Epigenomes':1, 'Eur. J. Investig. Health Psychol. Educ.':5,
              'Fermentation':2, 'Fibers':2, 'Fire':1, 'Fishes':4, 'Fluids':1, 'Foods':4, 'Forecasting':1,
              'Forests':1, 'Fractal Fract':1, 'Future Internet':2, 'Galaxies':1, 'Games':5, 'Gastrointest. Disord.':3,
              'Gels':2, 'Genealogy':6, 'Genes':1, 'GeoHazards':1, 'Geosciences':1, 'Geriatrics':3, 'Healthcare':3,
              'Heritage':6, 'High-Throughput':1, 'Horticulturae':4, 'Humanities':6, 'Hydrology':1, 'Informatics':2,
              'Information':1, 'Infrastructures':2, 'Inorganics':1, 'Insects':1, 'Instruments':2,
              'Int. J. Environ. Res. Public Health':3, 'Int. J. Financial Stud.':5, 'Int. J. Mol. Sci.':1,
              'Int. J. Neonatal Screen.':3, 'Int. J. Turbomach. Propuls. Power':2, 'Inventions':2, 'IoT':2,
              'ISPRS Int. J. Geo-Inf.':5, 'J':5, 'J. Cardiovasc. Dev. Dis.':3, 'J. Clin. Med.':3, 'J. Compos. Sci.':2,
              'J. Cybersecur. Priv.':2, 'J. Dev. Biol.':1, 'J. Funct. Biomater.':2, 'J. Funct. Morphol. Kinesiol.':3,
              'J. Fungi':1, 'J. Imaging':2, 'J. Intell.':5, 'J. Low Power Electron. Appl.':2, 'J. Manuf. Mater. Process.':2,
              'J. Mar. Sci. Eng.':2, 'J. Open Innov. Technol. Mark. Complex.':5, 'J. Otorhinolaryngol. Hear. Balance Med.':3,
              'J. Pers. Med.':3, 'J. Risk Financial Manag.':5, 'J. Sens. Actuator Netw.':2, 'Land':5, 'Languages':6,
              'Laws':5, 'Life':1, 'Logistics':2, 'Lubricants':2, 'Mach. Learn. Knowl. Extr.':1, 'Machines':2,
              'Magnetochemistry':1, 'Mar. Drugs':3, 'Materials':2, 'Math. Comput. Appl.':1, 'Mathematics':1,
              'Med. Sci.':3, 'Medicina':3, 'Medicines':3, 'Membranes':2, 'Metabolites':1, 'Metals':2, 'Methods Protoc.':1,
              'Microarrays':1, 'Micromachines':2, 'Microorganisms':1, 'Minerals':1, 'Molbank':1, 'Molecules':1,
              'Multimodal Technologies Interact.':2, 'Nanomaterials':2, 'Neuroglia':3, 'Nitrogen':1, 'Non-Coding RNA':1,
              'Nutrients':3, 'Particles':1, 'Pathogens':1, 'Pharmaceuticals':3, 'Pharmaceutics':3, 'Pharmacy':3,
              'Philosophies':6, 'Photonics':1, 'Physics':1, 'Plants':1, 'Plasma':1, 'Polymers':2, 'Proceedings':1,
              'Processes':2, 'Proteomes':1, 'Publications':6, 'Quantum Beam Sci.':1, 'Quantum Reports':1, 'Quaternary':1,
              'Reactions':1, 'Recycling':5, 'Religions':6, 'Remote Sens.':2, 'Reports':3, 'Resources':5, 'Risks':5,
              'Robotics':2, 'Safety':2, 'Sci':1, 'Sci. Pharm.':3, 'Sensors':2, 'Separations':1, 'Signals':2,
              'Sinusitis':3, 'Sinusitis and Asthma':3, 'Smart Cities':5, 'Soc. Sci.':5, 'Societies':5, 'Soil Syst.':1,
              'Soils':1, 'Sports':3, 'Stats':1, 'Surfaces':1, 'Sustainability':5, 'Symmetry':1, 'Systems':5,
              'Technologies':2, 'Toxics':2, 'Toxins':1, 'Trop. Med. Infect. Dis.':3, 'Universe':1, 'Urban Sci.':5,
              'Vaccines':3, 'Vet. Sci.':4, 'Vibration':2, 'Viruses':1, 'Vision':3, 'Water':5, 'World Electr. Veh. J.':2}

# List of files to read and update

files = [str(i) for i in range(1996,2019)]
files.append('all')
root = 'C:/Users/User/Documents/Data/MDPI/MDPIpapers_'
noot = 'C:/Users/User/Documents/Data/MDPI/Frascati_'

# Create new files repalcing journal with the Frascati Manual category and saving as a new file

for file in files:

    df = pd.read_csv(root + file + '.csv')
    df = df.replace({'Journal':FM_ref_tab})
    df.to_csv(noot + file + '.csv', index = False)

    for i in range(1,7):
        
        temp_df = df[df.Journal == i]
        temp_df.to_csv(noot + file + '_cat_' + str(i) + '.csv', index = False)

