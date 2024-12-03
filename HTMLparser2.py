from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_comment(self,data):
        if N>1 in data:
            print(f">>>Multi-line Comment",data,sep="\n")
        else:
            print(f">>>Single-line Comment",data,sep="\n")

        
    def handle_data(self,data):
        print(f">>>Data",data,sep="\n")


parser = MyHTMLParser()
for i in range(int(input())):
    parser.feed(input())
    