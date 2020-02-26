'use strict';
    angular
        .module('myApp')
        .factory ('Filters', ['$resource',
            function($resource) {

            var resource =
             $resource("/api/filters/", {},
             {
               query: {
                    method: 'GET',
                    isArray: false
               },

             });

            return resource;
        }]);