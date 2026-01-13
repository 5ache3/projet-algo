
let queue = [];
let stack = [];
let arrivalCounter = 0;


function enqueue(parcel) {
    queue.push(parcel);
    updateDisplay();
}

function dequeue() {
    if (queue.length === 0) return null;
    const parcel = queue.shift();
    updateDisplay();
    return parcel;
}


function pushToStack(parcel) {
    stack.push(parcel);
    updateDisplay();
}

function popFromStack() {
    if (stack.length === 0) return null;
    const parcel = stack.pop();
    updateDisplay();
    return parcel;
}


function addParcel() {
    const id = document.getElementById('parcelId').value.trim();
    const priority = parseInt(document.getElementById('parcelPriority').value);
    const weight = parseFloat(document.getElementById('parcelWeight').value);
    const destination = document.getElementById('parcelDestination').value.trim();

    
    if (!id) {
        alert('⚠️ Veuillez entrer un ID de colis.');
        return;
    }

    if (priority < 1 || priority > 5) {
        alert('⚠️ La priorité doit être entre 1 et 5.');
        return;
    }

    if (!weight || weight <= 0) {
        alert('⚠️ Veuillez entrer un poids valide.');
        return;
    }

  
    const isDuplicate = [...queue, ...stack].some(p => p.id === id);
    if (isDuplicate) {
        alert('⚠️ Un colis avec cet ID existe déjà !');
        return;
    }

    
    const parcel = {
        id: id,
        priority: priority,
        weight: weight,
        destination: destination || 'Non spécifié',
        arrivalOrder: ++arrivalCounter
    };

    
    enqueue(parcel);

  
    document.getElementById('parcelId').value = '';
    document.getElementById('parcelPriority').value = '3';
    document.getElementById('parcelWeight').value = '';
    document.getElementById('parcelDestination').value = '';

    alert('✅ Colis ajouté à la file d\'attente !');
}


function processParcel() {
    if (queue.length === 0) {
        alert('⚠️ La file d\'attente est vide !');
        return;
    }

    const parcel = dequeue();
    pushToStack(parcel);
    alert(`✅ Colis ${parcel.id} transféré vers le camion !`);
}


function unloadTruck() {
    if (stack.length === 0) {
        alert('⚠️ Le camion est vide !');
        return;
    }

    const parcel = popFromStack();
    alert(`✅ Colis ${parcel.id} déchargé du camion !`);
}


function sortQueue() {
    if (queue.length === 0) {
        alert('⚠️ La file d\'attente est vide !');
        return;
    }

    queue.sort((a, b) => {
        if (b.priority !== a.priority) {
            return b.priority - a.priority;
        }
        return a.arrivalOrder - b.arrivalOrder;
    });

    updateDisplay();
    alert('✅ File d\'attente triée par priorité !');
}


function sortStack() {
    if (stack.length === 0) {
        alert('⚠️ Le camion est vide !');
        return;
    }

    stack.sort((a, b) => a.weight - b.weight);
    updateDisplay();
    alert('✅ Camion trié par poids !');
}

function getPriorityColor(priority) {
    const colors = {
        1: 'from-emerald-400 to-green-500',
        2: 'from-blue-400 to-blue-500',
        3: 'from-amber-400 to-orange-500',
        4: 'from-red-400 to-red-500',
        5: 'from-rose-500 to-red-600'
    };
    return colors[priority] || 'from-gray-400 to-gray-500';
}


function getPriorityBorder(priority) {
    const borders = {
        1: 'border-l-emerald-500',
        2: 'border-l-blue-500',
        3: 'border-l-amber-500',
        4: 'border-l-red-500',
        5: 'border-l-rose-600'
    };
    return borders[priority] || 'border-l-gray-500';
}


function createParcelCard(parcel) {
    return `
        <div class="bg-gradient-to-r from-gray-50 to-gray-100 p-5 mb-3 rounded-xl border-l-4 ${getPriorityBorder(parcel.priority)} shadow-md hover:shadow-xl hover:scale-[1.02] transition-all duration-200 animate-slide-in">
            <div class="flex justify-between items-center mb-3">
                <span class="text-lg font-bold text-gray-800">Colis ${parcel.id}</span>
                <span class="px-4 py-1 bg-gradient-to-r ${getPriorityColor(parcel.priority)} text-white font-semibold rounded-full text-sm shadow-md">
                    Priorité ${parcel.priority}
                </span>
            </div>
            <div class="grid grid-cols-3 gap-3 text-sm text-gray-600">
                <div>
                    <span class="font-semibold text-gray-800">Poids:</span> ${parcel.weight} kg
                </div>
                <div>
                    <span class="font-semibold text-gray-800">Destination:</span> ${parcel.destination}
                </div>
                <div>
                    <span class="font-semibold text-gray-800">Ordre:</span> #${parcel.arrivalOrder}
                </div>
            </div>
        </div>
    `;
}


function updateDisplay() {
    const queueContainer = document.getElementById('queueContainer');
    const queueCount = document.getElementById('queueCount');
    
    if (queue.length === 0) {
        queueContainer.innerHTML = `
            <div class="text-center text-gray-400 py-16 italic">
                Aucun colis dans la file d'attente
            </div>
        `;
    } else {
        queueContainer.innerHTML = queue.map(parcel => createParcelCard(parcel)).join('');
    }
    queueCount.textContent = queue.length;

    
    const stackContainer = document.getElementById('stackContainer');
    const stackCount = document.getElementById('stackCount');
    
    if (stack.length === 0) {
        stackContainer.innerHTML = `
            <div class="text-center text-gray-400 py-16 italic">
                Le camion est vide
            </div>
        `;
    } else {
       
        stackContainer.innerHTML = [...stack].reverse().map(parcel => createParcelCard(parcel)).join('');
    }
    stackCount.textContent = stack.length;
}


document.addEventListener('keydown', function(e) {
    if (e.key === 'Enter' && e.target.tagName === 'INPUT') {
        e.preventDefault();
        addParcel();
    }
});
updateDisplay();