const {createApp} = Vue;

createApp({
    data(){
        return{
            productos:[],
            url:'http://127.0.0.1:5000/productos',
            cargando: true,
            error: false,
        }
    },
methods: {
    fetchApi(url){
        fetch(url)
        .then(res => res.json())
        .then(data =>{
            this.productos = data;
            this.cargando = false;  
        })
        .catch(err=>{
            console.error(err);
            this.error = true;
        })
    },
    eliminar(id){
        swal({
            title: "Are you sure?",
            text: "Once deleted, you will not be able to recover this imaginary file!",
            icon: "warning",
            buttons: true,
            dangerMode: true,
          })
        const url = this.url+"/"+id
        let options = {
            method: 'DELETE'
        }

        fetch(url,options)
        .then(res => res.json())
        .then(data =>{
            location.reload();
        })
        .catch(err => console.error(err))
    }
},
created(){
    this.fetchApi(this.url);

}
}).mount('#app')
