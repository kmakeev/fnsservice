'use strict';
    angular
        .module('myApp')
        .factory ('User', ['$resource',
            function($resource) {

            var resource =
             $resource("/api/user/", {},
             {
               query: {
                    method: 'GET',
                    isArray: false
               },
                logout: {
                    method: 'DELETE',
                    isArray: false
               },
             });
             resource.prototype.getUser = function () {
               console.log('In get User');
                return this.$query({});
            };
            return resource;
        }]);
