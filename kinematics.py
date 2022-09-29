import math


#in mm (Values from CAD model)
thighLength = 100 # Side B [#thigh a.k.a Femur]
HipToGroundlength = 190 #Side C
TibiaLength = 100 #Side A [#Tibia a.k.a Shin]



#using law of cosines to determine an angle for up and down movement of leg



#get Angle A

# cos A = sqaure(b) + sqaure(c) - sqaure(a)
hipangleA = pow(thighLength,2) + pow(HipToGroundlength,2) - pow(TibiaLength,2)

#2 * b * c
hipangleA2 = 2 * thighLength * HipToGroundlength


hipangleAfinal = hipangleA /hipangleA2
acosfunc = math.acos(hipangleAfinal) #inverse cos function in radians
CosAinDeg = math.degrees(acosfunc) #converts rad to deg
print(CosAinDeg)



# get Angle B
# cos B = sqaure(c) + sqaure(a) - sqaure(b)
hipangleB = pow(HipToGroundlength,2) + pow(TibiaLength,2) - pow(thighLength,2)

#2 * c * a
hipangleB2 = 2 * HipToGroundlength * TibiaLength


hipangleBfinal = hipangleB /hipangleB2
acosfuncB = math.acos(hipangleBfinal)
CosBinDeg = math.degrees(acosfuncB) #converts rad to deg
# print(CosBinDeg) Angle B = A since Side B = A



#get Angle C
AngleC = 180 - CosAinDeg - CosBinDeg 
print(AngleC)

#subtracting an offset of 45 and multiplying by the scaling factor
finalC = (AngleC - 45) * 25
print(finalC)






