from flask import Flask, render_template, request, redirect, url_for, flash
from main import Colis, File, Pile

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'  # For flash messages

# Initialize the queue and stack globally
file = File()
pile = Pile()

@app.route('/')
def index():
    """Main page - displays queue and stack"""
    return render_template('index.html', 
                         queue=file.list, 
                         stack=pile.list,
                         queue_count=len(file.list),
                         stack_count=len(pile.list))

@app.route('/add', methods=['POST'])
def add_package():
    """Add a package to the queue"""
    try:
        priorite = int(request.form.get('priority'))
        poid = float(request.form.get('weight'))
        destination = request.form.get('destination', '').strip()
        
        if not destination:
            destination = None
            
        file.ajouter(priorite, poid, destination)
        flash(f'✅ Colis ajouté à la file d\'attente avec priorité {priorite}', 'success')
    except Exception as e:
        flash(f'⚠️ Erreur: {str(e)}', 'error')
    
    return redirect(url_for('index'))

@app.route('/process', methods=['POST'])
def process_package():
    """Move package from queue to stack (FIFO)"""
    try:
        if len(file.list) == 0:
            flash('⚠️ La file d\'attente est vide', 'warning')
        else:
            colis = file.defiler()
            pile.ajouter(colis)
            flash(f'✅ Colis {colis.id} transféré vers le camion', 'success')
    except Exception as e:
        flash(f'⚠️ Erreur: {str(e)}', 'error')
    
    return redirect(url_for('index'))

@app.route('/unload', methods=['POST'])
def unload_package():
    """Remove package from stack (LIFO)"""
    try:
        if len(pile.list) == 0:
            flash('⚠️ Le camion est vide', 'warning')
        else:
            colis = pile.depiler()
            flash(f'✅ Colis {colis.id} déchargé du camion', 'success')
    except Exception as e:
        flash(f'⚠️ Erreur: {str(e)}', 'error')
    
    return redirect(url_for('index'))

@app.route('/sort-queue', methods=['POST'])
def sort_queue():
    """Sort queue by priority (highest first)"""
    try:
        if len(file.list) == 0:
            flash('⚠️ La file d\'attente est vide', 'warning')
        else:
            file.sort()
            flash('✅ File d\'attente triée par priorité', 'success')
    except Exception as e:
        flash(f'⚠️ Erreur: {str(e)}', 'error')
    
    return redirect(url_for('index'))

@app.route('/sort-stack', methods=['POST'])
def sort_stack():
    """Sort stack"""
    try:
        if len(pile.list) == 0:
            flash('⚠️ Le camion est vide', 'warning')
        else:
            pile.sort()
            flash('✅ Camion trié', 'success')
    except Exception as e:
        flash(f'⚠️ Erreur: {str(e)}', 'error')
    
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
