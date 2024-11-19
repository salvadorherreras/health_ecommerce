document.addEventListener('DOMContentLoaded', function () {
    // Eliminar un artículo individual
    document.querySelectorAll('.btn-remove').forEach(button => {
        button.addEventListener('click', function () {
            const productId = this.getAttribute('data-product-id');

            fetch(`/remove_item/${productId}`, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' }
            })
                .then(response => response.json())
                .then(data => {
                    if (data.status === 'success') {
                        location.reload(); // Refresca la página
                    }
                })
                .catch(error => console.error('Error:', error));
        });
    });

    // Eliminar artículos seleccionados
    document.getElementById('remove-selected').addEventListener('click', function () {
        const selectedItems = Array.from(document.querySelectorAll('.select-item:checked')).map(
            checkbox => checkbox.value
        );

        fetch('/remove_selected', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ items: selectedItems })
        })
            .then(response => response.json())
            .then(data => {
                if (data.status === 'success') {
                    location.reload(); // Refresca la página
                }
            })
            .catch(error => console.error('Error:', error));
    });
});

document.addEventListener('DOMContentLoaded', function () {
    const cartCount = document.getElementById('cart-count');

    // Manejar clics en los botones "Añadir al Carrito"
    document.querySelectorAll('.add-to-cart').forEach(button => {
        button.addEventListener('click', function (event) {
            event.preventDefault();
            const productId = this.getAttribute('data-product-id');

            fetch(`/add_to_cart/${productId}`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                }
            })
                .then(response => response.json())
                .then(data => {
                    if (data.status === 'success') {
                        // Actualiza el contador en la cabecera
                        cartCount.textContent = data.total_items;
                    }
                })
                .catch(error => console.error('Error:', error));
        });
    });

        // Incrementar cantidad
        document.querySelectorAll('.increment').forEach(button => {
            button.addEventListener('click', function () {
                const productId = this.getAttribute('data-product-id');
    
                fetch(`/increment_item/${productId}`, {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' }
                })
                    .then(response => response.json())
                    .then(data => {
                        if (data.status === 'success') {
                            location.reload(); // Refresca la página para ver los cambios
                        }
                    })
                    .catch(error => console.error('Error:', error));
            });
        });
    
        // Decrementar cantidad
        document.querySelectorAll('.decrement').forEach(button => {
            button.addEventListener('click', function () {
                const productId = this.getAttribute('data-product-id');
    
                fetch(`/decrement_item/${productId}`, {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' }
                })
                    .then(response => response.json())
                    .then(data => {
                        if (data.status === 'success') {
                            location.reload(); // Refresca la página para ver los cambios
                        }
                    })
                    .catch(error => console.error('Error:', error));
            });
        });

});

