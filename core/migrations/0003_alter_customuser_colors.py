# Generated by Django 4.2 on 2024-10-06 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_customuser_colors'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='colors',
            field=models.CharField(blank=True, choices=[('viridis', 'Viridis'), ('plasma', 'Plasma'), ('magma', 'Magma'), ('inferno', 'Inferno'), ('Blues', 'Blues'), ('BrBG', 'Brown-Blue-Green'), ('BuGn', 'Blue-Green'), ('BuPu', 'Blue-Purple'), ('CMRmap', 'CMRmap'), ('GnBu', 'Green-Blue'), ('Greens', 'Green'), ('Greys', 'Grey'), ('OrRd', 'Orange-Red'), ('Oranges', 'Orange'), ('PRGn', 'Pink-Red-Green'), ('PiYG', 'Pink-Yellow-Green'), ('PuBu', 'Purple-Blue'), ('PuBuGn', 'Purple-Blue-Green'), ('PuOr', 'Purple-Orange'), ('PuRd', 'Purple-Red'), ('Purples', 'Purples'), ('RdBu', 'Red-Blue'), ('RdGy', 'Red-Grey'), ('RdPu', 'Red-Purple'), ('RdYlBu', 'Red-Yellow-Blue'), ('RdYlGn', 'Red-Yellow-Green'), ('Reds', 'Reds'), ('Spectral', 'Spectral'), ('Wistia', 'Wistia'), ('YlGn', 'Yellow-Green'), ('YlGnBu', 'Yellow-Green-Blue'), ('YlOrBr', 'Yellow-Orange-Brown'), ('YlOrRd', 'Yellow-Orange-Red'), ('afmhot', 'Afmhot'), ('autumn', 'Autumn'), ('binary', 'Binary'), ('bone', 'Bone'), ('brg', 'BRG'), ('bwr', 'BWR'), ('cool', 'Cool'), ('coolwarm', 'Coolwarm'), ('copper', 'Copper'), ('cubehelix', 'Cubehelix'), ('flag', 'Flag'), ('gist_earth', 'Gist-earth'), ('gist_gray', 'Gist-gray'), ('gist_heat', 'Gist-heat'), ('gist_ncar', 'Gist-nicar'), ('gist_rainbow', 'Gist-rainbow'), ('gist_stern', 'Gist-stern'), ('gist_yarg', 'Gist-yarg'), ('gnuplot', 'Gnuplot'), ('gnuplot2', 'Gnuplot2'), ('gray', 'Gray'), ('hot', 'Hot'), ('hsv', 'Hsv'), ('jet', 'Jet'), ('nipy_spectral', 'Nipy-spectral'), ('ocean', 'Ocean'), ('pink', 'Pink'), ('prism', 'Prism'), ('rainbow', 'Rainbow'), ('seismic', 'Seismic'), ('spring', 'Spring'), ('summer', 'Summer'), ('terrain', 'Terrain'), ('winter', 'Winter'), ('Accent', 'Accent'), ('Dark2', 'Dark2'), ('Paired', 'Paired'), ('Pastel1', 'Pastel1'), ('Pastel2', 'Pastel2'), ('Set1', 'Set1'), ('Set2', 'Set2'), ('Set3', 'Set3'), ('tab10', 'Tab10'), ('tab20', 'Tab20'), ('tab20b', 'Tab20b'), ('tab20c', 'Tab20c')], default='viridis', max_length=50),
        ),
    ]
