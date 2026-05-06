# Images pour DB HIVE ENTREPRISE

## Comment ajouter des images réelles

Pour remplacer les placeholders par de vraies images :

1. **Images recommandées** :
   - Logo de l'entreprise : `logo.png` (200x200px)
   - Hero image : `hero-commerce.jpg` (1200x600px) - Commerce international
   - Services : 
     - `import-export.jpg` - Conteneurs, ports
     - `equipements.jpg` - Machines industrielles
     - `logistique.jpg` - Transport, entrepôts
     - `representation.jpg` - Partenariats commerciaux

2. **Placez les images** dans ce dossier (`static/images/`)

3. **Utilisez-les dans les templates** avec :
   ```html
   <img src="{% static 'images/nom-image.jpg' %}" alt="Description" class="img-fluid">
   ```

4. **Tailles recommandées** :
   - Hero : 1200x600px
   - Cartes services : 400x250px
   - Logo : 200x200px
   - Images de section : 800x500px

## Sources d'images libres de droits

- Unsplash.com
- Pexels.com
- Pixabay.com

Recherchez : "international trade", "shipping", "warehouse", "industrial equipment", "Africa commerce"
