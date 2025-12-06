from textnode import TextNode
from textnode import TextType

# Static Site Generator Main Script
def main():

    print("hello world")
    print("Starting static site generator...")
    # Additional logic for the static site generator would go here

    TextNode1 = TextNode("Google site", text_type=TextType.LINK, url="https://www.google.com")
    print(TextNode1)

    TextNode2 = TextNode("Google site", text_type=TextType.LINK, url="https://www.google.com")
    print(TextNode2)

    if( TextNode1 == TextNode2):
        print("The two text nodes are equal.")
    else:
        print("The two text nodes are not equal.")

if __name__ == "__main__":
    main()