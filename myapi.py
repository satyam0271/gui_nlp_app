import nlpcloud

# api_key = "b89d6a5c5778b2471f6077f2f2edc98abe28a7e6"
# client = nlpcloud.Client("<model>", "<token>")


class API:

    def __init__(self):
        self.api_key = "b89d6a5c5778b2471f6077f2f2edc98abe28a7e6"

    def sentiment_analysis(self,text):
        model = "gpt-oss-120b"

        client = nlpcloud.Client(model,self.api_key,gpu = True)
        response = client.sentiment(text,target="NLP Cloud")
        return response

    def headline_generation(self,text):
        model = "t5-base-en-generate-headline"

        client = nlpcloud.Client(model,self.api_key, gpu=False)
        response = client.summarization(text)
        return response

    def ner(self,text,entity):
        model = "gpt-oss-120b"

        client = nlpcloud.Client(model,self.api_key, gpu=True)
        response = client.entities(text,searched_entity=entity)
        return response

