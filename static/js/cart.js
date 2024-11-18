document.addEventListener('DOMContentLoaded', function () {
    const cartCount = document.getElementById('cart-count');
    const checkoutLink = document.getElementById('checkout-link');

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
                        cartCount.textContent = data.total_items;
                        checkoutLink.style.display = 'inline-block'; // Muestra el enlace "Ir a Pagar"
                    }
                })
                .catch(error => console.error('Error:', error));
        });
    });
});
