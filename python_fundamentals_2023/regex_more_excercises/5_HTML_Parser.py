import re

def extract_title_and_content(html):
    title = re.search(r"<title>(.*?)</title>", html, re.DOTALL | re.IGNORECASE)
    content = re.search(r"<body>(.*?)</body>", html, re.DOTALL | re.IGNORECASE)

    title_text = title.group(1).strip()
    content_text = re.sub(r"<.*?>", "", content.group(1)).strip()

    return title_text, content_text

html = input()
clean_html = re.sub(r'\n', '', html)

title, content = extract_title_and_content(clean_html)
print(f"Title: {title}")
print(f"Content: {content}")
