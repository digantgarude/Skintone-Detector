# Skintone detector
A script in python to allot skin tone to a certain shade.

It makes use of K means clustering to get approximate skin tone. It also uses haar cascade to detect face.

# Process : 
Image => Detect face => Extract Face => Pass to K means Clustering algorithm => Get the cluster with max members => Denote that as actual shade => Subtract the received skintone from selected values of skin tone shade => Allot the mskin tone with min subtracted value as shade.

# Run :
python main_file.py

Image file name : test.jpg

# Note :
The reference skin tone shades that I have used are in the file skin.png. 
Different values can be used. Just edit the list variable named 'colors' with custom RGB tones.
I've also left some code in comments so that it can be easier if one wants to test and see output at various points.