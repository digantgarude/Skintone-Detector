# Skintone Shade Detector

- A script in python to allot skin tone to a certain shade.

- It makes use of K means clustering to get approximate skin tone. It also uses haar cascade to detect face.

- This project can be used in fashion recommendation websites for recommendation of outfits based on skin tone of the user. (**Note** : *This is not racist in any sense and many Fashion designers use skin complexion to recommend outfits to users. This project is a part of my capstone project i.e Outfit recommendation based on Occasion and Skin Tone.* [Fashion Designer Website Example](https://www.instyle.com/how-tos/how-to-find-best-color-to-wear-for-your-skin-tone)) 

# Process : 

```
=> Take Image 
=> Detect face 
=> Extract Face 
=> Pass to K means Clustering algorithm 
=> Get the cluster with max members 
=> Denote that as actual shade 
=> Subtract the received skintone from selected values of skin tone shade 
=> Allot the skin tone with min subtracted value as shade.
```

## Installation

```bash
pip install sklearn
pip install matplotlib
pip install opencv-python
pip install pandas
pip install sklearn
```

## Usage:

```bash
python main_file.py
```

**Image file name** : test.jpg

# Note :

The reference skin tone shades that I have used are in the file skin.png. 
Different values can be used. Just edit the list variable named 'colors' with custom RGB tones.
I've also left some code in comments so that it can be easier if one wants to test and see output at various points.