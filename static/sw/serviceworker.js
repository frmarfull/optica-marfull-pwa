var nombreCache = 'login-v1';

self.addEventListener("install", function(event){
    console.log("Instalado");
    event.waitUntil(
        caches.open(nombreCache)
        .then(function(cacheEncontrada){
            return cacheEncontrada.addAll([
                '/',
                '/productos/listarCatalogo/',
                '/static/css/bootstrap.min.css',
                '/static/js/jquery-3.5.1.slim.min.js',
                '/static/js/bootstrap.bundle.min.js',
                '/manifest.json'
            ]);
        })
    );
});

self.addEventListener('fetch', function(event){
    event.respondWith(
        caches.match(event.request)
        .then(function(cacheEncontrada){
            if(cacheEncontrada){
                return cacheEncontrada;
            }
            return fetch(event.request)
            .then(function(peticion){
                return peticion;
            })
        })
    )
})