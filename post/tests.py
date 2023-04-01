from django.test import TestCase

# Create your tests here.

from post.models import Post,Audio,Video

class ModelsTest(TestCase):

    @classmethod
    def setUp(self):
        #Set up non-modified objects used by all test methods
        Post.objects.create(title ="Google is bad", text = "clickbait", author = "Bada")
        Audio.objects.create(name = "man doing flip", link = "https://www.youtube.com//watch?v=dQw4w9WgXcQ", description = "this is very cool")
        Video.objects.create(name = "raining tacos",link  = "pinchilin", time = "1:33")

    def test_posts(self):
        post = Client.objects.get(id=1)
        excepted_object_name = "%s" % (post.title)
        self.assertEquals(expected_object_name, str(post))

    def test_audio(self):
        audio = audio.objects.get(id=1)
        excepted_object_name = "%s" % (audio.title)
        self.assertEquals(expected_object_name, str(audio))

    def test_video(self):
        video = video.objects.get(id=1)
        excepted_object_name = "%s" % (video.title)
        self.assertEquals(expected_object_name, str(video))

    def test_posts_title(self):
        posts = Post.objects.get(id=1)
        max_length = posts._meta.getfield('title').max_length
        self.assertEquals(max_length,200)

    def test_posts_author(self):
        posts = Post.objects.get(id=1)
        max_length = posts._meta.getfield('author').max_length
        self.assertEquals(max_length,50)


    def test_audios_name(self):
        audios = Audio.objects.get(id=1)
        max_length = audios._meta.getfield('name').max_length
        self.assertEquals(max_length,200)

    def test_videos_name(self):
        videos = Video.objects.get(id=1)
        max_length = videos._meta.getfield('name').max_length
        self.assertEquals(max_length,200)