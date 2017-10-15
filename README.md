# ud036_StarterCode - Movie Trailer
A simple Website which is displaying diffrent Movies. 

# Usage

## Installation 
create your own movie web application i just a few steps.

clone or download the newest version https://github.com/swmo/ud036_StarterCode/archive/master.zip

## Getting started

use the example code in app.py or create your own application file

make sure you import the classes:
```
from classes.movie import Movie
from classes.website import Website

```

make a list of your movies you like to show. 
```
movies = []
movie = Movie('Intouchables',
              'https://upload.wikimedia.org/wikipedia/en/9/93/'
              'The_Intouchables.jpg',
              'https://www.youtube.com/watch?v=34WIbmXkewU')
movies.append(movie)
```

to genearte and show the website you can use the Website Class. It will genearte the website and direct open in your default browser.
```
website = Website(movies)
website.generate_html()
website.open_website()
```

Feel free to modify the templates for your needs (the website use bootstrap):
- main_page_content.html contains the body part of the website
- main_page_head.html conatins the head of the website. 
- movie_title_content.html contains the html which is used for every movie in the list.

## Example
Take a look at the app.py for an example.

## License

**MIT License**

Copyright (c) 2017 Moses Tschanz

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.


