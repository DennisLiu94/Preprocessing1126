# Preprocessing1126
A python 2.7 script for NTU machine learning course

This script is written in python 2.7 with opencv 2.4.2

Before using this script, you need to install opencv first.

You can use sudo apt-get install python-opencv in ubuntu/debian.


This script has some useful functions like resize, show_image, bluro, out_put, draw, and many useless functions like everything else. TT

If you want to change the procedure you deal with your raw data, you need to get inside and modify the code( which is strongly against the software design principles).

But it's more possible that nobody would use it.


###A new python script for aggregation is here. 

Since I didn't produce hundreds of .res file to do aggregation, a weighted voting is useless.	
I only have 4 to 6 files to aggregate, so a uniform voting plus a few tricks is enough.

If you want to use this script, you need to put the files that you want to aggregate in the same folder and named as 0.res, 1.res and so on. The name start from 0 and must be continuous.

You can change the number of files easily by change the value of c at the beginning of the script.

To have a better performance at track 1, I used a few tricks. Such as: if one .res file predicts a character is a upper case number, I add one score to the upper case of the number and add 0.9 score to the lower case of the number, and vise versa. I can also apply this trick on ten and cow.