from django.contrib import admin
from .models import Post
from .models import About
from .models import Project
from .models import Other
from .models import Contact

admin.site.register(Post)
admin.site.register(About)
admin.site.register(Project)
admin.site.register(Other)
admin.site.register(Contact)
