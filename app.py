from flask import Flask, render_template, request, redirect, url_for, flash
from main import Colis, File, Pile

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'  # For flash messages

# Initialize the queue and trucks globally
file = File()
trucks = {1: {"name": "Camion 1", "pile": Pile()}}
next_truck_id = 2

@app.route('/')
def index():
    """Main page - displays queue and trucks"""
    return render_template('index.html', 
                         queue=file.list, 
                         trucks=trucks,
                         queue_count=len(file.list))

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
        flash(f'Colis ajouté à la file d\'attente avec priorité {priorite}', 'success')
    except Exception as e:
        flash(f'Erreur: {str(e)}', 'error')
    
    return redirect(url_for('index'))

@app.route('/add-truck', methods=['POST'])
def add_truck():
    """Create a new truck"""
    global next_truck_id
    try:
        truck_name = request.form.get('truck_name', '').strip()
        if not truck_name:
            truck_name = f"Camion {next_truck_id}"
        
        trucks[next_truck_id] = {"name": truck_name, "pile": Pile()}
        flash(f'{truck_name} créé avec succès', 'success')
        next_truck_id += 1
    except Exception as e:
        flash(f'Erreur: {str(e)}', 'error')
    
    return redirect(url_for('index'))

@app.route('/process/<int:truck_id>', methods=['POST'])
def process_package(truck_id):
    """Move package from queue to specified truck (FIFO)"""
    try:
        if truck_id not in trucks:
            flash('Camion invalide', 'error')
        elif len(file.list) == 0:
            flash('La file d\'attente est vide', 'warning')
        else:
            colis = file.defiler()
            trucks[truck_id]["pile"].ajouter(colis)
            flash(f'Colis {colis.id} transféré vers {trucks[truck_id]["name"]}', 'success')
    except Exception as e:
        flash(f'Erreur: {str(e)}', 'error')
    
    return redirect(url_for('index'))

@app.route('/unload/<int:truck_id>', methods=['POST'])
def unload_package(truck_id):
    """Remove package from specified truck (LIFO)"""
    try:
        if truck_id not in trucks:
            flash('Camion invalide', 'error')
        elif len(trucks[truck_id]["pile"].list) == 0:
            flash(f'{trucks[truck_id]["name"]} est vide', 'warning')
        else:
            colis = trucks[truck_id]["pile"].depiler()
            flash(f'Colis {colis.id} déchargé de {trucks[truck_id]["name"]}', 'success')
    except Exception as e:
        flash(f'Erreur: {str(e)}', 'error')
    
    return redirect(url_for('index'))

@app.route('/sort-queue', methods=['POST'])
def sort_queue():
    """Sort queue by priority (highest first)"""
    try:
        if len(file.list) == 0:
            flash('La file d\'attente est vide', 'warning')
        else:
            file.sort()
            flash('File d\'attente triée par priorité', 'success')
    except Exception as e:
        flash(f'Erreur: {str(e)}', 'error')
    
    return redirect(url_for('index'))

@app.route('/sort-stack/<int:truck_id>', methods=['POST'])
def sort_stack(truck_id):
    """Sort specified truck"""
    try:
        if truck_id not in trucks:
            flash('Camion invalide', 'error')
        elif len(trucks[truck_id]["pile"].list) == 0:
            flash(f'{trucks[truck_id]["name"]} est vide', 'warning')
        else:
            trucks[truck_id]["pile"].sort()
            flash(f'{trucks[truck_id]["name"]} trié', 'success')
    except Exception as e:
        flash(f'Erreur: {str(e)}', 'error')
    
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
