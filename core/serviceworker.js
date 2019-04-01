// var cacheName = 'SWexamen';
// var filesToCache = [
// '/',
// ];
// self.addEventListener('install', function(event) {
//   event.waitUntil(
//     caches.open(cacheName).then(function(cache) {
//       return cache.addAll(filesToCache);
//     })
//   );
// });

// self.addEventListener('fetch', function(event) {
//     event.respondWith(
//       caches.match(event.request)
//         .then(function(response) {
//           if (response) {
//             return response;
//           }
//           var fetchRequest = event.request.clone();
//           return fetch(fetchRequest).then(
//             function(response) {
//               if(!response || response.status !== 200 || response.type !== 'basic') {
//                 return response;
//               }
//               var responseToCache = response.clone();
//               caches.open(cacheName)
//                 .then(function(cache) {
//                   cache.put(event.request, responseToCache);
//                 });
//               return response;
//             }
//           );
//         })
//       );
//   });

'use strict';

self.addEventListener('push', function(event) {
    console.log('[Service Worker] Push Received.');
    console.log(`[Service Worker] Push had this data: "${event.data.text()}"`);
  
    const title = 'Notificacion lista de compras';
    const options = {
      body: 'Prueba.',
      icon: 'static/core/img/icon.png',
      badge: 'static/core/img/badge.png'
    };
  
    event.waitUntil(self.registration.showNotification(title, options));
  });
  
self.addEventListener('notificationclick', function(event) {
  console.log('[Service Worker] Notification click Received.');

  event.notification.close();

  event.waitUntil(
    clients.openWindow('http://localhost:8000/listaproductoapi')
  );
});