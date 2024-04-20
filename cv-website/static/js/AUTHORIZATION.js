function send_auth() {
     
    var data = {
        login: document.querySelector('input[name="login"]').value,
        password: document.querySelector('input[name="password"]').value
      };
      
      fetch('/authorization', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify(data)
      })
        .then(response => response.json())
        .then(data => window.location.href = "/" + data["reflink"])
        .catch(error => console.error('Error:', error));      
}