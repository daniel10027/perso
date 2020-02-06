from django.contrib import admin
from .models import (AboutMe,
                    
                     SloganOrange, 
                     Expertise,
                     Contact,
                     Compteur,
                     Skills, 
                     Beforeskills,
                     Education, 
                     Work,
                     Info, 
                     Liens,
                     ProjectList,
                     CompetenceFor,
                     CopyRight,
                     Header )
# Register your models here.

admin.site.register(AboutMe)
admin.site.register(CompetenceFor)
admin.site.register(Compteur)
admin.site.register(SloganOrange)
admin.site.register(Expertise)
admin.site.register(Skills)
admin.site.register(Education)
admin.site.register(Work)
admin.site.register(Contact)
admin.site.register(Info)
admin.site.register(Beforeskills)
admin.site.register(Liens)
admin.site.register(ProjectList)
admin.site.register(CopyRight)
admin.site.register(Header)