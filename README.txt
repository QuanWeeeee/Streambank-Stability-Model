This README.txt file was generated on 2024-11-08 by Quan Wei


--------------------
GENERAL INFORMATION
--------------------

1. Title of Dataset: Quantifying the Effects of Water Management Decisions on Streambank Stability 

2. Author Information
	A. Principal Investigator Contact Information
		Name: Quan Wei
		Institution: Department of Earth and Environmental Sciences, University of Waterloo, Waterloo, ON, Canada
		Email: quan.wei@uwaterloo.ca

	B. Associate or Co-investigator Contact Information
		Name: Andrea E. Brookfield
		Institution:  Department of Earth and Environmental Sciences, University of Waterloo, Waterloo, ON, Canada
		Email: andrea.brookfield@uwaterloo.ca
	C. Associate or Co-investigator Contact Information
		Name: Anthony Layzell
		Institution:  Kansas Geological Survey, University of Kansas, Lawrence, KS, USA
		Email: alayzell@ku.edu


3. Date of data collection (single date, range, approximate date): 

2005-01-01 to 2023-01-01

4. Geographic location of data collection: 

Borehole Shear Test Data 
Place name: the Lower Republican River Basin
Country: U.S.
State: Kansas

HGS Model Data
Place name: the Lower Republican River Basin
Country: U.S.
State: Kansas

5. Information about funding sources that supported the collection of the data: 

This work was supported by a US Geological Survey Section 104(b) grant via the Kansas Water Resource Institute (PI Layzell) and the Natural Science and Engineering Research Council of Canada Discovery Grant Program (PI Brookfield).
---------------------------
SHARING/ACCESS INFORMATION
---------------------------

1. Licenses/restrictions placed on the data: 

These data are available under a CC BY 4.0 license <https://creativecommons.org/licenses/by/4.0/> 

2. Links to publications that cite or use the data: 

Brookfield, A.E. and Layzell, A.L. (2019) ‘Simulating the Effects of Reservoir Management Strategies on Fluvial Erosion’, Water Resources Management, 33(15), pp. 4983–4995. Available at: https://doi.org/10.1007/s11269-019-02380-y.

3. Recommended citation for this dataset: 

Wei, Q., Layzell, A., Brookfield. A. (2024). Quantifying the Effects of Water Management Decisions on Streambank Stability. Federated Research Data Repository. doi:

---------------------
DATA & FILE OVERVIEW
---------------------

1. File List


   A. Filename: SSM-edited.py       
      Short description:  Modified Streambank Stability Model  

   B. Filename: multi-layer.py       
      Short description:  Streambank Stability Model with user-defined layer numbers        

   C. Filename:   2005.txt    
      Short description: Model running data from HGS in 2005.      

   D. Filename:  2005_f.csv     
      Short description: Stability Model output file based on data from 2005. 
      Parameters are included in 2005_f.csv file:

	Geographic Coordinate System:	GCS_WGS_1984
	Datum: 	D_WGS_1984
	Prime Meridian: 	Greenwich
	Angular Unit: 	Degree
     
	Variables:	                                                                                         Acronym  

        Longitude (dd)                                                                               		    X                                                       
        Latitude (dd)                                                                                               Y
        Elevation (m)                                                                                               Z
        Factor of Safety (-)                                                                                        FS
        Angle that has the lowest FS value (degree)                                                                Beta


   E. Filename:   2010olf.txt    
      Short description: Model running data from HGS in 2010.      

   F. Filename:  2010_f.csv     
      Short description: Stability Model output file based on data from 2010
      Parameters are included in 2010_f.csv file:

	Geographic Coordinate System:	GCS_WGS_1984
	Datum: 	D_WGS_1984
	Prime Meridian: 	Greenwich
	Angular Unit: 	Degree
     
	Variables:	                                                                                         Acronym  

        Longitude (dd)                                                                               		    X                                                       
        Latitude (dd)                                                                                               Y
        Elevation (m)                                                                                               Z
        Factor of Safety (-)                                                                                        FS
        Angle that has the lowest FS value (degree)                                                                Beta




---------------------------
METHODOLOGICAL INFORMATION
---------------------------

1. Description of methods used for collection/generation of data: 

For each test, an expandable shear head was lowered into a 3-inch diameter borehole augured to a given depth in the streambank. An initial normal stress was applied to the material by expanding the shear head for 15 minutes. A vertical force was then applied to the shear head by a hand crank, and the peak shear stress was recorded. The test was repeated with progressively higher normal stresses applied to the material in order to construct a failure envelope and determine the variables c’ and Φ.’ At each field site, BST tests were performed at different depths, depending on the alluvial stratigraphy and sedimentology. Three tests were repeated to test for variability. 


