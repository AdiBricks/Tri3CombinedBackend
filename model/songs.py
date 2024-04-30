# I created this code as part of a different repo. Then for the purposes of this repo, I added and modified it to fit
# Backend file: This file sets up the sqlite database for the songs 

from __init__ import app, db

class Song(db.Model):  
    __tablename__ = 'songs'  

    id = db.Column(db.Integer, primary_key=True)
    _name = db.Column(db.String(255), unique=False, nullable=False)
    _url = db.Column(db.String(255), unique = False, nullable=False)
    _description = db.Column(db.String(255), unique=True, nullable=False)
    _uri = db.Column(db.String(255), unique=False, nullable=False)
    _tokens = db.Column(db.Integer)
    
    def __init__(self, name, url, description, uri, tokens):
        self._name = name
        self._description = description
        self._url = url  # Corrected assignment to _url
        self._uri = uri
        self._tokens = tokens

    def to_dict(self):
        return {"id": self.id, "_name": self._name, "url": self._url, "_description": self._description, "_uri": self._uri, "_tokens": self._tokens}
    
    def update(self, name="", url="", uri=""):
        """only updates values with length"""
        if len(name) > 0:
            self.name = name
        if len(url) > 0:
            self.url = uri
        if len(uri) > 0:
            self.uri = uri
        db.session.commit()
        return self

# Function to create songs, store them in JSON format, and return the created songs
def initSongs():
    with app.app_context():

        db.create_all()
        
        songs_data = [
    {'name': 'FEIN', 'url': '/audios/FEIN.mp3', 'description': 'Travis Scott_', 'uri': 'https://i.ibb.co/9t3PTg0/fein.jpg', 'tokens':'1'},
    {'name':'Creepin', 'url':'/audios/CREEP.mp3', 'description':'The Weeknd', 'uri':'https://i1.sndcdn.com/artworks-sWl8wb2Zk1xthx3m-39RYRQ-t500x500.jpg', 'tokens':'2'},
    {'name':'Role Model', 'url':'', 'description':' Brent Fiaiyaz', 'uri':'https://i1.sndcdn.com/artworks-O2SRR9SCgyRq4u4v-eAojjA-t500x500.jpg', 'tokens':'3'},
    {'name':'Right my Wrongs', 'url':'', 'description':' Bryson Tiller', 'uri':'https://i.scdn.co/image/ab67616d0000b273d5f3cea8affdca01a0dc754f', 'tokens':'4'},
    {'name':'Roar', 'url':'', 'description':' Katy Perry', 'uri':'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT_Y92S1N976xSO57PbyPinyoJ8IVnqGPFhLQ&usqp=CAU', 'tokens':'5'},
    {'name':'Shake it Off', 'url':'/audios/SHAKE.mp3', 'description':' Taylor Swift', 'uri':'https://pyxis.nymag.com/v1/imgs/2d9/6f5/3f8dbd63613637b7843e4653ff548503b9-tay--.w710.jpg', 'tokens':'6'},
    {'name':'Often', 'url':'/audios/OFTEN.mp3', 'description':' The Weeknd_', 'uri':'https://cdns-images.dzcdn.net/images/cover/eea9f7fc913300e40307a0ff70dc73cf/350x350.jpg', 'tokens':'7'},
    {'name':'Thank God', 'url':'', 'description':' Travis Scott', 'uri':'https://i.ibb.co/9t3PTg0/fein.jpg', 'tokens':'8'},
    {'name':'God Did ', 'url':'', 'description':' DJ Khalid', 'uri':'https://upload.wikimedia.org/wikipedia/en/0/0a/DJ_Khaled_-_God_Did.png', 'tokens':'9'},
    {'name':'Badtameez Dil', 'url':'', 'description':' Yeh Jawaani Hai Deewani', 'uri':'https://m.media-amazon.com/images/M/MV5BNWIxZWU1YzAtYTc4NS00NTM4LWJmODgtYzEwNTE0NmJiYzI4XkEyXkFqcGdeQXVyODk2ODI3MTU@._V1_UX200_CR0,0,200,200_AL_.jpg', 'tokens':'10'},
    {'name':'Same Old Love', 'url':'', 'description':' Selena Gomez', 'uri':'https://upload.wikimedia.org/wikipedia/en/b/b3/Same_Old_Love_by_Selena_Gomez.png', 'tokens':'11'},
    {'name':'Waka Waka ', 'url':'', 'description':' Shakira', 'uri':'https://photos.prnewswire.com/prnfull/20100901/NY58538-a', 'tokens':'12'},
    {'name':'Swim', 'url':'', 'description':' Chase Atlantic ', 'uri':'https://i.ytimg.com/vi/ykP640XEjSQ/maxresdefault.jpg', 'tokens':'13'},
    {'name':'Fireside', 'url':'', 'description':' Arctic Monkeys', 'uri':'https://i.ytimg.com/vi/PG8yTUeptFU/maxresdefault.jpg', 'tokens':'14'},
    {'name':'Daddy Issues', 'url':'', 'description':' The Neighborhood', 'uri':'https://i.scdn.co/image/ab67616d0000b2733066581d697fbdee4303d685', 'tokens':'15'},
    {'name':'Art Deco', 'url':'', 'description':'Lana Del Rey ', 'uri':'https://i1.sndcdn.com/artworks-000144834419-kkxrj8-t500x500.jpg', 'tokens':'16'},
    {'name':'The Color Violet', 'url':'/audios/COLOR.mp3', 'description':' Tory Lanez ', 'uri':'https://i1.sndcdn.com/artworks-XTdw6XGAR3WX-0-t500x500.jpg', 'tokens':'17'},
    {'name':'Light it Up', 'url':'', 'description':' Major Lazer', 'uri':'https://i.ytimg.com/vi/r2LpOUwca94/maxresdefault.jpg', 'tokens':'18'},
    {'name':'Maneater', 'url':'', 'description':' Nelly Furtado ', 'uri':'https://upload.wikimedia.org/wikipedia/en/5/56/Maneater_%28Nelly_Furtado_single_-_cover_art%29.png', 'tokens':'19'},
    {'name':'Dark Horse', 'url':'', 'description':' Katy Perry ', 'uri':'https://static.independent.co.uk/s3fs-public/thumbnails/image/2014/02/26/10/katy-perry-dark-horse-v2.jpg', 'tokens':'20'},
    {'name':'Watch', 'url':'', 'description':' Billie Eilish ', 'uri':'https://thomasbleach.files.wordpress.com/2017/07/billie.jpg', 'tokens':'21'},
    {'name':'Eyes Without Face', 'url':'', 'description':' Billy Idol ', 'uri':'https://i.ytimg.com/vi/e7U1YZNgwnY/maxresdefault.jpg', 'tokens':'22'},
    {'name':'Good Days', 'url':'', 'description':' SZA', 'uri':'https://upload.wikimedia.org/wikipedia/en/7/7c/SZA_-_Good_Days.png', 'tokens':'23'},
    {'name':'sdp interlude', 'url':'', 'description':'Travis Scott ', 'uri':'https://i.scdn.co/image/ab67616d0000b273f54b99bf27cda88f4a7403ce', 'tokens':'24'},
    {'name':'Mary', 'url':'', 'description':' Alex G ', 'uri':'https://i.scdn.co/image/ab67616d0000b273c85ca3b845a922baff3041c7', 'tokens':'25'},
    {'name':'Flashing Lights', 'url':'', 'description':'Kanye West ', 'uri':'https://i.scdn.co/image/ab67616d0000b27326f7f19c7f0381e56156c94a', 'tokens':'26'},
    {'name':'Trust issues', 'url':'', 'description':'Drake', 'uri':'https://i1.sndcdn.com/artworks-QHAz47bKkwaj-0-t500x500.jpg', 'tokens':'27'},
    {'name':'Gods Plan', 'url':'', 'description':'Drake ', 'uri':'https://i.ytimg.com/vi/m1a_GqJf02M/maxresdefault.jpg', 'tokens':'28'},
    {'name':'Time to Pretend', 'url':'', 'description':'MGMT ', 'uri':'https://i.scdn.co/image/ab67616d0000b2738b32b139981e79f2ebe005eb', 'tokens':'29'},
    {'name':'Sensei Wu', 'url':'/audios/WU.mp3', 'description':' Ian Wu Father ', 'uri':'https://m.media-amazon.com/images/I/51Zl1Tdk3YL._AC_UF894,1000_QL80_.jpg', 'tokens':'30'},
    ]

        
        # iterate
        for song_data in songs_data:
            existing_song = Song.query.filter_by(_name=song_data['name']).first()
            # If user exists, print a message and update user data
            if existing_song:
                print(f"User with _uid '{song_data['name']}' already exists. Updating user data.")
                existing_song.update(
                    name=song_data['name'],
                    url=song_data['url'],
                    uri=song_data['uri'],
                )
                # If user does not exist, create a new user and add to the database
            else:
                new_song = Song(
                    name=song_data['name'],
                    url=song_data['url'],
                    description=song_data['description'],
                    uri=song_data['uri'],
                    tokens=song_data['tokens']   
                )
                db.session.add(new_song)
        db.session.commit()
        
        
if __name__ == "__main__":
    initSongs()
