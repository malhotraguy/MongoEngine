from mongoengine import *
connect('tumblelog')

class User(Document):
    email = StringField(required=True)
    first_name = StringField(max_length=50)
    last_name = StringField(max_length=50)

class Comment(EmbeddedDocument):
    content = StringField()
    name = StringField(max_length=120)

class Post(Document):
    title = StringField(max_length=120,required=True)
    author = ReferenceField(User,reverse_delete_rule=CASCADE)
    tags = ListField(StringField(max_length=30))
    comments = ListField(EmbeddedDocumentField(Comment))

    meta = {'allow_inheritance':True}

class TextPost(Post):
    content = StringField()

class ImagePost(Post):
    image_post = StringField()

class LinkPost(Post):
    link_url = StringField()



# "Adding Data To Our Tumblelog

ross = User(email="123@abc.com",first_name="Ross",last_name="Lawley").save()

john = User(email="456@def.com",first_name="John",last_name="Mcmath").save()

post1 = TextPost(title="Fun with MongoEngine",author=john)
post1.content = "Took a look at MongoEngine today, it is fun to learn"
post1.tags = ['mongodb','mongoengine']
post1.save()

post2 = LinkPost(title="Another post for learning MongoEngine",author=ross)
post2.link_url = "http://docs.mongoengine.com/"
post2.tags = ['mongoengine']
post2.save()

# For Accessing our Data

for post in Post.objects:
    print(post.title)

# For retrieving type-specific information

for post in TextPost.objects:
    print(post.content)

# For retrieving type-specific information without using subclasses
for post in Post.objects:
    print(post.title)
    print("="*len(post.title))

    if isinstance(post,TextPost):
        print(post.content)
    if isinstance(post,LinkPost):
        print("Link:{}".format(post.link_url))



for post in Post.objects(tags="mongodb"):
    print(post.title)
num_posts= Post.objects(tags="mongodb").count()
print("Found {} posts with tag 'mongodb' ".format(num_posts))
