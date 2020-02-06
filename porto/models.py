from django.db import models
import datetime
import datetime
def annee():
    return [(r,r) for r in range(1984, datetime.date.today().year+1)]

class AboutMe(models.Model):
    """Model definition for AboutMe."""
    titre = models.CharField(max_length=50)
    description = models.TextField()
    # TODO: Define fields here

    class Meta:
        """Meta definition for AboutMe."""

        verbose_name = 'AboutMe'
        verbose_name_plural = 'AboutMes'

    def __str__(self):
        """Unicode representation of AboutMe."""
        return self.titre
################################################################
################################################################
class CompetenceFor(models.Model):
    """Model definition for CompetenceFor."""
    div_class = models.CharField(max_length=50)
    i_class = models.CharField(max_length=50)
    titre = models.CharField(max_length=50)
    description = models.TextField()
    # TODO: Define fields here

    class Meta:
        """Meta definition for CompetenceFor."""

        verbose_name = 'CompetenceFor'
        verbose_name_plural = 'CompetenceFors'

    def __str__(self):
        """Unicode representation of CompetenceFor."""
        return self.titre
################################################################
################################################################
class SloganOrange(models.Model):
    """Model definition for SloganOrange."""
    titre = models.TextField()
    button_titre = models.CharField(max_length=50)
    # TODO: Define fields here

    class Meta:
        """Meta definition for SloganOrange."""

        verbose_name = 'SloganOrange'
        verbose_name_plural = 'SloganOranges'

    def __str__(self):
        """Unicode representation of SloganOrange."""
        return self.titre
################################################################
################################################################
class Expertise(models.Model):
    """Model definition for Expertis."""
    div_class = models.CharField(max_length=50)
    i_class = models.CharField(max_length=50)
    titre = models.CharField(max_length=50)
    description = models.TextField()
    # TODO: Define fields here

    class Meta:
        """Meta definition for Expertise."""

        verbose_name = 'Expertis'
        verbose_name_plural = 'Expertises'

    def __str__(self):
        """Unicode representation of Expertise."""
        return self.titre
################################################################
################################################################
class Compteur(models.Model):
    """Model definition for Compteur."""
    data_to = models.IntegerField()
    data_speed = models.IntegerField()
    data_refresh_interval = models.IntegerField()
    label = models.CharField(max_length=50)
    # TODO: Define fields here

    class Meta:
        """Meta definition for Compteur."""

        verbose_name = 'Compteur'
        verbose_name_plural = 'Compteurs'

    def __str__(self):
        """Unicode representation of Compteur."""
        return self.label
################################################################
################################################################
class Beforeskills(models.Model):
    """Model definition for beforeskills."""
    description = models.TextField()

    # TODO: Define fields here

    class Meta:
        """Meta definition for beforeskills."""

        verbose_name = 'beforeskills'
        verbose_name_plural = 'beforeskillss'

    def __str__(self):
        """Unicode representation of beforeskills."""
        return self.description

################################################################
################################################################

class Skills(models.Model):
    """Model definition for Skills."""
    language = models.CharField(max_length=50)
    couleur = models.CharField(max_length=50)
    value = models.IntegerField()
    # TODO: Define fields here

    class Meta:
        """Meta definition for Skills."""

        verbose_name = 'Skills'
        verbose_name_plural = 'Skillss'

    def __str__(self):
        """Unicode representation of Skills."""
        return self.language
################################################################
################################################################
class Education(models.Model):
    """Model definition for Education."""
    titre = models.CharField(max_length=50)
    description = models.TextField()
    activite1 = models.CharField(max_length=50, blank=True, null=True)
    activite2 = models.CharField(max_length=50, blank=True, null=True)
    activite3 = models.CharField(max_length=50, blank=True, null=True)
    activite4 = models.CharField(max_length=50, blank=True, null=True)
    activite5 = models.CharField(max_length=50, blank=True, null=True)
    # TODO: Define fields here

    class Meta:
        """Meta definition for Education."""

        verbose_name = 'Education'
        verbose_name_plural = 'Educations'

    def __str__(self):
        """Unicode representation of Education."""
        return self.titre
################################################################
################################################################
class Work(models.Model):
    div_class = models.CharField(max_length=50)
    i_class = models.CharField(max_length=50)
    fade = models.CharField(max_length=50, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    titre = models.CharField(max_length=50)
    de = models.IntegerField(default=datetime.date.today().year+1)
    a  = models.IntegerField(   default=datetime.date.today().year+1)
    
    """Model definition for Work."""

    # TODO: Define fields here

    class Meta:
        """Meta definition for Work."""

        verbose_name = 'Work'
        verbose_name_plural = 'Works'

    def __str__(self):
        """Unicode representation of Work."""
        return self.titre
################################################################
################################################################
class Contact(models.Model):
    """Model definition for Contact."""
    email = models.CharField(max_length=50)
    rue = models.CharField(max_length=50)
    ville = models.CharField(max_length=50)
    telephone = models.CharField(max_length=50)
    # TODO: Define fields here

    class Meta:
        """Meta definition for Contact."""

        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'

    def __str__(self):
        """Unicode representation of Contact."""
        return self.email
################################################################
################################################################
class Info(models.Model):
    """Model definition for Info."""
    nom = models.CharField(max_length=50)
    role = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='images/', height_field=None, width_field=None, max_length=None)
    # TODO: Define fields here

    class Meta:
        """Meta definition for Info."""

        verbose_name = 'Info'
        verbose_name_plural = 'Infos'

    def __str__(self):
        """Unicode representation of Info."""
        return self.nom
################################################################
################################################################
class Liens(models.Model):
    """Model definition for Liens."""
    titre = models.CharField(max_length=50)
    lien = models.CharField(max_length=50)
    # TODO: Define fields here

    class Meta:
        """Meta definition for Liens."""

        verbose_name = 'Liens'
        verbose_name_plural = 'Lienss'

    def __str__(self):
        """Unicode representation of Liens."""
        return self.titre
################################################################
################################################################
class ProjectList(models.Model):
    """Model definition for ProjectList."""
    fadein = models.CharField(max_length=50)
    lien   = models.CharField(max_length=50)
    image  = models.ImageField(upload_to='images/', height_field=None, width_field=None, max_length=None)
    titre1 = models.CharField(max_length=50)
    titre2 = models.CharField(max_length=50)
    vue    = models.IntegerField(blank=True, null=True)
    aime   = models.IntegerField(blank=True, null=True)
    url_partage = models.CharField(max_length=50, blank=True, null=True)
    
    

    # TODO: Define fields here

    class Meta:
        """Meta definition for ProjectList."""

        verbose_name = 'ProjectList'
        verbose_name_plural = 'ProjectLists'

    def __str__(self):
        """Unicode representation of ProjectList."""
        return self.titre1
################################################################
################################################################
class CopyRight(models.Model):
    """Model definition for CopyRight."""
    droit = models.CharField(max_length=50)
    url = models.CharField(max_length=50)
    titre = models.CharField(max_length=50)
    

    # TODO: Define fields here

    class Meta:
        """Meta definition for CopyRight."""

        verbose_name = 'CopyRight'
        verbose_name_plural = 'CopyRights'

    def __str__(self):
        """Unicode representation of CopyRight."""
        return self.titre
    
################################################################
################################################################
class Header(models.Model):
    """Model definition for Header."""
    hello1 = models.CharField(max_length=50)
    bg1 = models.ImageField(upload_to='images', height_field=None, width_field=None, max_length=None,default="img_bg_1.jpeg")
    qui = models.CharField(max_length=50)
    github = models.CharField(max_length=50)
    titre = models.CharField(max_length=50)
    cv_url = models.CharField(max_length=50)
    hello2 = models.CharField(max_length=50)
    bg2 = models.ImageField(upload_to='images/', height_field=None, width_field=None, max_length=None,default='img_bg_1.jpeg')
    portfolio_url = models.CharField(max_length=50)
    titre_button_portfolio = models.CharField(max_length=50)

    # TODO: Define fields here

    class Meta:
        """Meta definition for Header."""

        verbose_name = 'Header'
        verbose_name_plural = 'Headers'

    def __str__(self):
        """Unicode representation of Header."""
        return self.hello1

