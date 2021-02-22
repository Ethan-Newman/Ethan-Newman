
import tweepy

#AUTHENTICATION
class AuthBot:
    consumer_token = 'B9KX3vUWconaVvoX5qb58N5sM'
    consumer_secret = 'oqOLzpDJm56pXYJI7ieGJJEdHFDljaAN7xSIK0hIofo7Y8DT1t'
    access_token = '1359899886162960388-pNNP9ZyKj4ltVKSPXau7Ugry7hlq4j'
    access_secret = 'dxLx8JS1IWROHir1TcARxem26oqcwEcivQewzGSxE1ViJ'

    def Authenticate(self):
        auth = tweepy.OAuthHandler(self.consumer_token, self.consumer_secret)
        auth.set_access_token(self.access_token, self.access_secret)
        api = tweepy.API(auth)
        return api
    