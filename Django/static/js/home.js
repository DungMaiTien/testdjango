function showButton(element) {
    var button = element.querySelector('.hidden-button');
    button.style.display = 'block';
}

function hideButton(element) {
    var button = element.querySelector('.hidden-button');
    button.style.display = 'none';
}

function addToCart(title, price) {
    // Tạo một yêu cầu AJAX hoặc Fetch API để thêm sản phẩm vào giỏ hàng
    // Bạn cần truyền tên và giá sản phẩm vào yêu cầu
    fetch('/add-to-cart/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken'),  // Lấy giá trị CSRF token
        },
        body: JSON.stringify({
            title: title,
            price: price,
        }),
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            alert('Sản phẩm đã được thêm vào giỏ hàng.');
        } else {
            alert('Có lỗi xảy ra khi thêm sản phẩm vào giỏ hàng.');
        }
    })
    .catch(error => {
        console.error('Lỗi: ' + error);
    });
}

// Hàm để lấy giá trị CSRF token từ cookie
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Tìm cookie có tên là csrftoken
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
function getProductInfo(cardElement) {
    const titleElement = cardElement.querySelector('.card-title');
    const priceElement = cardElement.querySelector('.product-price'); // Đã thêm class "product-price" vào thẻ small

    if (titleElement && priceElement) {
        const title = titleElement.textContent.trim();
        const price = priceElement.textContent.trim();

        // Gọi hàm addToCart với các giá trị title và price
        addToCart(title, price);
    }
}
