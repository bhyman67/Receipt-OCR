
<h1>
    <p align="center">Receipt OCR</p>
</h1>

<h1></h1>

I took one of my <a href="https://github.com/bhyman67/Receipt-OCR/blob/master/reciept.jpg">reciepts</a> from King Soopers and wrote a script to extract data from it using the <a href = "https://www.taggun.io/">taggun api</a>. 


Here's what the JSON response was. 

![alt text](JSON_Response.JPG)

I extracted the data and imoported it into  pandas dataframe. It looks like this:

![alt text](Extracted_Data.JPG)

Though this API is neat! It was inaccurate in the data that it pulled in this scenario.

<p align="right">Back to <a href="https://bhyman67.github.io/">BHyman Analytics<a><p>