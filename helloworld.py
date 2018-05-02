'''
Created on Mar 14, 2018
ogo-oluwa jesutomi olasubulumi <tomilashy@yahoo.com>
@author: ogo-oluwa.olasubulumi
'''
print("Enter an interger");

fruit = "banana";
ripeness = "unripe";
print(f"the {fruit} is {ripeness}");
fruit = "lemon";
ripeness = "rotten";

print("the {} is {}".format(fruit,ripeness));
print("Hello"+" world");
print("Lol"[0],fruit[4])
print(fruit[-4])

#comment
decimal= 12.35342;
integer = int(decimal);
print(integer)
#mileage converter

print("how many kilomerters did you cycle/run today?")
kms=float(input())
miles= round(kms/1.609,5) #round miles to 5 decimal places
print(f"you ran {miles} miles ")

