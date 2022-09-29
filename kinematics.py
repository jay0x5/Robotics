import math


#in mm (Values from CAD model)
thighLength = 100 # Side B
HipToGroundlength = 190 #Side C
FemurLength = 100 #Side A



#using law of cosines to determine an angle for up and down movement of leg



#get Angle A
# cos A = sqaure(b) + sqaure(c) - sqaure(a)
hipangleA = pow(thighLength,2) + pow(HipToGroundlength,2) - pow(FemurLength,2)

#2 * b * c
hipangleA2 = 2 * thighLength * HipToGroundlength


hipangleAfinal = hipangleA /hipangleA2
acosfunc = math.acos(hipangleAfinal)
CosAinDeg = math.degrees(acosfunc) #converts rad to deg
print(CosAinDeg)



# get Angle B
# cos B = sqaure(c) + sqaure(a) - sqaure(b)
hipangleB = pow(HipToGroundlength,2) + pow(FemurLength,2) - pow(thighLength,2)

#2 * c * a
hipangleB2 = 2 * HipToGroundlength * FemurLength


hipangleBfinal = hipangleB /hipangleB2
acosfuncB = math.acos(hipangleBfinal)
CosBinDeg = math.degrees(acosfuncB) #converts rad to deg
print(CosBinDeg)



#get Angle C
AngleC = 180 - CosAinDeg - CosBinDeg 
print(AngleC)







