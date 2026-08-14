import requests

url = "https://weather.tsukumijima.net/api/forecast"

params = {'city':400040}

data = requests.get(url,params=params).json()

def publicTimeFormatted():
    publicTimeFormatted = data['publicTimeFormatted']
    return publicTimeFormatted

def title():
    title = data['title']
    return title

class description:
    description = data['description']
    
    def publicTimeFormatted(self):
        publicTimeFormatted = self.description['publicTimeFormatted']
        return publicTimeFormatted
    
    def headlineText(self):
        headlineText = self.description['headlineText']
        if headlineText == "":
            headlineText = "見出し文空白"
        return headlineText
    
    def bodyText(self):
        bodyText = self.description['bodyText']
        if bodyText == "":
            bodyText = "概況文無し"
        return bodyText
