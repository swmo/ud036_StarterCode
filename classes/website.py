import webbrowser
import os
import re


class Website:
    """
 Genearte a website with movie
 This class can be used to genarte and
 show an html file with movies.

 Attributes:
    movies (array):
        list of movie objects
    output_file_path (str):
        string, default path for
    the generating html
        template_pathes (array):
    list of the templates pathes
        template (array):
    text section of each template
    """

    def __init__(self, movies):
        """Inits the class with the movies"""
        self.movies = movies

        """set default values of the attributes"""
        self.output_file_path = "index.html"
        self.template_pathes = {
            "main_page_head": "template/main_page_head.html",
            "main_page_content": "template/main_page_content.html",
            "movie_title_content": "template/movie_title_content.html"}
        self.template = {
            "main_page_head": "",
            "main_page_content": "",
            "movie_title_content": ""}

    def load_templates(self):
        """load the defined templates to the object"""
        for key, path in self.template_pathes.iteritems():
            file = open(path, "r")
            self.template[key] = file.read()
            file.close()

    def create_movie_titles_content(self):
        """create html with the list of movies"""
        content = ""
        for movie in self.movies:
            youtube_id_match = re.search(
                r'(?<=v=)[^&#]+',
                movie.trailer_youtube_url)
            youtube_id_match = youtube_id_match or re.search(
                r'(?<=be/)[^&#]+',
                movie.trailer_youtube_url)
            trailer_youtube_id = (
                youtube_id_match.group(0) if youtube_id_match else None)
            # Append the tile for the movie with its content filled in
            content += self.template.get('movie_title_content').format(
                movie_title=movie.title,
                poster_image_url=movie.poster_image_url,
                trailer_youtube_id=trailer_youtube_id)
        return content

    def generate_html(self):
        """generate the html and save the file"""
        self.load_templates()
        main_page_content = self.template.get('main_page_content')
        main_page_head = self.template.get('main_page_head')
        rendered_content = main_page_content.format(
            movie_tiles=self.create_movie_titles_content())
        output_file = open(self.output_file_path, 'w')
        output_file.write(main_page_head + rendered_content)
        output_file.close()

    def open_website(self):
        """open the generated html"""
        url = os.path.abspath(self.output_file_path)
        webbrowser.open('file://'+url, new=2)
