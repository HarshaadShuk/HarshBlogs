from bs4 import BeautifulSoup
import random
thumbnails=["tn1.jpg",'tn2.jpg','tn3.jpg','tn4.jpg','tn5.jpg','tn6.jpg','tn7.jpg','tn8.jpg',"tn9.jpg","tn10.jpg"]
def newpage(new_articles):
    for article in new_articles:
        titleofarticle=article['title']
        contentofarticle=article['content']
        with open(f"{title}.html","w", encoding='utf-8') as page:
            template=f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Blog Title 1</title>
        <link rel="stylesheet" href="styles.css">
    </head>
    <body>
        <header>
            <nav>
                <div class="logo">My Blog</div>
                <ul>
                    <li><a href="#home">Home</a></li>
                    <li><a href="#about">About</a></li>
                    <li><a href="#contact">Contact</a></li>
                </ul>
                <input type="text" id="searchBar" placeholder="Search...">
            </nav>
        </header>

        <main>
            <article class="blog-post">
                <h1>{titleofarticle}</h1>
                <p>{contentofarticle}</p>
            </article>
        </main>

        <footer>
            <p>&copy; 2024 My Blog. All rights reserved.</p>
        </footer>

        <script src="scripts.js"></script>
    </body>
    </html>


    """
            page.write(template)



def add_articles_to_section(file_path, new_articles):
    # Read the existing HTML file
    with open(file_path, 'r', encoding='utf-8') as file:
        soup = BeautifulSoup(file, 'html.parser')

    # Find the main blog-grid container
    blog_grid = soup.find('div', class_='blog-grid')

    # Add new articles to the blog grid
    for article in new_articles:
        img_src=article['image_src']
        titleofarticle=article['title']
        contentofarticle=article['content']


        blog_tile = soup.new_tag('div', **{'class': 'blog-tile'})

        img_tag = soup.new_tag('img', src=img_src, alt='Blog Thumbnail')
        blog_tile.append(img_tag)

        h2_tag = soup.new_tag('h2')
        h2_tag.string = titleofarticle
        blog_tile.append(h2_tag)

        p_tag = soup.new_tag('p', **{'class': 'preview'})
        p_tag.string = contentofarticle  # Show a preview of the content
        blog_tile.append(p_tag)

        a_tag = soup.new_tag('a', href=f'{titleofarticle}.html'.format(len(blog_grid.find_all('div')) + 1), **{'class': 'read-more'})
        a_tag.string = 'Read More'
        blog_tile.append(a_tag)

        blog_grid.append(blog_tile)
        # print(blog_tile)
    # Write the updated HTML back to the file
    with open(file_path, 'w' , encoding='utf-8') as file:
        file.write(str(soup))

# Example usage
title, content = input("Enter the name of your Title: "),input("Enter content: ")
new_articles = [
    {
        'image_src': random.choice(thumbnails),
        'title': title,
        'content': content
    },
]

add_articles_to_section(file_path='index.html', new_articles=new_articles)
newpage(new_articles)
