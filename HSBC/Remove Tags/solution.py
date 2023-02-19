import pandas as pd
class Solution:
    # I could use regex, but I don't want to exclude something that looks like a tag but it's actually not
    tag_list = pd.read_html("https://www.w3schools.com/TAGS/default.asp")[0]["Tag"]
    def remove_tags(self, input):
            for tag in self.tag_list:
                input = input.replace(tag, "").replace(tag[0]+"/"+tag[1:], "")
            return input