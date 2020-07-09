
/**
 * Display cart data on page load
 */
document.addEventListener('readystatechange', () => {
    fetch('/store/cart/count').then(resp => resp.json())
    .then(data => {
        console.log(data)
        document.getElementById("cart-count").innerHTML = `(${data.total})`
    })
})


/**
 * Add iterate over rendered table buttons
 * and add event listener to each .detete-btn class
 */
const addToCart = document.getElementById('add-to-cart');
const deleteBtns = document.querySelectorAll('.delete-btn');
if (deleteBtns !== null){
    for (let i = 0; i < deleteBtns.length; i++) {
        const btn = deleteBtns[i];
        btn.addEventListener('click', removeItemTable)
    }
}

function removeItemTable() {
    // event.target will be the input element.
    removeCartItem(event)
    var td = event.target.parentNode; 
    var tr = td.parentNode; 
    tr.parentNode.removeChild(tr);
}
/**
 * Remove Cart Item on button click 
 */
function removeCartItem(e) {
    var item_id = e.target.dataset['prodid'];
    if (item_id !== undefined){
        fetch('/store/cart/delete/'+item_id,{
            method:"DELETE",
        }).then(res => {
            if (res.ok) {
                return res.json();
            } else {
                return Promise.reject({ status: res.status, statusText: res.statusText })
            }
        })
        .then(data => {
              console.log(data)
          })
    }
    
}

/**
 * Add Item to Cart only after button has rendered 
 * and DOM Loaded
 */
if (addToCart !== null){
    addToCart.addEventListener('click', (e) => {
        e.preventDefault()
        const product_id = e.target.dataset['prod_id'];
        const item_qty = document.getElementById("item-qty").value
        const user_id = document.getElementById("user_id").value

       const data = {
            quantity: item_qty,
            product_id: product_id,
            user_id: user_id
        }
        console.log(data)
        fetch('/store/cart',{
            method:"POST",
            headers: {
                'Content-Type': 'application/json'
              },
            body: JSON.stringify(data)
        }).then(res => {
            if (res.ok) {
                return res.json();
            } else {
                return Promise.reject({ status: res.status, statusText: res.statusText })
            }
        })
        .then(data => {
              document.getElementById("success-msg").style.display = ''
              document.getElementById("cart-count").innerHTML = `(${data.total_count})`
          })
    })
}


/**
 * Handle Order form submission and redirect to thank you page.
 */

 const createOrderBtn = document.getElementById("create-order")

 if (createOrderBtn !== null){
     createOrderBtn.addEventListener('click', (e) => {
         e.preventDefault()
         makeOrder()
     })
 }


function makeOrder(){
    const paymentMethod = document.getElementsByName("paymentMethod")[0].value;
    const email = document.getElementById("email").value;
    const user_id = document.getElementById("user_id").value
    const city = document.getElementById("state").value
    const zip = document.getElementById("zip").value
    const country = document.getElementById("country").value;
    
    const data = {
        payment_method: paymentMethod,
        email: email,
        zip_code: zip,
        country: country,
        state: city,
        user_id: user_id
    }
    console.log(data)
    const options = {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        }, 
        body: JSON.stringify(data)
    }
    
    
    fetch('/store/orders/create', options)
    .then(res => {
        if (res.ok){
            return res
        }
        else {
            return Promise.reject({ status: res.status, statusText: res.statusText })
        }
    })
    .then(data => {
        console.log(data)
        location.href="/store/orders/complete";
    
    })
}