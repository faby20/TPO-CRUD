// para recuperar los datos URL y mostralo en los input
console.log(location.search);

let argsUrl = location.search.substring(1).split("&");
console.log(argsUrl);

let data = [];
for (let i = 0; i < argsUrl.length; i++) {
  data[i] = argsUrl[i].split("=");
}
console.log(data);

document.getElementById("id").value = decodeURIComponent(data[0][1]);
document.getElementById("nombre").value = decodeURIComponent(data[1][1]);
document.getElementById("precio").value = decodeURIComponent(data[2][1]);
document.getElementById("stock").value = decodeURIComponent(data[3][1]);
document.getElementById("imagen").value = decodeURIComponent(data[4][1]);

// 2 actualuzar los datos
function modificar() {
 let id = document.getElementById("id").value;
  let n = document.getElementById("nombre").value;
  let p = document.getElementById("precio").value;
  let s = document.getElementById("stock").value;
  let i = document.getElementById("imagen").value;

  // se crea la variable producto, q va aser un objeto
  let producto = {
    nombre: n,
    precio: p,
    stock: s,
    imagen: i
  };
  let url = "http://127.0.0.1:5000/productos/" + id;
  let options = {
    body: JSON.stringify(producto),
    method: "PUT",
    headers: { 'Content-Type': 'application/json'}
  };
  fetch(url, options)
    .then(function(){
      alert('Producto editado exitosamente!');
      window.location.href = './productos.html';
    })
    .catch(err => {
      alert('No pudo modificarse el producto');
      console.error(err);
    });
}
