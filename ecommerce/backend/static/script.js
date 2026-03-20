console.log("JS Loaded ✅");

// CART STORAGE
let cart = JSON.parse(localStorage.getItem("cart")) || [];

// IMAGE FUNCTION
function getImage(name) {
    name = name.toLowerCase();

    if (name.includes("apple")) return "/static/images/apple.png";
    if (name.includes("milk")) return "/static/images/milk.png";
    if (name.includes("bread")) return "/static/images/bread.png";
    if (name.includes("banana")) return "/static/images/banana.png";
    if (name.includes("orange")) return "/static/images/orange.png";
    if (name.includes("rice")) return "/static/images/rice.png";
    if (name.includes("eggs")) return "/static/images/eggs.png";
    if (name.includes("cheese")) return "/static/images/cheese.png";

    return `/static/images/${name}.png`;
}

// LOAD PRODUCTS
fetch('/products')
.then(res => res.json())
.then(data => {
    let container = document.getElementById('products');

    if (!container) return;

    data.forEach(p => {
        let div = document.createElement('div');
        div.className = 'product';

        div.innerHTML = `
            <img src="${getImage(p.name)}" class="product-img">
            <h3>${p.name}</h3>
            <p>₹${p.price}</p>
            <button onclick="addToCart('${p.name}', ${p.price})">Add to Cart</button>
        `;

        container.appendChild(div);
    });
});

// ADD TO CART
function addToCart(name, price) {
    let cart = JSON.parse(localStorage.getItem("cart")) || [];

    cart.push({name, price});

    localStorage.setItem("cart", JSON.stringify(cart));

    alert(name + " added to cart!");
}

// LOAD CART PAGE
function loadCart() {
    let cartItems = document.getElementById("cart-items");

    if (!cartItems) return;

    let cart = JSON.parse(localStorage.getItem("cart")) || [];
    let total = 0;

    cartItems.innerHTML = "";

    cart.forEach(item => {
        total += item.price;

        cartItems.innerHTML += `
            <div class="cart-item">
                ${item.name} - ₹${item.price}
            </div>
        `;
    });

    document.querySelector("h3").innerText = "Total: ₹" + total;
}

// AUTO LOAD
window.onload = function () {
    if (window.location.pathname === "/cart") {
        loadCart();
    }
};

// CHECKOUT
function checkout() {
    let cart = JSON.parse(localStorage.getItem("cart")) || [];

    localStorage.setItem("orders", JSON.stringify(cart));
    localStorage.removeItem("cart");

    alert("Order placed!");
    window.location.href = "/orders";
}