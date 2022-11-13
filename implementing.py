import requests
import lxml.html

# requesting url
web_response = requests.get('http://pyresearch.herokuapp.com//')

# building
element_tree = lxml.html.fromstring(web_response.text)

tree_title_element = element_tree.xpath('//title')[0]

print("Tag title : ", tree_title_element.tag)
print("\nText title :", tree_title_element.text_content())
print("\nhtml title :", lxml.html.tostring(tree_title_element))
print("\ntitle tag:", tree_title_element.tag)
print("\nParent's tag title:", tree_title_element.getparent().tag)
