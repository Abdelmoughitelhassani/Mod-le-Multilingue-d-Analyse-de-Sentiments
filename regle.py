import nbformat

# Charger le notebook
with open("arabe_notebook.ipynb", "r", encoding="utf-8") as f:
    nb = nbformat.read(f, as_version=4)

# Supprimer les widgets cassés dans les métadonnées (mais garder les outputs)
if 'widgets' in nb['metadata']:
    del nb['metadata']['widgets']

# Sauvegarder le notebook réparé
with open("arabe_notebook_fixed.ipynb", "w", encoding="utf-8") as f:
    nbformat.write(nb, f)

print("✅ Notebook corrigé et sauvegardé sous 'arabe_notebook_fixed.ipynb'")
