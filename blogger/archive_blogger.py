"""
from https://daniel.feldroy.com/posts/2022-02-blogger-to-markdown-script

How to use this script:
1. Go to your blogger account settings
2. Search for the "Back up content" link
3. Download the content as an XML file
4. Run the script with:

    Usage: python legacy.py [OPTIONS] INPUT_FILE OUTPUT_DIR

    Arguments:
      INPUT_FILE  [required]
      OUTPUT_DIR  [required]

    Options:
        --tag TEXT
            Tag to add to frontmatter
            [default: legacy-blogger]
        --show-original / --no-show-original
            Link MD files to original articles
            [default: show-original]

TODOs
1. Remove the odd 'pydanny' specific items
2. Add pure python way to convert HTML to markdown
"""

from bs4 import BeautifulSoup

# from https://stackoverflow.com/questions/42412251/python-strip-string-from-html-tags-leave-links-but-in-changed-form
def cleanComment(comment):
    comment = comment.replace('&nbsp;', ' ')
    soup = BeautifulSoup(comment, 'html.parser')
    for m in soup.find_all('a'):
        if str(m) in comment:
            if not m['href'].startswith("#"):
                    comment = comment.replace(str(m), f"[{m.__dict__['next_element']}]({m['href']})")
    soup = BeautifulSoup(comment, 'html.parser')
    comment = soup.get_text()
    return comment

import sys
from pathlib import Path
import os


try:
    import feedparser
    import typer
    import yaml
except ImportError:
    print("Run 'pip install feedparser typer yaml'")


if __name__ == "__main__":
 #   input_file: Path,
 #   output_dir: Path,
 #   tag: str = typer.Option("legacy-blogger", help="Tag to add to frontmatter"),
 #   show_original: bool = typer.Option(True, help="Link MD files to original articles"),

    input_file = Path('blog-11-12-2022.xml')
    print(f"Parsing data from '{input_file}'")
    output_dir = Path('../posts')
    if not output_dir.exists():
        output_dir.mkdir()
    tag = 'legacy-blogger'
    show_original = True

    raw_text = input_file.read_text()
    # parse the historical data
    data = feedparser.parse(raw_text)
    posts = {}
    for entry in data.entries:
        try:
            # Filter out config data and other junk
            if "tag:blogger.com" in entry.link:
                continue
            if "comments" in entry["href"]:
                continue
            if "#settings" in entry.category:
                continue
            if entry.title == "Template: pydanny":
                continue

            # add comments to entries
            if "#comment" in entry.category:
                posts[entry["thr_in-reply-to"]["href"]].comments.append(entry)
                continue

            # Add entries to the posts and prep for comments
            entry["comments"] = []
            posts[entry.link] = entry
        except KeyError:
            continue

    # Write the markdown files
    print(f"Writing {len(posts)} blogger posts to markdown files")
    for key, value in posts.items():
        # Get a MD filename from the original HTML URL
        filename = value['published'].split('T')[0] + '-' + os.path.basename(key).replace(".html", "")
        postname = filename[11:].replace('.md', '')
        # print('\n',link, data['feed']['link'], filename)
        # Catches some of the configuration elements
        if len(filename.strip()) == 0:
            continue
        # bypasses simple pages, TODO: Provide option to create MD pages
        if filename.startswith("p-"):
            continue
        filename = filename.replace("/", "-")

        frontmatter = {
            "date": value["published"].split("T")[0].replace("-", "/"),
            "title": value["title"],
            "author": "Russ Poldrack"
        }
        postdir = output_dir / postname
        if not postdir.exists():
            postdir.mkdir()
        
        with open(postdir / 'index.qmd', "w") as f:
            # Set the frontmatter
            f.write("---\n")

            #for k, v in frontmatter.items():
            #    f.write(f'{k}: {v}\n')
            postdate = frontmatter['date']
            posttitle = frontmatter['title'].replace(':', '-')
            #f.write(yaml.dump(frontmatter))
            f.write(f'author: "Russ Poldrack"\ndate: {postdate}\ntitle: {posttitle}\n')
            f.write("---\n\n")
            if show_original:
                # Set a link to the original content
                f.write(
                    f"*This was originally posted on blogger [here]({key})*.\n\n"
                )
            # Write the HTML, TODO: consider converting to markdown
            f.write(cleanComment(value["summary"]))
            # If any comments, add them
            if value["comments"]:
                f.write("\n\n---\n\n")
                f.write(
                    f'## {len(value["comments"])} comments captured from [original post]({key}) on Blogger\n\n'
                )
                for comment in value["comments"]:
                    f.write(
                        f"**{comment['author_detail']['name']} said on {comment['published'][:10]}**\n\n"
                    )
                    f.write(comment["summary"])
                    f.write("\n\n")


